from ej1b4 import results
import numpy as np

def test_results():
    #Primer Test
    numbers = [1, 2, 3, 4, 5]
    ave, standard = results(numbers)
    assert round(ave,2) == 3.0, "results does not return the correct average value for input [1, 2, 3, 4, 5]. It should be 3.0"
    assert round(standard,2) == 1.41, "results does not return the correct standard deviation value for input [1, 2, 3, 4, 5]. It should be 1.41"

    #Segundo Test
    numbers = [10, 20, 30, 40, 50]
    ave, standard = results(numbers)
    assert round(ave,2) == 30, "results does not return the correct average value for input [10, 20, 30, 40, 50]. It should be 30"
    assert round(standard,2) == 14.14, "results does not return the correct standard deviation value for input [10, 20, 30, 40, 50]. It should be 14.14"
