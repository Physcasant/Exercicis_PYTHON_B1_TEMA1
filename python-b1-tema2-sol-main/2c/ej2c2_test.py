from ej2c2 import get_element_from_list


def test_get_element_from_list():
    assert get_element_from_list([1, 2, 3], 0) == 1, "get_element_from_list does not return the correct value for input ([1, 2, 3], 0). It should be 1"
    assert get_element_from_list([1, 2, 3], 1) == 2, "get_element_from_list does not return the correct value for input ([1, 2, 3], 1). It should be 2"   
    assert (
        get_element_from_list([1, 2, 3], 3)
        == "The specified index is out of the items_list's range"
    ), "get_element_from_list does not return the correct value for input ([1, 2, 3], 3). It should be 'The specified index is out of the items_list's range'"
    assert (
        get_element_from_list([], 0)
        == "The specified index is out of the items_list's range"
    ), "get_element_from_list does not return the correct value for input ([], 0). It should be 'The specified index is out of the items_list's range'"
    assert get_element_from_list(5, 0).__contains__("An unexpected error has occurred:"), "get_element_from_list does not return the correct value for input (5, 0). It should contain 'An unexpected error has occurred:'"
