from ej2b3 import triangle_area_calculate
from flake8.api import legacy as flake8

import pytest
import os, pathlib


def test_triangle_area_calculate():
    assert triangle_area_calculate(3, 5) == 7.5, "triangle_area_calculate does not return the correct value for input 3, 5. It should be 7.5"
    assert triangle_area_calculate(10, 5) == 25, "triangle_area_calculate does not return the correct value for input 10, 5. It should be 25"
    assert triangle_area_calculate(33, 45) == 742.5, "triangle_area_calculate does not return the correct value for input 33, 45. It should be 742.5"


def test_triangle_area_calculate_invalid_numbers():
    with pytest.raises(ValueError):
        triangle_area_calculate(0, 5)
    with pytest.raises(ValueError):
        triangle_area_calculate(0, -5)


def test_pep8_conformity():
    # Checking how pytest was called lo locate the file
    launch_path = pathlib.Path.cwd()
    exercise = "ej2b3.py"
    if str(launch_path).split(os.sep)[-1].startswith("python-b1"):
        exercise = "2b/" + exercise

    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([exercise])
    print(report)
    assert report.total_errors == 0, "Your code does not comply with PEP8. Please review your code"
