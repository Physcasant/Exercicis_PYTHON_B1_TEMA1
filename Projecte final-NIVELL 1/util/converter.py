"""
Mòdul converter.py
Conté convertidors que transformen les files dels DataFrame en objectes.
"""

from abc import ABC, abstractmethod
# Importem el mòdul intern de Python anomenat builtins, que conté les funcions bàsiques que Python
# te disponibles sempre, com ara: 
# print(), len(), str(), float(),...
import builtins

from products.product import Hamburger, Soda, Drink, HappyMeal
from users.user import Cashier, Customer


class Converter(ABC):
    """Classe abstracta per convertir un DataFrame en una llista d'objectes."""

    @abstractmethod
    def convert(self, dataFrame, *args) -> list:
        """Converteix les files d'un DataFrame en objectes."""
        pass

    def print(self, list) -> None:
        """Imprimeix la informació de tots els objectes de la llista."""
        for element in list:
            builtins.print(element)


class CashierConverter(Converter):
    """Converteix files del fitxer cashiers.csv en objectes Cashier."""

    def convert(self, dataFrame, *args) -> list:
        # Creem una llista buida on guardarem els objectes Cashier que anirem creant a partir
        # de les files del DataFrame.
        cashiers = [] 
        # El mètode dataframe.iterrows() permet recòrrer aquesta taula fila per fila
        # Però cada volta del bucle retorna dues coses: index, row
        # És a dir: for index, row in dataframe.iterrows():
        # La primera variable és l'index de la fila, que és un número que comença a 0 i va incrementant per cada fila.
        # La segona variable és un objecte que representa la fila actual, i que té les columnes com a atributs. 
        # Per què _? Aquest simbol indica que no ens interessa l'index de la fila, només el contingut de la fila (row). 
        # És una convenció en Python per indicar que aquesta variable no s'utilitzarà.:
        for _, row in dataFrame.iterrows():
            cashier = Cashier(
                dni=row["dni"],
                nom=row["nom"],
                edat=row["edat"],
                horari=row["horari"],
                sou=row["sou"],
            )
            cashiers.append(cashier)
        return cashiers


class CustomerConverter(Converter):
    """Converteix files del fitxer customers.csv en objectes Customer."""

    def convert(self, dataFrame, *args) -> list:
        customers = []
        for _, row in dataFrame.iterrows():
            customer = Customer(
                dni=row["dni"],
                nom=row["nom"],
                edat=row["edat"],
                email=row["email"],
                codi_postal=row["codi_postal"],
            )
            customers.append(customer)
        return customers

"""
Les següents classes converteixen les files dels DataFrame en objectes de tipus Hamburger, Soda, Drink i HappyMeal.
Cada classe té un mètode convert() que recorre les files del DataFrame i crea un objecte per cada fila, 
utilitzant les dades de les columnes id, nom i preu. 
Aquests objectes es guarden en una llista que es retorna al final del mètode.
"""
class HamburgerConverter(Converter):
    """Converteix files del fitxer hamburgers.csv en objectes Hamburger."""

    def convert(self, dataFrame, *args) -> list:
        products = []
        for _, row in dataFrame.iterrows():
            hamburger = Hamburger(
                row["id"],
                row["nom"],
                float(row["preu"].replace(",", "."))
            )

            products.append(hamburger)
        return products

class SodaConverter(Converter):
    """Converteix files del fitxer sodas.csv en objectes Soda."""

    def convert(self, dataFrame, *args) -> list:
        products = []
        for _, row in dataFrame.iterrows():
            soda = Soda(
                row["id"],
                row["nom"],
                float(row["preu"].replace(",", "."))
            )

            products.append(soda)
        return products

class DrinkConverter(Converter):
    """Converteix files del fitxer drinks.csv en objectes Drink."""

    def convert(self, dataFrame, *args) -> list:
        products = []
        for _, row in dataFrame.iterrows():
            drink = Drink(
                row["id"],
                row["nom"],
                float(row["preu"].replace(",", "."))
            )
            products.append(drink)
        return products

class HappyMealConverter(Converter):
    """Converteix files del fitxer happyMeal.csv en objectes HappyMeal."""

    def convert(self, dataFrame, *args) -> list:
        products = []
        for _, row in dataFrame.iterrows():
            happy_meal = HappyMeal(
                row["id"],
                row["nom"],
                float(row["preu"].replace(",", "."))
            )

            products.append(happy_meal)
        return products

class HappyMealConverter(Converter):
    """Converteix files del fitxer happyMeal.csv en objectes HappyMeal."""

    def convert(self, dataFrame, *args) -> list:
        products = []
        for _, row in dataFrame.iterrows():
            products.append(
                HappyMeal(
                    row["id"],
                    row["nom"],
                    float(row["preu"].replace(",", "."))
                )
            )
        return products
