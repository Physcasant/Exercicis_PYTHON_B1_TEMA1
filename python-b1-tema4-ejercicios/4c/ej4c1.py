"""
Enunciado:
Se necesita implementar las siguientes clases:

Clase "Person": Representa a una persona y cuenta con un método 'describe(self)'
que devuelve una descripción de la persona.
Clase "Student": Representa a un estudiante y tiene como parámetro la clase
"Person". Además, cuenta con un método "describe" que extiende la descripción
de la persona y agrega información sobre la carrera que estudia.

El método 'describe' de la clase "Person" retornará el siguiente formato:
f"{self.name} is {self.age} years old."

El método 'describe' de la clase "Student" retornará lo mismo que la clase 
"Person" y, además:
f"{description} Studies {self.major}."

Se requiere crear dos objetos, "person_1" y "student_1", a partir de las
clases "Person" y "Student", respectivamente. Se debe acceder a los
métodos 'describe' de los objetos y mostrar la descripción correspondiente.

Parámetros:
    Para la clase Person:
        - name: String con el nombre de la persona/objeto.
        - age: un número entero, que representa la edad de la persona.
    
    Para la clase Student:
        - name: String con el nombre del estudiante.
        - age: Un número entero, que representa la edad del estudiante.
        - major: String que indica la carrea que estudia.
        
Ejemplo:
    Entrada:
        person_1 = Person("Juan", 30)
        person_1.describe()
        
        student_1 = Student("Ana", 25, "Systems Engineering")
        student_1.describe()
    Salida:
        Juan is 30 years old.
        Ana is 25 years old. Studies Systems Engineering.

Enunciat:
Es necessita implementar les classes següents:

Classe "Person": Representa una persona i compta amb un mètode 'descriu(self)'
que torna una descripció de la persona.
Classe "Student": Representa un estudiant i té com a paràmetre la classe
"Person". A més, compta amb un mètode "descriu" que estén la descripció
de la persona i afegeix informació sobre la carrera que estudia.

Cal crear dos objectes, "person_1" i "student_1", a partir de les
classes "Person" i "Student", respectivament. Cal accedir als
mètodes 'descriu' dels objectes i mostrar la descripció corresponent.

El mètode 'descriu' de la classe "Person" retornarà el següent format:
f"{self.name} is {self.age} years old."

El mètode 'descriu' de la classe "Student" retornarà el mateix que la classe 
"Person" i, a més:
f"{description} Studies {self.major}."    

Paràmetres:
     Per a la classe Person:
         - name: String amb el nom de la persona/objecte.
         - age: un nombre enter que representa l'edat de la persona.
    
     Per a la classe Student:
         - name: String amb el nom de l'estudiant.
         - age: Un nombre enter que representa l'edat de l'estudiant.
         - major: String que indica la carrea que estudia.
        
Exemple:
     Entrada:
         person_1 = Person("Joan", 30)
         person_1.describe()
        
         student_1 = Student("Ana", 25, "Systems Engineering")
         student_1.describe()
     Sortida:
         Juan is 30 years old.
         Ana is 25 years old. Studies Systems Engineering.

"""

# Class that represents a person
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Method that returns the description of the person
    def describe(self):
        return f"{self.name} is {self.age} years old."

# Class that represents a student
class Student(Person):
    # Constructor
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    # Method that returns the description of the student
    def describe(self):
        description = super().describe()
        return f"{description} Studies {self.major}."

person_1 = Person("Juan", 30)
student_1 = Student("Ana", 25, "Systems Engineering")

print(person_1.describe())  # Juan is 30 years old.
print(student_1.describe())  # Ana is 25 years old. Studies Systems Engineering.


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# Access to object methods
#print(person_1.describe())  # Juan is 30 years old.
#print(student_1.describe())  # Ana is 25 years old. Studies Systems Engineering.
