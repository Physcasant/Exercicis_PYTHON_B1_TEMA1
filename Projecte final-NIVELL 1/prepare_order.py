"""
El mòdul prepare_order.py conté la classe PrepareOrder, que és la classe principal de l'aplicació. 
Aquesta classe coordina la lectura dels fitxers CSV, la conversió de les dades en objectes i 
la preparació d'una comanda.
El mètode run() és el punt d'entrada de l'aplicació, on es mostra un menú per seleccionar un caixer,
un client i els productes que volen comprar.
La idea és aquesta: CSV  →  DataFrame  →  Objectes Python  →  Comanda  →  Mostrar / guardar
És a dir:
1. Llegeix els fitxer CSV de la carpeta data/
2. Converteix les files dels CSV en objectrs: caixers, clients i productes.
3. Permet escollir un caixer i un client per preparar una comanda, demanant dades per teclat: DNI del caixer, DNI del client i identificadors del productes
4. Crea una comanda amb la classe Order
5. Afegeix productes a la comanda.
6. Mostra la informació de la comanda per pantalla.
7. Permet guardar la comanda en un fitxer CSV anomenat orders.csv, amb els camps: cashier_dni, customer_dni, sale_datetime i total.
"""

"""Imports del mòdul prepare_order.py"""

from datetime import datetime # Importa la classe datetime, que permet obtenir la data i hora actual.
from pathlib import Path # Importa Path, que serveix per treballar amb rutes de fitxers i carpetes d’una manera més neta i segura
import pandas as pd # Importa la llibreria pandas, que és una eina molt potent per treballar amb dades en format de taula (DataFrame). La utilitzarem per llegir i escriure fitxers CSV.
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="debug_prepare_order.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Importa la classe Order del mòdul orders/order.py, que representa una comanda en procés.
from orders.order import Order

