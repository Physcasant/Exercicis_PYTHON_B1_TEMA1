"""
Enunciado:
Implementa una función 'convert_kg_to_lb' que reciba como parámetro un valor
numérico llamado 'kg' que corresponde al valor que se desea convertir de 
kilogramos a libras.

El valor introducido no puede ser menor o igual que '0', si se introduce un
valor menor o igual a '0' se debe crear un ValueError. El valor introducido
debe ser de type numérico de manera que si se introduce otro valor que no sea
numérico se deberá crear un TypeError.

Parámetros:
kg = Valor numérico que representa a los kilogramos para convertir a libras.

Ejemplo:
    Entrada: 50
    Salida: 110.23

    Entrada: 0
    Salida: ValueError

    Entrada: 'abc'
    Salida: TypeError

Enunciat:
Implementa una funció 'convert_kg_to_lb' que rebi com a paràmetre un valor
numèric anomenat 'kg' que correspon al valor que es vol convertir de
quilograms a lliures.

El valor introduït no pot ser menor o igual que '0' si s'introdueix un valor
menor o igual a '0' s'ha de crear un ValueError. El valor introduït ha de ser de
tipus numèric de manera que si s'introdueix un altre valor que no sigui numèric s'haurà
de crear un TypeError.

Paràmetres:
kg = Valor numèric que representa els quilograms per convertir lliures.

Exemple:
     Entrada: 50
     Sortida: 110.23

     Entrada: 0
     Sortida: ValueError

     Entrada: 'abc'
     Sortida: TypeError

"""


def kg_to_lb(kg):
    try:
        if kg <= 0:
            raise ValueError("Must be greater than 0.")
        else:
            lb = kg * 2.20462
            return round(lb, 2)
    except TypeError:
        raise TypeError("Must be a number.")


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(kg_to_lb(50))
