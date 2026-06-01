from ej4b3 import create_list

import pytest
from random import randint
from typing import List, Tuple


def test_create_list_returns_tuple_of_two_lists():
    # GIVEN
    length_list = 4

    # WHEN
    result = create_list(length_list)

    # THEN
    assert isinstance(result, tuple), "create_list should return a tuple"
    assert len(result) == 2, "create_list should return two lists"
    assert isinstance(result[0], list), "the first element returned by create_list should be a list"
    assert isinstance(result[1], list), "the second element returned by create_list should be a list"


def test_create_list_lists_have_same_length():
    # GIVEN
    length_list = 5

    # WHEN
    ram_list, heap_list = create_list(length_list)

    # THEN
    assert len(ram_list) == len(heap_list), "the lists returned by create_list should have the same length"


def test_create_list_ram_list_contains_random_integers():
    # GIVEN
    length_list = 7

    # WHEN
    ram_list, _ = create_list(length_list)

    # THEN
    assert all(isinstance(i, int) for i in ram_list), "the first list returned by create_list should contain only integers"
    assert all(0 <= i <= 100 for i in ram_list), "the first list returned by create_list should contain only integers between 0 and 100"


def test_create_list_heap_list_is_a_copy_of_ram_list():
    # GIVEN
    length_list = 8

    # WHEN
    ram_list, heap_list = create_list(length_list)

    # THEN
    assert ram_list == heap_list, "the second list returned by create_list should be a copy of the first list"
    assert id(ram_list) != id(heap_list), "the second list returned by create_list should be a copy of the first list"


def test_create_list_with_zero_length():
    # GIVEN
    length_list = 0

    # WHEN
    ram_list, heap_list = create_list(length_list)

    # THEN
    assert len(ram_list) == 0, "the first list returned by create_list should be empty for length_list 0"
    assert len(heap_list) == 0, "the second list returned by create_list should be empty for length_list 0"


def test_create_list_with_negative_length():
    # GIVEN
    length_list = -5

    # WHEN / THEN
    with pytest.raises(ValueError):
        create_list(length_list)
