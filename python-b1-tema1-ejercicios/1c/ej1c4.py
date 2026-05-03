""" 
Enunciado:
Escribe una función llamada is_palindrome(word) que reciba como parámetro
una cadena word y verifique si es un palíndromo utilizando recursión.
La función debe devolver True si la cadena es un palíndromo y False en
caso contrario.

Parámetros:
    word (str): una cadena de caracteres.

Ejemplo:
    Entrada:
    word = "racecar"
    print(is_palindrome(word))

    Salida:
    True



Enunciat:

Enunciat:
Escriu una funció anomenada is_palindrome(word) que rebi com a paràmetre
una cadena word i verifiqui si és un palíndrom utilitzant recursió.
La funció ha de tornar True si la cadena és un palíndrom i False a
cas contrari.

Paràmetres:
     word (str): una cadena de caràcters.

Exemple:
     Entrada:
     word = "racecar"
     print(is_palindrome(word))

     Sortida:
     True

"""


def is_palindrome(word):
    # Cas base
    if len(word) <= 1:
        return True
    # Si el primer i l'últim són diferents → no és palíndrom
    if word[0] != word[-1]:
        return False
    # Cas recursiu: comprovem la part del mig
    return is_palindrome(word[1:-1])

    pass
word = "level"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
word = "juan"
print(f"Is '{word}' word palindrome?", is_palindrome(word))

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# word = "level"
# print(f"Is '{word}' word palindrome?", is_palindrome(word))
#
# word = "juan"
# print(f"Is '{word}' word palindrome?", is_palindrome(word))
