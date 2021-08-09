#!/usr/bin/env python
# Find all project Python files and use autopep8 to autoformat

from os import system
from os.path import dirname, realpath
from pathlib import Path

# path to backend directory
dir_path = dirname(dirname(realpath(__file__)))

# list all *.py files in backend directory
files = list(
    map(lambda x: str(x),
        list(Path(dir_path).rglob("*.py"))
        )
)
print('Starting autoformat files...')
# filter out virtual env directories
py_files = list(
    filter(
        lambda file: ".venv" not in file and "venv" not in file,
        files))
for file in py_files:
    system("autopep8 --in-place --aggressive --aggressive {0}".format(file))
print('Autoformat is finished successfully.')
