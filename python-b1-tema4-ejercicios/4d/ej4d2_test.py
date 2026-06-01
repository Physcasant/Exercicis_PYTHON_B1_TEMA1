from ej4d2 import create_read_file
from io import StringIO
import os
import sys
import re

def test_create_read_file(capsys):
    create_read_file()

    assert os.path.isfile('text_file.txt')

    captured = capsys.readouterr()
    output = captured.out

    assert output.strip() != ""

    with open('text_file.txt', 'r') as f:
        lines = f.readlines()
        assert isinstance(lines[0].strip(), str), "The first line of the file should be a string"
        assert isinstance(lines[1].strip(), str), "The second line of the file should be a string"
        assert isinstance(int(lines[2].strip()), int), "The third line of the file should be an integer"