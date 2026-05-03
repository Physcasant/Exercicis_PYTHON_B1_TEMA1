from ej2d3 import division_list
import pytest


def test_division_list():
    # Lista con un string y un cero
    list_numbers = [1, "a", 9, 0, 22]
    scalar_number = 2
    with pytest.raises(TypeError):
        division_list(list_numbers, scalar_number)

    list_numbers = [1.5, 2.5, 9.2, 0, 22]
    scalar_number = 7.1
    list_result = division_list(list_numbers, scalar_number)
    assert (
            list_result ==
            [0.21126760563380284, 0.35211267605633806, 1.295774647887324, 0.0, 3.098591549295775]
    ), "division_list does not return the correct value for input [1.5, 2.5, 9.2, 0, 22] and 7.1. It should be [0.21126760563380284, 0.35211267605633806, 1.295774647887324, 0.0, 3.098591549295775]"
