"""
Mòdul product.py
Defineix la classe abstracta Product i les classes concretes de productes.
"""

from abc import ABC, abstractmethod
from products.food_package import FoodPackage, Wrapping, Bottle, Glass, Box


class Product(ABC):
    """Classe abstracta que representa un producte del restaurant."""

    def __init__(self, id: str, nom: str, preu: float):
        self.id = id
        self.name = nom
        self.price = float(preu)

    @abstractmethod
    def type(self) -> str:
        """Retorna el tipus de producte."""
        pass

    @abstractmethod
    def foodPackage(self) -> FoodPackage:
        """Retorna l'embolcall associat al producte."""
        pass

    def describe(self) -> str:
        """Retorna la descripció completa del producte."""
        package = self.foodPackage()
        return (
            f"Producte - Tipus: {self.type()}, Nom: {self.name}, "
            f"Id: {self.id}, Preu: {self.price}, "
            f"Embolcall: {package.pack()}, Material: {package.material()}."
        )

    def __str__(self) -> str:
        return self.describe()


class Hamburger(Product):
    """Producte de tipus hamburguesa."""

    def __init__(self, id: str, nom: str, preu: float):
        super().__init__(id, nom, preu)

    def type(self) -> str:
        return "Hamburguesa"

    def foodPackage(self) -> FoodPackage:
        return Wrapping()


class Soda(Product):
    """Producte de tipus refresc."""

    def __init__(self, id: str, nom: str, preu: float):
        super().__init__(id, nom, preu)

    def type(self) -> str:
        return "Refresc"

    def foodPackage(self) -> FoodPackage:
        return Bottle()


class Drink(Product):
    """Producte de tipus beguda."""

    def __init__(self, id: str, nom: str, preu: float):
        super().__init__(id, nom, preu)

    def type(self) -> str:
        return "Beguda"

    def foodPackage(self) -> FoodPackage:
        return Glass()


class HappyMeal(Product):
    """Producte de tipus menú infantil."""

    def __init__(self, id: str, nom: str, preu: float):
        super().__init__(id, nom, preu)

    def type(self) -> str:
        return "Happy Meal"

    def foodPackage(self) -> FoodPackage:
        return Box()
