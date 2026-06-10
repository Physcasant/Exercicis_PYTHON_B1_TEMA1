# Projecte final Python B1 - Sistema de menjar ràpid

Solució model del projecte final del nivell B1.

## Estructura

```text
uoc_Sistema_menjar_rapid_project/
├── data/
│   ├── cashiers.csv
│   ├── customers.csv
│   ├── drinks.csv
│   ├── hamburgers.csv
│   ├── happyMeal.csv
│   └── sodas.csv
├── orders/
│   ├── __init__.py
│   └── order.py
├── products/
│   ├── __init__.py
│   ├── food_package.py
│   └── product.py
├── users/
│   ├── __init__.py
│   └── user.py
├── util/
│   ├── __init__.py
│   ├── converter.py
│   └── file_manager.py
├── main.py
└── prepare_order.py
```

## Com executar-lo

1. Obrir la carpeta `uoc_fast_food_project` amb VS Code.
2. Instal·lar pandas si no els tens instal·lats:

```bash
pip install pandas
```

3. Executa:

```bash
python main.py
```

## Dades de prova

Pots provar el funcionament amb:

- DNI caixer: `5001`
- DNI client: `1001`
- Productes: `H1`, `G1`

## Notes

- El mètode `save_order()` desa opcionalment la comanda a `data/orders.csv`.
- El projecte utilitza classes abstractes, herència, lectura CSV amb pandas, conversió de DataFrames a objectes i integració mitjançant una classe principal.
