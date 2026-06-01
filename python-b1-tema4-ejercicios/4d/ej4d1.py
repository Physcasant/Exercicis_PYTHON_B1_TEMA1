"""
Enunciado:
Realizando la entrada por consola de los datos, implementa la función 'sum'
que solicite la entrada de dos números con 'input' y devuelva la suma de los
números.

Parámetro:
No recibe ningún parámetro debido a que dentro de la función se solicita la
entrada de los números.

Ejemplo:
    Entrada:
        "Insert the first number: " 8
        "Insert the second number: " 3

    Salida:
        "Result: " 11

Enunciat:
Realitzant l'entrada per consola de les dades, implementa la funció 'sum'
que sol·liciti l'entrada de dos números amb 'input' i torni la suma dels
números.

Paràmetre:5
No rep cap paràmetre pel fet que dins de la funció se sol·licita la
entrada dels números.

Exemple:
     Entrada:
         "Insert the first number: " 8
         "Insert the second number: " 3

     Sortida:
         "Result: " 11
"""

def sum_number():
    first_number = int(input("Insert the first number: "))
    second_number = int(input("Insert the second number: "))

    result = first_number + second_number

    print("Result:", result)


sum_number()


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# sum()
