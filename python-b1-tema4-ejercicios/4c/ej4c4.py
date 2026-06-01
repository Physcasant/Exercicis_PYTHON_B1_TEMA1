"""
Enunciado:
Se pide crear una interfaz "Animal" que tenga un método abstracto "talk".
Además, se deben crear las clases concretas "Dog", "Cat" y "Parrot" que
implementen la interfaz "Animal".

El método "talk" debe imprimir "¡Guau!" para la clase "Dog", "¡Meow!"
para la clase "Cat" y "¡Whistle!" para la clase "Parrot"

Parámetros:
    La clase Animal:
        - name: String que representa el nombre del animal.
        
Ejemplo:
    Entrada:
        dog = Dog("Fido")
        dog.talk()

        cat = Cat("Fido")
        cat.talk()
        
        parrot = Parrot("Polly")
        parrot.name
    Salida:
        "¡Guau!"
        "¡Meow!"
        "Polly"


Enunciat:
Es demana crear una interfície "Animal" que tingui un mètode abstracte "talk".
A més, cal crear les classes concretes "Dog", "Cat" i "Parrot" que
implementin la interfície "Animal".

El mètode "talk" ha d'imprimir "Guau!" per a la classe "Dog", "Meow!"
per a la classe "Cat" i "Whistle!" per a la classe "Parrot"

Paràmetres:
     La classe Animal:
         - name: String que representa el nom de lanimal.
        
Exemple:
     Entrada:
         dog = Dog("Fido")
         dog.talk()

         cat = Cat("Fido")
         cat.talk()
        
         parrot = Parrot("Polly")
         parrot.name
     Sortida:
         "Guau!"
         "Meow!"
         "Polly"        
"""
from abc import ABC, abstractmethod
# Abstract class Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name
        @abstractmethod
        def talk(self):
            pass
# Correct and overwrite class Dog(Animal) here 
class Dog(Animal):
    def talk(self):
        return "Guau!"
# Corret and overwrite class Cat(Animal) here 
class Cat(Animal): 
    def talk(self):
        return "Meow!"
# Corret and overwrite class Parrot(Animal) here 
class Parrot(Animal):
    def talk(self):
        return "Whistle!"
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
def test_code():
	animals = [Dog("Fido"), Cat("Felix"), Parrot("Polly")]	
	for animal in animals:
	    print(f"{animal.name} dice {animal.talk()}")
test_code()