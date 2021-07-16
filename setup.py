import setuptools
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

with open("README.md", "r") as fh:
    long_description = fh.read()

name = "snakemd"
version = "1.0"
release = "1.0.0"
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
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docsrc'),
            'build_dir': ('setup.py', 'docsrc/_build'),
            'builder': ("setup.py", "dirhtml")
        }
    },
)
