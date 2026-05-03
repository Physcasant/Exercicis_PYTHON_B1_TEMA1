import pytest
from ej2c3 import factorial, calculate_factorial


def test_factorial():
    assert factorial(5) == 120, "factorial does not return the correct value for input 5. It should be 120"
    assert factorial(0) == 1, "factorial does not return the correct value for input 0. It should be 1"
    with pytest.raises(
        ValueError, match="Factorial of a negative number cannot be calculated"
    ):
        factorial(-5)
    with pytest.raises(
        ValueError, match="Factorial of a negative number cannot be calculated"
    ):
        factorial(-1)
    assert calculate_factorial(8) == 40320, "calculate_factorial does not return the correct value for input 8. It should be 40320"
    assert calculate_factorial(-10).__contains__("An unexpected error has occurred:"), "calculate_factorial does not return the correct value for input -10. It should contain 'An unexpected error has occurred:'"
