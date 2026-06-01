import os
import sys
from ej4d3 import read_and_write

def test_read_and_write(capsys, monkeypatch):
    input_values = ["Julio\n", "30\n"]
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))

    read_and_write()

    assert os.path.isfile("file.txt"), "The file.txt file should be created"
    with open("file.txt", "r") as file:
        assert file.read() != "", "The file.txt file should not be empty"

    captured = capsys.readouterr()
    assert captured.out.strip() == "Julio\n\n30", "The output should be 'Julio\\n\\n30'"
