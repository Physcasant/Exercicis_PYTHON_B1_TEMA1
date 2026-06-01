"""
Enunciado:

Implementa la clase "Shape", que tiene el método 'get_sides', que devuelve una
lista con los lados de la forma.

Luego, implementa la clase "Triangle", que hereda de "Shape" y tiene los métodos
'area' y '__init__', donde el método 'area' devuelve el área del triángulo y '__init__'
inicializa los atributos base, altura y lados de la forma.

Por último, implementa la clase "Rectangle", que hereda de "Shape" y tiene los
métodos 'area' y '__init__', donde el método 'area' devuelve el área del rectángulo
y '__init__' inicializa los atributos largo, ancho y lados de la forma.

Parámetros:
    Para la clase Triangle:
        - sides: una lista de tres enteros, que representa los lados del
        triángulo.
        - base: un número entero, que representa la base del triángulo.
        - height: un número entero, que representa la altura del triángulo.
    
    Para la clase Rectangle:
        - sides: una lista de cuatro enteros, que representa los lados del
        rectángulo.
        - length: un número entero, que representa el largo del rectángulo.
        - width: un número entero, que representa el ancho del rectángulo.
        
Ejemplo:
    Entrada:
        triangle = Triangle([3, 4, 5], 4, 3)
        triangle.area()
        
        rectangle = Rectangle([5, 5, 2, 2], length=5, width=2)
        rectangle.get_area()
    Salida:
        6.0
        10


Enunciat:

Implementa la classe "Shape", que té el mètode 'get_sides', que torna una
llista amb els costats de la forma.

Després, implementa la classe "Triangle", que hereta de "Shape" i té els mètodes
'area' i '__init__', on el mètode 'area' torna l'àrea del triangle i '__init__'
inicialitza els atributs base, altura i costats de la forma.

Finalment, implementa la classe "Rectangle", que hereta de "Shape" i té els
mètodes 'area' i '__init__', on el mètode 'area' torna l'àrea del rectangle
i '__init__' inicialitza els atributs longitud, ample i costats de la forma.

Paràmetres:
     Per a la classe Triangle:
         - sides: una llista de tres enters, que representa els costats del
         triangle.
         - base: un nombre enter, que representa la base del triangle.
         - height: un nombre enter, que representa l'alçada del triangle.
    
     Per a la classe Rectangle:
         - sides: una llista de quatre enters, que representa els costats del
         rectangle.
         - length: un nombre enter, que representa el llarg del rectangle.
         - width: un nombre enter, que representa l'amplada del rectangle.
        
Exemple:
     Entrada:
         triangle = Triangle([3, 4, 5], 4, 3)
         triangle.area()
        
         rectangle = Rectangle([5, 5, 2, 2], length=5, width=2)
         rectangle.get_area()
     Sortida:
         6.0
         10        
"""

# Corret and overwrite class Dog(Shape) here
class Shape:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides
    
class Triangle(Shape):
    def __init__(self, sides, base, height):  
        super().__init__(sides)
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2

class Rectangle(Shape):
    def __init__(self, sides, length, width):        
        super().__init__(sides)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

triangle = Triangle([3, 4, 5], base=4, height=3)
print(triangle.get_area()) # Output: 6.0
rectangle = Rectangle([5, 5, 2, 2], length=5, width=2)
print(rectangle.get_area()) # Output: 10
print (rectangle.get_sides()) # shows sides of the rectangle


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# # Create a triangle with base 4 and height 3
#triangle = Triangle([3, 4, 5], base=4, height=3)
# # Get the area of the triangle
#print(triangle.get_area()) # Output: 6.0
#print (triangle.get_sides()) # shows sides of the triangle

# # Create a rectangle with length 5 and width 2
#rectangle = Rectangle([5, 5, 2, 2], length=5, width=2)
# # Get the area of the rectangle
#print(rectangle.get_area()) # Output: 10
#print (rectangle.get_sides()) # shows sides of the rectangle
