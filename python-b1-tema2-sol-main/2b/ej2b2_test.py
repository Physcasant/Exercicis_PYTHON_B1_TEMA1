from ej2b2 import check_leap_year
from flake8.api import legacy as flake8

import os, pathlib


def test_check_leap_year():
    assert check_leap_year(2020) is True, "check_leap_year does not return the correct value for input 2020. It should be True"
    assert check_leap_year(2000) is True, "check_leap_year does not return the correct value for input 2000. It should be True"
    assert check_leap_year(2023) is False, "check_leap_year does not return the correct value for input 2023. It should be False"
    assert check_leap_year(2025) is False, "check_leap_year does not return the correct value for input 2025. It should be False"


def test_pep8_conformity():
    # Checking how pytest was called lo locate the file
    launch_path = pathlib.Path.cwd()
    exercise = "ej2b2.py"
    if str(launch_path).split(os.sep)[-1].startswith("python-b1"):
        exercise = "2b/" + exercise

    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([exercise])
    assert report.total_errors == 0, "Your code does not comply with PEP8. Please review your code"
