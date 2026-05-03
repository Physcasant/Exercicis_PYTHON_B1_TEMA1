from ej1b3 import line_graph

import pytest
import matplotlib.pyplot as plt

def test_line_graph():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    line_graph(x, y)
    ax = plt.gca()
    assert ax.get_xlabel() == 'Axis X', "no label in Axis X detected"
    assert ax.get_ylabel() == 'Axis Y', "no label in Axis Y detected"
    assert ax.get_title() == 'Graph', "no title detected"
    assert len(plt.get_fignums()) == 1, "number of figures is not 1"