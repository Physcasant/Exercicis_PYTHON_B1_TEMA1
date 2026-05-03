from ej1c3 import find_max


def test_preorder():
    assert find_max([1, 2, 3, 4, 5]) == 5, "find_max does not return the correct value for input [1, 2, 3, 4, 5]. It should be 5"
    assert find_max([102, 2, 3, 4, 5]) == 102, "find_max does not return the correct value for input [102, 2, 3, 4, 5]. It should be 102"
    assert find_max([3, 40005, 5]) == 40005, "find_max does not return the correct value for input [3, 40005, 5]. It should be 40005"
