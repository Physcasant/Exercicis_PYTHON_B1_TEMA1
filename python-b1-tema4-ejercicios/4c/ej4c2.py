"""
Enunciado:
Se pide crear una interfaz "Vehicles" que tenga un método abstracto "drive".
Además, se deben crear las clases concretas "Car" y "Bicycle" que implementen
la interfaz "Vehicles".

El método "drive" debe imprimir "Driving a car" para la clase "Car" y "Riding
a bicycle" para la clase "Bicycle".

Parámetros:
    La clase Car y Bicycle no reciben parámetros.
        
Ejemplo:
    Entrada:
        car = Car()
        print(car.drive())

        bicycle = Bicycle()
        print(bicycle.drive())
    Salida:
        Driving a car
        Riding a bicycle


Enunciat:
Es demana crear una interfície "Vehicles" que tingui un mètode abstracte "drive".
A més, cal crear les classes concretes "Car" i "Bicycle" que implementin
la interfície "Vehicles".

El mètode "drive" ha d'imprimir "Driving a car" per a la classe "Car" i "Riding"
a bicycle" per a la classe "Bicycle".

Paràmetres:
     La classe Car i Bicycle no reben paràmetres.
        
Exemple:
     Entrada:
         car = Car()
         print(car.drive())

         bicycle = Bicycle()
         print(bicycle.drive())
     Sortida:
         Driving a car
         Riding a bicycle
"""

from abc import ABC, abstractmethod

# Write abstract class Vehicles here 
class Vehicles(ABC):
    @abstractmethod
    def drive(self):
        pass
# Correct and overwrite class Car(Vehicles) here 
# Class Car inherits from Vehicles
class Car(Vehicles):
    def drive(self):
        return "The car is driving."
        pass
# Correct and overwrite class Bicycle(Vehicles) here 
# Class Bicycle inherits from Vehicles
class Bicycle(Vehicles):
    def drive(self):
        return "The bicycle is driving."
        pass
car = Car()
print(car.drive())
bicycle = Bicycle()
print(bicycle.drive())


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# car = Car()
# print(car.drive())
# bicycle = Bicycle()
# print(bicycle.drive())
