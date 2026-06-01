"""
Enunciado:
Crea una función llamada 'add_elapsed_time(dictionary, key, value)' que
almacenará el último registro del tiempo de carrera de los atletas.
La fucnión recibe como parámetros un diccionario llamado 'dictionary',
una clave llamada 'key' y un valor llamado 'value'. La función debe
ser capaz de agregar el nuevo elemento al diccionario utilizando la
clave y el valor proporcionados.

Si la clave ya existe en el diccionario, se debe reemplazar el valor
anterior por el nuevo valor. La función debe retornar el diccionario
actualizado.

Parámetros:
    dictionary = Un diccionario al que se debe agregar un nuevo elemento.
    key = Una cadena que representa la clave del nuevo elemento a agregar.
    value = El valor del nuevo elemento a agregar.

Ejemplo:
    Entrada:
    my_dict = {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}
    mi_diccionario = add_elapsed_time(my_dict, 'Juan', 8.6)

    Salida:
    {'Juan': 8.6, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}

Enunciat:

"""


def add_elapsed_time(dictionary, key, value):
    dictionary[key]=value
    return dictionary
my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
my_dict = add_elapsed_time(my_dict, "Juan", 8.8)
my_dict = add_elapsed_time(my_dict, "Alice", 7.3)
print(my_dict)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
# my_dict = add_elapsed_time(my_dict, "Juan", 8.8)
# my_dict = add_elapsed_time(my_dict, "Alice", 7.3)
# print(my_dict)
