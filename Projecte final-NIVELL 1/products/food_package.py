"""
Mòdul food_package.py
Conté la classe abstracta FoodPackage i les implementacions concretes
per als diferents tipus d'embolcall del menjar ràpid.
"""

from abc import ABC, abstractmethod


class FoodPackage(ABC):
    """Classe abstracta que defineix un embolcall de menjar."""

    @abstractmethod
    def pack(self) -> str:
        """Retorna el tipus d'embolcall."""
        pass

    @abstractmethod
    def material(self) -> str:
        """Retorna el material de l'embolcall."""
        pass


class Wrapping(FoodPackage):
    """Embolcall per a hamburgueses."""

    def pack(self) -> str:
        return "Paper d'alumini per a menjar"

    def material(self) -> str:
        return "Alumini"


class Bottle(FoodPackage):
    """Ampolla per a refrescos."""

    def pack(self) -> str:
        return "Ampolla"

    def material(self) -> str:
        return "Plàstic"


class Glass(FoodPackage):
    """Got per a begudes."""

    def pack(self) -> str:
        return "Got"

    def material(self) -> str:
        return "Cartró"


class Box(FoodPackage):
    """Caixa per a menús infantils."""

    def pack(self) -> str:
        return "Caixa"

    def material(self) -> str:
        return "Cartró"
