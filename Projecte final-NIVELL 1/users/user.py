"""
Mòdul user.py
Defineix la classe abstracta User i les classes concretes Cashier i Customer.
"""

from abc import ABC, abstractmethod


class User(ABC):
    """Classe abstracta que representa un usuari del sistema."""

    def __init__(self, dni: str, nom: str, edat: int):
        self.dni = str(dni)
        self.nom = nom
        self.edat = int(edat)

    @abstractmethod
    def describe(self) -> str:
        """Retorna una descripció de l'usuari."""
        pass

    def __str__(self) -> str:
        return self.describe()


class Cashier(User):
    """Classe que representa un caixer."""

    def __init__(self, dni: str, nom: str, edat: int, horari: str, sou: float):
        super().__init__(dni, nom, edat)
        self.horari = horari
        self.sou = float(sou)

    def describe(self) -> str:
        return (
            f"Caixer - Nom: {self.nom}, DNI: {self.dni}, Edat: {self.edat}, "
            f"Horari: {self.horari}, Salari: {self.sou}."
        )


class Customer(User):
    """Classe que representa un client."""

    def __init__(self, dni: str, nom: str, edat: int, email: str, codi_postal: str):
        super().__init__(dni, nom, edat)
        self.email = email
        self.codi_postal = str(codi_postal)

    def describe(self) -> str:
        return (
            f"Client - Nom: {self.nom}, DNI: {self.dni}, Edat: {self.edat}, "
            f"Correu: {self.email}, Codi Postal: {self.codi_postal}."
        )
