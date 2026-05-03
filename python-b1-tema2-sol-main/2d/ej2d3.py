from typing import List

"""
Enunciado:
Corrige la función 'division_list' que realiza una división de una lista
de número enteros dividido para un número escalar.

Para corregir los errores se puede cambiar los valores de la lista
'list_numbers' y el valor del número escalar 'scalar_number'.

En la función 'division_list' se debe verificar que el contenido de
la lista sea de tipo 'int' o 'float', caso contrario, mostrar una
excepción TypeError(f"Value {number_in_list} is not numeric.").

Parámetros:
    list_numbers (list): Lista de números.
    number (int): Número entero.
    
Ejemplos:
    Entrada:
        list_numbers = [1.5, 2.5, 9.2, 0, 22]
        scalar_number = 4.0
        
    Salida:
        [0.375, 0.625, 2.3, 0.0, 5.5]


Enunciat:
Corregeix la funció 'division_list' que fa una divisió d'una llista
de nombre enters dividit per a un nombre escalar.

Per corregir els errors es poden canviar els valors de la llista
'list_numbers' i el valor del número escalar 'scalar_number'.

A la funció 'division_list' s'ha de verificar que el contingut de
la llista sigui de tipus 'int' o 'float', en cas contrari, mostra una
excepció TypeError(f"Value {number_in_list} is not numeric.").

Paràmetres:
     list_numbers (list): Llista de números.
     number (int): Número sencer.
    
Exemples:
     Entrada:
         list_numbers = [1.5, 2.5, 9.2, 0, 22]
         scalar_number = 4.0
        
     Sortida:
         [0.375, 0.625, 2.3, 0.0, 5.5]

"""


def division_list(list_numbers: List, number: int) -> List[float]:
    result = []
    for number_in_list in list_numbers:
        if not isinstance(number_in_list, (int, float)):
            raise TypeError(f"Value {number_in_list} is not numeric.")
        result.append(number_in_list / number)
    return result


list_numbers = [1.5, 2.5, 9.2, 0, 22]
scalar_number = 4.0

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(division_list(list_numbers, scalar_number))
