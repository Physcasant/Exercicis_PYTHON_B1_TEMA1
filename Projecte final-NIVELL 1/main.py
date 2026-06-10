"""
Punt d'entrada de l'aplicació.
Executa aquest fitxer amb: python main.py
"""

from prepare_order import PrepareOrder

if __name__ == "__main__":
    app = PrepareOrder()
    app.run()
