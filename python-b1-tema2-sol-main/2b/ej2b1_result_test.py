from ej2b1 import sum_list_numbers
from flake8.api import legacy as flake8
import os, pathlib


def test_suma():
    assert sum_list_numbers([1, 2, 3, 4]) == 10, "sum_list_numbers does not return the correct value for input [1, 2, 3, 4]. It should be 10"
    assert sum_list_numbers([1, 2, 3, 4, 5]) == 15, "sum_list_numbers does not return the correct value for input [1, 2, 3, 4, 5]. It should be 15"
    assert sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80]) == 339.35, "sum_list_numbers does not return the correct value for input [50, 10.5, 21, 37.2, 99.9, 40.75, 80]. It should be 339.35"
    
def test_pep8_conformity():
    # Checking how pytest was called lo locate the file
    launch_path = pathlib.Path.cwd()
    exercise = "ej2b1.py"
    if str(launch_path).split(os.sep)[-1].startswith("python-b1"):
        exercise = "2b/" + exercise

    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([exercise])
    assert report.get_statistics("E") == [], "Your code does not comply with PEP8. Please review your code"
