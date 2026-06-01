"""
Enunciado:

Crea una función llamada 'count_fruits(fruits_list)' que reciba como parámetro una lista
de frutas y retorne un diccionario donde cada llave sea el nombre de una
fruta y su valor sea la cantidad de veces que aparece en la lista.

Parámetros:
    fruits_list: lista de frutas

Retorno:
    Un diccionario donde cada llave es el nombre de una fruta y su valor es
    la cantidad de veces que aparece en la lista.

Ejemplo:
    Entrada:
    fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
    count_fruits(fruits)

    Salida:
    {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}

Enunciat:

Crea una funció anomenada 'count_fruits(fruits_list)' que rebi com a paràmetre una llista
de fruites i retorni un diccionari on cada clau sigui el nom d'una
fruita i el seu valor sigui la quantitat de vegades que apareix a la llista.

Paràmetres:
     fruits_list: llista de fruites

Retorn:
     Un diccionari on cada clau és el nom d'una fruita i el seu valor és
     la quantitat de vegades que apareix a la llista.

Exemple:
     Entrada:
     fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
     count_fruits(fruits)

     Sortida:
     {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}    
"""


def count_fruits(fruits_list):
    fruit_count = {}
    for fruit in fruits_list:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1
    return fruit_count
fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
print(count_fruits(fruits))

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
# print(count_fruits(fruits))