# Importa la classe encarregada de llegir i escriure fitxers CSV. 
# Aquesta classe té dos mètodes: read() per llegir un fitxer CSV i retornar un DataFrame, i write() per escriure un DataFrame en un fitxer CSV.
from util.file_manager import CSVFileManager 
# Importa les classes encarregades de convertir les files dels DataFrame en objectes de tipus Cashier, 
# Customer, Hamburger, Soda, Drink i HappyMeal.
from util.converter import (
    CashierConverter,
    CustomerConverter,
    HamburgerConverter,
    SodaConverter,
    DrinkConverter,
    HappyMealConverter,
) 
"""
Classe principal que coordina el funcionament de l'aplicació: 
Integra la lectura dels CSV, la conversió a objectes i la preparació d'una comanda.
La seva funció és coordinar tot el procés: 
    1. carregar les dades dels fitxers CSV,
    2. mostrar dades
    3. buscar caixer
    4. buscar client
"""
class PrepareOrder:
    """
    Inicialitza les rutes i les llistes d'objectes.
    És el constructor de la classe PrepareOrder, que s'executa automàticament quan fem:
    app =PrepareOrder()
    """
    def __init__(self):
        # Aquesta línia obté la carpeta on es troba el fitxer prepare_order.py i la guarda a self.base_path. 
        # Això és útil perquè així podem construir rutes relatives a aquesta carpeta, 
        # independentment d'on s'executi el programa.
        # _file_ representa el fitxer actual (prepare_order.py), i .parent ens porta a la carpeta que el conté.
        # El projecte està en aquesta ruta: C:\Users\casan\OneDrive\Documents\CURSOS\PYTHON\UOC\B1\Projecte final-NIVELL 1
        # Llavors Path(__file__).parent ens porta a: C:\Users\casan\OneDrive\Documents\CURSOS\PYTHON\UOC\B1\Projecte final-NIVELL 1
        self.base_path = Path(__file__).parent 
        # Aquesta línia construeix la ruta a la carpeta data, que és on es troben els fitxers CSV.
        self.data_path = self.base_path / "data"
        # Aquestes 3 linies creen llistes buides on guardarem els objectes que anirem creant a partir de les dades dels CSV: caixers, clients i productes.
        # Desprès, quan s'executi load_data(), aquestes llistes s'ompliran amb els objectes corresponents.
        self.cashiers = []
        self.customers = []
        self.products = []

    """
    Aquest mètode és fonamental. És el que carrega totes les dades del projecte.
    El seu objectiu és passar d'això: fitxers CSV a això: llistes d'objectes Python (caixers, clients i productes).
    Per fer això, segueix aquests passos:
    1. Llegeix cada fitxer CSV: df_cashier= CSVFileManager(...).read(). Aquesta líniea fa tres coses: 
       a) crea una ruta cap al fitxer: self.data_path / "cashiers.csv"
       b) crea un objecte CSVFileManager amb aquesta ruta
       c) crida el mètodo read() per lleguir el fitxer
       El resultat es guarda a: i el converteix en un DataFrame
       El mateix es fa amb tots els altres CSV: customers.csv, hamburgers.csv, sodas.csv, drinks.csv i happyMeal.csv
    2. Conversió de caixers i clients: self.cashiers = CashierConverter().convert(df_cashiers) i self.customers = CustomerConverter().convert(df_customers)
       Aquesta línia també fa tres coses:
       a) crea un objecte CashierConverter
       b) crida el mètode convert() d'aquest objecte, passant-li el DataFrame que conté les dades dels caixers
       c) guarda el resultat a self.cashiers, que és una llista d'objectes Cashier
       El mateix es fa amb els clients, utilitzant CustomerConverter.
       En definitiva, aquesta part del codi converteix les dades dels CSV de caixers i clients en objectes Python que podem utilitzar a l'aplicació.
    3. Conversió de productes: per cada tipus de producte (Hamburger, Soda, Drink i HappyMeal), es fa el mateix procés:
       Aquí es creen quatre llistes diferents: hamburgers, sodas, drinks i happy_meals, on es guarden els objectes corresponents a cada tipus de producte.
       Desprès, aquestes quatre llistes es concatenen en una sola llista self.products= hamburgers + sodas + drinks + happy_meals, que conté tots els productes disponibles.
       És a dir, adjunta totes les llistes de productes en una sola llista. Així, self.products conté tots els objectes de tipus Hamburger, Soda, Drink i HappyMeal que s'han creat a partir dels CSV.
       Aquesta línia és molt útil perquè ens permet tenir tots els productes en una sola llista, facilitant la seva gestió a l'hora de preparar les comandes.
       Per exemple, quan volem buscar un producte pel seu identificador, només hem de buscar a self.products, en lloc de buscar a quatre llistes diferents.
    """
    def load_data(self) -> None:
        logger.debug("Iniciant la càrrega de dades CSV.")
        """Llegeix tots els fitxers CSV i converteix les files en objectes."""
        df_cashiers = CSVFileManager(self.data_path / "cashiers.csv").read()
        df_customers = CSVFileManager(self.data_path / "customers.csv").read()
        df_hamburgers = CSVFileManager(self.data_path / "hamburgers.csv").read()
        df_sodas = CSVFileManager(self.data_path / "sodas.csv").read()
        df_drinks = CSVFileManager(self.data_path / "drinks.csv").read()
        df_happy_meals = CSVFileManager(self.data_path / "happyMeal.csv").read()
 
        logger.debug(f"Columnes cashiers: {df_cashiers.columns.tolist()}")
        logger.debug(f"Columnes customers: {df_customers.columns.tolist()}")
        logger.debug(f"Columnes hamburgers: {df_hamburgers.columns.tolist()}")
        logger.debug(f"Columnes sodas: {df_sodas.columns.tolist()}")
        logger.debug(f"Columnes drinks: {df_drinks.columns.tolist()}")
        logger.debug(f"Columnes happyMeal: {df_happy_meals.columns.tolist()}")

        self.cashiers = CashierConverter().convert(df_cashiers)
        self.customers = CustomerConverter().convert(df_customers)

        hamburgers = HamburgerConverter().convert(df_hamburgers)
        sodas = SodaConverter().convert(df_sodas)
        drinks = DrinkConverter().convert(df_drinks)
        happy_meals = HappyMealConverter().convert(df_happy_meals)

        self.products = hamburgers + sodas + drinks + happy_meals

    """
    Mètode find_cashier_by_dni, find_customer_by_dni i find_product_by_id: 
    aquests mètodes són molt importants perquè ens permeten buscar un caixer, un client o un producte
    a partir d'un identificador únic (DNI per caixers i clients, id per productes).
    Cada mètode recorre la llista corresponent (self.cashiers, self.customers o self.products) i 
    compara el DNI o id de cada element amb el valor que s'ha passat com a paràmetre. 
    Si troba una coincidència, retorna l'objecte corresponent. 
    Si no troba cap coincidència, retorna None.
    Aquests mètodes són molt útils perquè ens permeten validar les dades que introdueix l'usuari. Per exemple, quan demanem el DNI del caixer, podem utilitzar find_cashier_by_dni per comprovar si existeix un caixer amb aquest DNI i obtenir la seva informació. 
    Si no existeix, podem mostrar un missatge d'error i demanar el DNI de nou.  
    """
    def find_cashier_by_dni(self, dni: str):
        """Busca un caixer pel seu DNI."""
        for cashier in self.cashiers:
            if cashier.dni == dni:
                return cashier
        return None

    def find_customer_by_dni(self, dni: str):
        """Busca un client pel seu DNI."""
        for customer in self.customers:
            if customer.dni == dni:
                return customer
        return None

    def find_product_by_id(self, product_id: str):
        """Busca un producte pel seu identificador."""
        for product in self.products:
            if product.id.upper() == product_id.upper():
                return product
        return None
    
    """
    Mètodes per mostrar dades:
    show_cashiers(), show_customers() i show_products(): aquests mètodes 
    mostren per pantalla la llista de caixers, clients i productes disponibles. 
    """
    def show_cashiers(self) -> None:
        """Mostra tots els caixers disponibles."""
        print("\nLlista de caixers:")
        CashierConverter().print(self.cashiers)

    def show_customers(self) -> None:
        """Mostra tots els clients disponibles."""
        print("\nLlista de clients:")
        CustomerConverter().print(self.customers)

    def show_products(self) -> None:
        """Mostra tots els productes disponibles."""
        print("\nLlista de productes:")
        for product in self.products:
            print(product)

    """ Mètodes per demanar dades a l'usuari:
    ask_cashier(), ask_customer() i add_products_to_order(): aquests mètodes
    demanen a l'usuari que introdueixi el DNI del caixer, el DNI del client i els identificadors dels productes que volen comprar. 
    Utilitzen els mètodes de cerca (find_cashier_by_dni, find_customer_by_dni i find_product_by_id) per validar les dades introduïdes i obtenir els objectes corresponents.
    ask_yes_no(): aquest mètode és un auxiliar que demana una resposta de sí/no i retorna True o False. S'utilitza per preguntar a l'usuari si vol afegir més productes o si vol desar la comanda.
    add_products_to_order(): aquest mètode permet escollir productes i afegir-los a la comanda.
    """ 
    def ask_cashier(self):
        """Demana el DNI del caixer fins que existeixi."""
        while True:
            dni = input("\nIntrodueix DNI del caixer: ").strip()
            cashier = self.find_cashier_by_dni(dni)
            if cashier is not None:
                print(cashier)
                return cashier
            print("No s'ha trobat cap caixer amb aquest DNI.")

    def ask_customer(self):
        """Demana el DNI del client fins que existeixi."""
        while True:
            dni = input("\nIntrodueix DNI del client: ").strip()
            customer = self.find_customer_by_dni(dni)
            if customer is not None:
                print(customer)
                return customer
            print("No s'ha trobat cap client amb aquest DNI.")

    def ask_yes_no(self, message: str) -> bool:
        """Demana una resposta de sí/no i retorna True o False."""
        while True:
            answer = input(message).strip().lower()
            if answer in ["si", "sí", "s", "yes", "y"]:
                return True
            if answer in ["no", "n"]:
                return False
            print("Resposta no vàlida. Escriu Sí o No.")

    """ Mètode add_products_to_order: aquest mètode permet escollir productes i afegir-los a la comanda.
    Rep com a paràmetre un objecte Order, que representa la comanda que s'està preparant.
    El seu funcionament és el següent:
    1. Entra en un bucle While True: que es repetirà fins que l'usuari decideixi no afegir més productes.
    2. Demana a l'usuari que introdueixi l'identificador del producte que vol afegir a la comanda.
       product_id = input("\nIntrodueix l'identificador del producte: ").strip()
    3. Utilitza el mètode find_product_by_id per buscar el producte corresponent a l'identificador introduït.
    4. Si no es troba cap producte amb aquest identificador, mostra un missatge d'error.
    5. Si es troba el producte, mostra la seva informació i l'afegeix a la comanda utilitzant el mètode add() de l'objecte Order.
    6. Després d'afegir el producte, pregunta a l'usuari si vol afegir un altre producte: add_more = self.ask_yes_no("Vols afegir un altre producte? Sí/No: ").
       Si la resposta és afirmativa, 
       el bucle continua i es torna a demanar un identificador de producte. Si la resposta és negativa, 
       el bucle finalitza (break) i es torna al menú principal.
   """
    def add_products_to_order(self, order: Order) -> None:
        """Permet escollir productes i afegir-los a la comanda."""
        while True:
            product_id = input("\nIntrodueix l'identificador del producte: ").strip()
            product = self.find_product_by_id(product_id)

            if product is None:
                print("No s'ha trobat cap producte amb aquest identificador.")
            else:
                print(product)
                order.add(product)

            add_more = self.ask_yes_no("Vols afegir un altre producte? Sí/No: ")
            if not add_more:
                break

    """
    Mètode save_order: aquest mètode s'encarrega d'exportar la comanda a un fitxer CSV anomenat orders.csv, amb els camps demanats: cashier_dni, customer_dni, sale_datetime i total.
    El seu funcionament és el següent:
    1. Defineix la ruta al fitxer orders.csv: orders_file = self.data_path / "orders.csv"
    2. Crea una nova fila amb la informació de la comanda que es vol guardar. 
       Aquesta fila és un DataFrame amb una sola fila, que conté els camps:
        - cashier_dni: el DNI del caixer que ha atès la comanda (order.cashier.dni)
        - customer_dni: el DNI del client que ha fet la comanda (order.customer.dni)
        - sale_datetime: la data i hora actual en format "YYYY-MM-DD HH:MM:SS" (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        - total: el preu total de la comanda (order.calculateTotal())
    3. Comprova si el fitxer orders.csv ja existeix: if orders_file.exists():
        - Si existeix, llegeix el contingut actual del fitxer en un DataFrame (old_data) i
          concatena aquest DataFrame amb la nova fila (new_row) utilitzant pd.concat(). 
          El resultat es guarda a data.
          El paràmetre ignore_index=True indica que s'ha d'ignorar l'índex dels DataFrames i
          crear un nou índex per al DataFrame concatenat. 
          És a dir, serveix per regenerar l'índex del DataFrame resultant,
          assignant un nou índex seqüencial que comença des de 0 i incrementa per cada fila. 
          Això és útil quan es vol evitar duplicats d'índex o quan no es necessita conservar 
          l'índex original dels DataFrames que s'estan concatenant.
        - Si no existeix, data és simplement la nova fila (new_row).
    4. Escriu el DataFrame data al fitxer orders.csv utilitzant CSVFileManager(self.data_path / "orders.csv").write(data).
    5. Mostra un missatge confirmant que la comanda s'ha desat correctament, indicant la ruta del fitxer on s'ha guardat la comanda.
    """
    def save_order(self, order: Order) -> None:
        logger.debug("Iniciant procés de desament de la comanda.")    
        """Exporta la comanda a data/orders.csv amb els camps demanats."""
        orders_file = self.data_path / "orders.csv"
        products_ids = []
        products_names = []
        products_details = []

        for product in order.products:
            product_id = product.id
            product_name = product.name
            product_price = product.price

            logger.debug(
                f"Producte afegit a orders.csv: "
                f"id={product_id}, name={product_name}, price={product_price}"
            )

            products_ids.append(product.id)
            products_names.append(product.name)
            products_details.append(
                f"{product_id} - {product_name} - {product_price} €"
            )
        new_row = pd.DataFrame([
            {
                "cashier_dni": order.cashier.dni,
                "customer_dni": order.customer.dni,
                "sale_datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),                
                "products_ids": " | ".join(products_ids),
                "products_names": " | ".join(products_names),
                "products_detail": " | ".join(products_details),
                "total": order.calculateTotal(),
            }
        ])

        logger.debug(f"Nova fila de comanda:\n{new_row}")

        if orders_file.exists():
            old_data = CSVFileManager(orders_file).read()
            data = pd.concat([old_data, new_row], ignore_index=True)
        else:
            data = new_row

        CSVFileManager(orders_file).write(data)
        logger.debug("Comanda desada correctament.")
        print(f"Comanda desada correctament a {orders_file}")

    """
    Mètode run: aquest és el punt d'entrada de l'aplicació, on es mostra un menú per seleccionar un caixer, un client i els productes que volen comprar.
    Quan a main.py fem: app=PrpeareOrder() i app.run(), s'executa aquest mètode, que coordina tot el procés de preparació d'una comanda.
    El seu funcionament és el següent:
    1. Carrega les dades dels fitxers CSV cridant al mètode load_data().
    2. Mostra un missatge de benvinguda i les llistes de caixers, clients i productes disponibles.
    3. Demana a l'usuari que introdueixi el DNI del caixer i el DNI del client, utilitzant
       els mètodes ask_cashier() i ask_customer(). Aquests mètodes validen les dades introduïdes i
       retornen els objectes corresponents. No continua fins que el DNI sigui correcte. 
       Quan es troba el caixer i el client, es mostra la seva informació per pantalla.
    4. Crea una nova comanda utilitzant la classe Order, passant-li el caixer i el client seleccionats.
    5. Mostra la llista de productes disponibles i permet a l'usuari escollir productes i afegir-los a la comanda utilitzant el mètode add_products_to_order().
    6. Mostra la informació completa de la comanda per pantalla utilitzant el mètode show() de l'objecte Order.
    """
    def run(self) -> None:
        """Executa el menú principal de preparació d'una comanda."""
        self.load_data()

        print("Benvingut/da al sistema de menjar ràpid")
        self.show_cashiers()
        self.show_customers()

        cashier = self.ask_cashier()
        customer = self.ask_customer()
        order = Order(cashier, customer)

        self.show_products()
        self.add_products_to_order(order)

        print("\nComanda final:")
        order.show()

        if self.ask_yes_no("\nVols desar la comanda en un CSV? Sí/No: "):
            self.save_order(order)
