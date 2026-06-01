from ej4d1 import sum
from io import StringIO
import pytest

def test_sum(monkeypatch, capsys):
    inputs = iter(['3', '2']) # Primero simula 3, luego 2
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = sum()

    captured = capsys.readouterr()
    assert captured.out == "Result:  5\n", "sum does not print the correct value for input 3 and 2. It should be 'Result: 5'"

    assert result == 5, "sum does not return the correct value for input 3 and 2. It should be 5"       