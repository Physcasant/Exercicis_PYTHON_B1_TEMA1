from ej1c2 import invert_list


def test_invert_list():
    # Prueba básica con una lista de números enteros
    assert invert_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "invert_list does not return the correct value for input [1, 2, 3, 4, 5]. It should be [5, 4, 3, 2, 1]"
    # Prueba con una lista de cadenas
    assert invert_list(["a", "b", "c", "d", "e"]) == ["e", "d", "c", "b", "a"], "invert_list does not return the correct value for input ['a', 'b', 'c', 'd', 'e']. It should be ['e', 'd', 'c', 'b', 'a']"
    # Prueba con una lista vacía
    assert invert_list([]) == [], "invert_list does not return the correct value for input []. It should be []"
    # Prueba con una lista que contiene un solo elemento
    assert invert_list([10]) == [10], "invert_list does not return the correct value for input [10]. It should be [10]"
