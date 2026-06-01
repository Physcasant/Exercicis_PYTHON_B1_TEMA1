import pytest
from ej4c3 import Triangle, Rectangle, Shape


def test_triangle_get_area():
    triangle = Triangle([3, 4, 5], 4, 3)
    assert triangle.get_area() == 6.0, "Triangle.get_area() does not return the correct value for input [3, 4, 5], 4, 3. It should be 6.0"


def test_rectangle_get_area():
    rectangle = Rectangle([5, 5, 2, 2], 5, 2)
    assert rectangle.get_area() == 10, "Rectangle.get_area() does not return the correct value for input [5, 5, 2, 2], 5, 2. It should be 10"
