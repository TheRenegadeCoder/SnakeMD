import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

MAJOR = 2
MINOR = 0
PATCH = 0
PRE = ""

name = "SnakeMD"
version = f"{MAJOR}.{MINOR}"
release = f"{MAJOR}.{MINOR}.{PATCH}{PRE}"
setuptools.setup(
    name=name,
    version=release,
    author="The Renegade Coder",
    author_email="jeremy.grifski@therenegadecoder.com",
    description="A markdown generation library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRenegadeCoder/SnakeMD",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Documentation :: Sphinx",
    ]
)
