"""
Mòdul order.py
Conté la classe Order, que representa una comanda en procés.
"""

from products.product import Product
from users.user import Cashier, Customer


class Order:
    """Classe que representa una comanda feta per un client i atesa per un caixer."""

    def __init__(self, cashier: Cashier, customer: Customer):
        self.cashier = cashier
        self.customer = customer
        self.products = []

    def add(self, product: Product) -> None:
        """Afegeix un producte a la comanda."""
        self.products.append(product)

    def calculateTotal(self) -> float:
        """Calcula el preu total de la comanda."""
        total = 0
        for product in self.products:
            total += product.price
        return round(total, 2)

    def show(self) -> None:
        """Mostra per pantalla la informació completa de la comanda."""
        print(f"Hola: {self.customer}")
        print(f"Atès per: {self.cashier}")

        for index, product in enumerate(self.products, start=1):
            print(f"Producte {index}: {product}")

        print(f"Preu total: {self.calculateTotal()}")
