"""Build distributions and check a consumer against an isolated installed wheel.

Run with Python 3.10+ and the tools in tests/typing/requirements.txt installed:
    python tests/check_installed_typing.py
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parent.parent


def run(*args: str, cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, env=env, text=True, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--python",
        default=sys.executable,
        help="target Python interpreter (defaults to the checker interpreter)",
    )
    requested_python = parser.parse_args().python
    target_python = os.path.abspath(shutil.which(requested_python) or requested_python)
    env = os.environ.copy()
    for name in ("PYTHONPATH", "MYPYPATH", "PYTHONHOME"):
        env.pop(name, None)
    with tempfile.TemporaryDirectory(prefix="snakemd-typing-") as temp:
        work = Path(temp)
        dist = work / "dist"
        run(
            sys.executable,
            "-m",
            "build",
            "--no-isolation",
            "--outdir",
            str(dist),
            cwd=ROOT,
            env=env,
        )
        (wheel,) = dist.glob("*.whl")
        (sdist,) = dist.glob("*.tar.gz")
        with zipfile.ZipFile(wheel) as archive:
            assert "snakemd/py.typed" in archive.namelist(), "wheel lacks py.typed"
        with tarfile.open(sdist) as archive:
            assert any(
                name.endswith("/snakemd/py.typed") for name in archive.getnames()
            ), "sdist lacks py.typed"

        venv = work / "venv"
        run(target_python, "-m", "venv", str(venv), cwd=work, env=env)
        python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        run(
            str(python),
            "-m",
            "pip",
            "install",
            "--no-index",
            "--no-deps",
            str(wheel),
            cwd=work,
            env=env,
        )
        run(
            str(python),
            "-c",
            "import importlib.metadata as m, snakemd; "
            "assert 'site-packages' in snakemd.__file__; "
            "assert not any(d.metadata['Name'].lower().replace('_', '-') == 'snakemd-stubs' for d in m.distributions())",
            cwd=work,
            env=env,
        )

        for name in ("consumer.py", "negative.py", "public_api.py"):
            shutil.copy(ROOT / "tests" / "typing" / name, work / name)
        (work / "input.csv").write_text("header\ncell\n", encoding="utf-8")
        run(
            str(python),
            "-c",
            "from pathlib import Path; from public_api import exercise_public_api; "
            "exercise_public_api(Path('input.csv'), Path('.'))",
            cwd=work,
            env=env,
        )
        version = subprocess.check_output(
            [
                str(python),
                "-c",
                "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')",
            ],
            cwd=work,
            env=env,
            text=True,
        ).strip()
        config = work / "mypy.ini"
        config.write_text("[mypy]\n", encoding="utf-8")
        # Each checker resolves imports from the clean wheel-only environment,
        # while its own tools live outside that environment.
        checkers = {
            "mypy": (
                sys.executable,
                "-m",
                "mypy",
                "--strict",
                "--no-incremental",
                "--cache-dir",
                os.devnull,
                "--config-file",
                str(config),
                "--python-version",
                version,
                "--python-executable",
                str(python),
            ),
            "pyright": (
                sys.executable,
                "-m",
                "pyright",
                "--outputjson",
                "--pythonversion",
                version,
                "--pythonpath",
                str(python),
            ),
            "ty": (
                sys.executable,
                "-m",
                "ty",
                "check",
                "--output-format",
                "concise",
                "--color",
                "never",
                "--error-on-warning",
                "--python-version",
                version,
                "--python",
                str(python),
            ),
        }
        # Check the source at the same target version, independently of the
        # stricter installed-consumer fixtures below.
        source_checks = {
            "mypy": (
                sys.executable,
                "-m",
                "mypy",
                "--no-incremental",
                "--cache-dir",
                os.devnull,
                "--config-file",
                str(config),
                "--python-version",
                version,
                "--python-executable",
                str(python),
            ),
            "pyright": (
                sys.executable,
                "-m",
                "pyright",
                "--pythonversion",
                version,
                "--pythonpath",
                str(python),
            ),
            "ty": (
                sys.executable,
                "-m",
                "ty",
                "check",
                "--python-version",
                version,
                "--python",
                str(python),
                "--error-on-warning",
            ),
        }
        for name, command in source_checks.items():
            run(*command, str(ROOT / "snakemd"), cwd=ROOT, env=env)
            print(f"{name}: source check passed for Python {version}")
        negative_lines = [
            line
            for line, text in enumerate(
                (work / "negative.py").read_text().splitlines(), 1
            )
            if "link: str =" in text or "Inline(123)" in text or ".add_row(" in text
        ]
        assert len(negative_lines) == 3, "negative fixture must exercise three errors"
        for name, command in checkers.items():
            run(*command, "consumer.py", cwd=work, env=env)
            run(*command, "public_api.py", cwd=work, env=env)
            negative = subprocess.run(
                (*command, "negative.py"),
                cwd=work,
                env=env,
                text=True,
                capture_output=True,
            )
            assert (
                negative.returncode != 0
            ), f"{name}: negative consumer unexpectedly passed"
            if name == "pyright":
                result = json.loads(negative.stdout)
                errors = {
                    (item["range"]["start"]["line"] + 1, item.get("rule"))
                    for item in result["generalDiagnostics"]
                    if item["severity"] == "error"
                }
                rules = (
                    "reportAssignmentType",
                    "reportArgumentType",
                    "reportArgumentType",
                )
            elif name == "mypy":
                errors = {
                    (int(line), code)
                    for line, code in re.findall(
                        r"negative\.py:(\d+): .*?\[([a-z-]+)\]", negative.stdout
                    )
                }
                rules = ("assignment", "arg-type", "arg-type")
            else:
                errors = {
                    (int(line), code)
                    for line, code in re.findall(
                        r"negative\.py:(\d+):\d+: error\[([a-z-]+)\]", negative.stdout
                    )
                }
                rules = (
                    "invalid-assignment",
                    "invalid-argument-type",
                    "invalid-argument-type",
                )
            expected = set(zip(negative_lines, rules))
            assert expected <= errors, (
                f"{name}: missing expected errors {expected - errors}\n"
                f"stdout: {negative.stdout}\nstderr: {negative.stderr}"
            )
            print(f"{name}: installed-wheel consumer checks passed")
        print("Wheel and sdist include py.typed.")


if __name__ == "__main__":
    main()
