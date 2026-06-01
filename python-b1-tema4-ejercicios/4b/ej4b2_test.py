from ej4b2 import average_score_ram, average_score_heap


def test_average_score_ram():
    # Test para la función average_score_ram
    assert average_score_ram({"Juan": 8, "Maria": 7, "Pedro": 9}) == 8.0, "average_score_ram does not return the correct value for input {'Juan': 8, 'Maria': 7, 'Pedro': 9}. It should be 8.0"
    assert average_score_ram({"Juan": 6, "Maria": 6, "Pedro": 6}) == 6.0, "average_score_ram does not return the correct value for input {'Juan': 6, 'Maria': 6, 'Pedro': 6}. It should be 6.0"
    assert average_score_ram({"Juan": 10, "Maria": 9, "Pedro": 8}) == 9.0, "average_score_ram does not return the correct value for input {'Juan': 10, 'Maria': 9, 'Pedro': 8}. It should be 9.0"


def test_average_score_heap():
    # Test para la función average_score_heap
    assert average_score_heap({"Juan": 8, "Maria": 7, "Pedro": 9}) == 8.0, "average_score_heap does not return the correct value for input {'Juan': 8, 'Maria': 7, 'Pedro': 9}. It should be 8.0"
    assert average_score_heap({"Juan": 6, "Maria": 6, "Pedro": 6}) == 6.0, "average_score_heap does not return the correct value for input {'Juan': 6, 'Maria': 6, 'Pedro': 6}. It should be 6.0"
    assert average_score_heap({"Juan": 10, "Maria": 9, "Pedro": 8}) == 9.0, "average_score_heap does not return the correct value for input {'Juan': 10, 'Maria': 9, 'Pedro': 8}. It should be 9.0"
