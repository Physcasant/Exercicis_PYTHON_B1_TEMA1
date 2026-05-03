from ej2d1 import kg_to_lb
import pytest


def test_kg_to_lb():
    assert kg_to_lb(1) == 2.20, "kg_to_lb does not return the correct value for input 1. It should be 2.20"

    with pytest.raises(ValueError):
        kg_to_lb(-1), "kg_to_lb does not raise an exception for input -1. It should raise a ValueError"

    with pytest.raises(TypeError):
        kg_to_lb("abc"), "kg_to_lb does not raise an exception for input 'abc'. It should raise a TypeError"
