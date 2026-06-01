from ej3a2_main import arithmetic, geometry

# archivo: test_arithmetic.py
def test_square_root():
    assert arithmetic.square_root(9) == 3,  "The square root operation does not work"
    assert arithmetic.square_root(16) == 4,  "The square root operation does not work"


def test_power():
    assert arithmetic.power(3, 2) == 9,  "The power operation does not work"
    assert arithmetic.power(5, 3) == 125,  "The power operation does not work"


# archivo: test_geometry.py
def test_square_area():
    result = geometry.square_area(5)
    assert result == 25,  "The square_area operation does not work"


def test_rectangle_area():
    result = geometry.rectangle_area(3, 5)
    assert result == 15,  "The rectangle_area operation does not work"


def test_triangle_area():
    result = geometry.triangle_area(3, 5)
    assert result == 7.5,  "The triangle_area operation does not work"


def test_circle_area():
    result = geometry.circle_area(5)
    assert round(result, 2) == 78.54,  "The circle_area operation does not work"
