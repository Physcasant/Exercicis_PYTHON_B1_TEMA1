from ej1b2 import calculate_angle
import math


def test_calculate_angle():
    assert calculate_angle(0) == 0, "calculate_angle does not return the correct value for input 0. It should be 0"
    assert calculate_angle(90) == 1, "calculate_angle does not return the correct value for input 90. It should be 1"
    assert math.isclose(calculate_angle(180), 0, rel_tol=0.01), "calculate_angle does not return the correct value for input 180. It should be around 0"
    assert math.isclose(calculate_angle(270), -1, rel_tol=0.01), "calculate_angle does not return the correct value for input 270. It should be around -1"
    assert math.isclose(calculate_angle(45), 0.71, rel_tol=0.01), "calculate_angle does not return the correct value for input 45. It should be around 0.71"