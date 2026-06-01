import pytest

from ej4b1 import squared_sum_ram, squared_sum_heap


def test_squared_sum_ram():
    numbers_list = [6, 4, 7]
    expected_result = 101
    assert squared_sum_ram(numbers_list) == expected_result, "squared_sum_ram does not return the correct value for input [6, 4, 7]. It should be 101"


def test_squared_sum_heap():
    numbers_list = [6, 4, 7]
    expected_result = 101
    assert squared_sum_heap(numbers_list) == expected_result, "squared_sum_heap does not return the correct value for input [6, 4, 7]. It should be 101"
