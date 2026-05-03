from ej2a1 import (
    sum_even_numbers_in_list_while,
    sum_even_numbers_in_list_for,
    sum_even_numbers_in_list_do_while,
)


def test_sum_even_numbers_list():
    assert sum_even_numbers_in_list_while([1, 2, 3, 4, 5, 6]) == 12, "sum_even_numbers_in_list_while does not return the correct value for input [1, 2, 3, 4, 5, 6]. It should be 12"
    assert sum_even_numbers_in_list_while([1, 3, 5.0, 7, 9, 10.0]) == 10, "sum_even_numbers_in_list_while does not return the correct value for input [1, 3, 5.0, 7, 9, 10.0]. It should be 10"
    assert sum_even_numbers_in_list_while([]) == 0, "sum_even_numbers_in_list_while does not return the correct value for input []. It should be 0"
    assert sum_even_numbers_in_list_for([2, 4, 6, 8, 10]) == 30, "sum_even_numbers_in_list_for does not return the correct value for input [2, 4, 6, 8, 10]. It should be 30"
    assert sum_even_numbers_in_list_for([3, 4, 11, 8, 10]) == 22, "sum_even_numbers_in_list_for does not return the correct value for input [3, 4, 11, 8, 10]. It should be 22"
    assert sum_even_numbers_in_list_for([1.0, 4, 6, -3, 10]) == 20, "sum_even_numbers_in_list_for does not return the correct value for input [1.0, 4, 6, -3, 10]. It should be 20"
    assert sum_even_numbers_in_list_do_while([-2, 0, 2]) == 0, "sum_even_numbers_in_list_do_while does not return the correct value for input [-2, 0, 2]. It should be 0"
    assert sum_even_numbers_in_list_do_while([2.0, 0, -2]) == 0, "sum_even_numbers_in_list_do_while does not return the correct value for input [2.0, 0, -2]. It should be 0"
    assert sum_even_numbers_in_list_do_while([1, 0, 8, 3, 10]) == 18, "sum_even_numbers_in_list_do_while does not return the correct value for input [1, 0, 8, 3, 10]. It should be 18"
