from ej1c1 import mult_recursive


def test_mult_recursive():
    assert mult_recursive(0, 3) == 0, "Must return 0 for value 0 and times 3"
    assert mult_recursive(2, 3) == 6, "Must return 6 for value 2 and times 3"
    assert mult_recursive(5, 2) == 10, "Must return 10 for value 5 and times 2"
    assert mult_recursive(10, 10) == 100, "Must return 100 for value 10 and times 10"
