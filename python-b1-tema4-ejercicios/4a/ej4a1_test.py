from ej4a1 import find_intersection


def test_find_intersection():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    resultado = find_intersection(lista1, lista2)
    assert resultado == [4, 5], "find_intersection does not return the correct value for input ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]). It should be [4, 5]"

    lista3 = [1, 2, 3]
    lista4 = [4, 5, 6]
    resultado = find_intersection(lista3, lista4)
    assert resultado == [], "find_intersection does not return the correct value for input ([1, 2, 3], [4, 5, 6]). It should be an empty list []"

    lista5 = []
    lista6 = [1, 2, 3]
    resultado = find_intersection(lista5, lista6)
    assert resultado == [], "find_intersection does not return the correct value for input ([], [1, 2, 3]). It should be an empty list []"
