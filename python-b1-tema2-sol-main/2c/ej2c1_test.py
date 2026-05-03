from ej2c1 import convert_to_integer


def test_convert_to_integer():
    assert convert_to_integer("10") == 10, "convert_to_integer does not return the correct value for input '10'. It should be 10"
    assert convert_to_integer("-10") == -10, "convert_to_integer does not return the correct value for input '-10'. It should be -10"
    assert convert_to_integer("10.5") == "The string cannot be converted to an integer", "convert_to_integer does not return the correct value for input '10.5'. It should be 'The string cannot be converted to an integer'"
    assert convert_to_integer("abc") == "The string cannot be converted to an integer", "convert_to_integer does not return the correct value for input 'abc'. It should be 'The string cannot be converted to an integer'"
    assert convert_to_integer(["5"]).__contains__("An unexpected error has occurred:"), "convert_to_integer does not return the correct value for input ['5']. It should be 'An unexpected error has occurred:'"
