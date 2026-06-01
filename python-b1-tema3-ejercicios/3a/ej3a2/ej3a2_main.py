"""
Enunciado:
Implementar un paquete llamado 'ej3a2_math_package' que tiene dos módulos:
'arithmetic.py' y 'geometry.py', con la siguiente estructura:

    ej3a2_math_package/
        __init__.py
        arithmetic.py
        geometry.py

El módulo 'arithmetic.py' contendrá dos funciones: 'power(base, exponent)',
'square_root(number)'.
El módulo 'geometry.py' contendrá funciones como: 'square_area(side_length)',
'triangle_area(base_length, height)', 'circle_area(radius)' y
'rectangle_area(base_length, height)'.

El paquete 'ej3a2_math_package' se debe importar desde el script 'ej3a2_main.py'

Ejemplo:
    Entrada:
    arithmetic.power(3, 2)
    arithmetic.square_root(16)
    geometry.square_area(5)
    geometry.rectangle_area(3, 5)
    geometry.triangle_area(3, 5)
    geometry.circle_area(5)

    Salida:
    125
    4.0
    25
    15
    7.5
    31.4159265359

Enunciat:

Implementar un paquet anomenat 'ej3a2_math_package' que té dos mòduls:
'arithmetic.py' i 'geometry.py', amb la següent estructura:

     ej3a2_math_package/
         __init__.py
         arithmetic.py
         geometry.py

El mòdul 'arithmetic.py' contindrà dues funcions: 'power(base, exponent)',
'square_root(number)'.
El mòdul 'geometry.py' contindrà funcions com: 'square_area(side_length)',
'triangle_area(base_length, height)', 'circle_area(radius)' i
'rectangle_area(base_length, height)'.

El paquet 'ej3a2_math_package' s'ha d'importar des de l'script 'ej3a2_main.py'

Exemple:
     Entrada:
     arithmetic.power(3, 2)
     arithmetic.square_root(16)
     geometry.square_area(5)
     geometry.rectangle_area(3, 5)
     geometry.triangle_area(3, 5)
     geometry.circle_area(5)

     Sortida:
     125
     4.0
     25
     15
     7.5
     31.4159265359
"""
# archivo ej3a2_main.py

from ej3a2_math_package import geometry, arithmetic

# Arithmetic operations
print(arithmetic.power(5, 3))
print(arithmetic.square_root(16))

# Geometric operations
square_area_result = geometry.square_area(5)
rectangle_area_result = geometry.rectangle_area(3, 5)
triangle_area_result = geometry.triangle_area(3, 5)
circle_area_result = geometry.circle_area(5)

print(square_area_result)
print(rectangle_area_result)
print(triangle_area_result)
print(circle_area_result)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(square_area_result)
#print(rectangle_area_result)
#print(triangle_area_result)
#print(circle_area_result)
