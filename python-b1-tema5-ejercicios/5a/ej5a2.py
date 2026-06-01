"""
Enunciado:
Implementa una jerarquía de clases para representar
animales que pueden emitir sonidos. Existe una clase abstracta "Animal"
que define un método abstracto "make_sound". También, implementa tres
clases concretas "Dog", "Cat" y "Duck" que heredan de la clase "Animal"
e implementan su propio método "make_sound" para representar el sonido
que cada animal emite.

Luego de implementar las clases debes crear una lista de animales
que incluya un perro, un gato y un pato, y se recorra la lista haciendo
que cada animal emita el sonido correspondiente usando la función
"make_sound" y se imprima el sonido que emite cada animal.

Clases:
    - Animal: Clase abstracta que representa la abstracción de un animal y
    define el método abstracto "make_sound".
    - Dog: Clase que hereda de "Animal" y representa un perro, define su
    propio método "make_sound" que devuelve "Woof".
    - Cat: Clase que hereda de "Animal" y representa un gato, define su
    propio método "make_sound" que devuelve "Meow"
    - Duck: Clase que hereda de "Animal" y representa un pato, define su
    propio método "make_sound" que devuelve "Quack"

Ejemplo:
    Entrada:
        animals = [Dog(), Cat(), Duck()]
        for animal in animals:
            print(f'{animal.make_sound()}')

    Salida:
        Woof
        Meow
        Quack

Enunciat:
Implementa una jerarquia de classes per representar
animals que poden emetre sons. Hi ha una classe abstracta "Animal"
que defineix un mètode abstracte "make_sound". També, implementa tres
classes concretes "Dog", "Cat" i "Duck" que hereten de la classe "Animal"
i implementen el seu propi mètode "make_sound" per representar el so
que cada animal emet.

Després d'implementar les classes heu de crear una llista d'animals
que inclogui un gos, un gat i un ànec, i es recorri la llista fent
que cada animal emeti el so corresponent usant la funció
"make_sound" i s'imprimeix el so que emet cada animal.

Classes:
     - Animal: Classe abstracta que representa l'abstracció d'un animal i
     defineix el mètode abstracte "make_sound".
     - Dog: Classe que hereta de "Animal" i representa un gos, defineix el seu
     propi mètode "make_sound" que torna "Woof".
     - Cat: Classe que hereta de "Animal" i representa un gat, defineix la seva
     propi mètode "make_sound" que torna "Meow"
     - Duck: Classe que hereta de "Animal" i representa un ànec, defineix el seu
     propi mètode "make_sound" que torna "Quack"

Exemple:
     Entrada:
         animals = [Dog(), Cat(), Duck()]
         for animal in animals:
             print(f'{animal.make_sound()}')

     Sortida:
         Woof
         Meow
         Quack
"""

from abc import ABC, abstractmethod

# Corret and overwrite class Animal here 
class Animal(ABC):
    pass

# Corret and overwrite class Dog(Animal) here
class Dog():
    pass


# Corret and overwrite class class Cat(Animal) here
class Cat():
    pass

# Corret and overwrite class Duck(Animal) here
class Duck():
    pass

# Create a list of animals here
animals = []
# Print animals sounds
for animal in animals:
    # Write your code here
    pass
