"""
Enunciado:
Crea una clase llamada "DatabaseConnector" que represente un conector de
base de datos genérico con bajo acoplamiento, fácil de mantener y extender,
Por lo tanto, que permita conectarse a diferentes tipos de bases
de datos. La clase debe tener un método "connect" que permita establecer
una conexión con una base de datos específica.

Además, se deben crear tres clases para diferentes tipos de bases de datos:
"SQLDatabase", "PostgresDatabase", y "RedshiftDatabase". Cada clase de base
de datos debe tener una propiedad "connected" que se establezca en True
cuando se conecta correctamente a la base de datos.

Métodos y propiedades:

Clase "DatabaseConnector":
    connect(database): conecta a una base de datos específica. El parámetro
    "database" debe ser una instancia de una de las clases de base de datos
    ("SQLDatabase", "PostgresDatabase" o "RedshiftDatabase").

Clase "SQLDatabase":
    connected: propiedad booleana que indica si la conexión a la base de
    datos se estableció correctamente.

Clase "PostgresDatabase":
    connected: propiedad booleana que indica si la conexión a la base de
    datos se estableció correctamente.

Clase "RedshiftDatabase":
    connected: propiedad booleana que indica si la conexión a la base de
    datos se estableció correctamente.

Ejemplo:
    Entrada:
        db_connector = DatabaseConnector()
        sql_db = SQLDatabase()
        postgres_db = PostgresDatabase()
        redshift_db = RedshiftDatabase()
        print(sql_db.connected, postgres_db.connected, redshift_db.connected)
        db_connector.connect(sql_db)
        db_connector.connect(postgres_db)
        db_connector.connect(redshift_db)
        print(sql_db.connected, postgres_db.connected, redshift_db.connected)

    Salida:
        False False False
        True True True

Enunciat:
Crea una classe anomenada "DatabaseConnector" que representi un connector de
base de dades genèric amb baix acoblament, fàcil de mantenir i estendre,
Per tant, que permeti connectar-se a diferents tipus de bases de dades. 
La classe ha de tenir un mètode "connect" que permeti establir
una connexió amb una base de dades específica.

A més, s'han de crear tres classes per a diferents tipus de bases de dades:
"SQLDatabase", "PostgresDatabase", i "RedshiftDatabase". Cada classe de base de dades
  ha de tenir una propietat "connected" que s'estableixi en True
quan es connecta correctament a la base de dades.

Mètodes i propietats:

Classe "DatabaseConnector":
    connect(database): connecta a una base de dades específica. El paràmetre
    "database" ha de ser una instància d'una de les classes de base de dades
    ("SQLDatabase", "PostgresDatabase" o "RedshiftDatabase").

Classe "SQLDatabase":
    connected: propietat booleana que indica si la connexió a la base de dades
     es va establir correctament.

Classe "PostgresDatabase":
    connected: propietat booleana que indica si la connexió a la base de dades
     es va establir correctament.

Classe "RedshiftDatabase":
    connected: propietat booleana que indica si la connexió a la base de dades
     es va establir correctament.

Exemple:
    Entrada:
        db_connector = DatabaseConnector()
        sql_db = SQLDatabase()
        postgres_db = PostgresDatabase()
        redshift_db = RedshiftDatabase()
        print(sql_db.connected, postgres_db.connected, redshift_db.connected)
        db_connector.connect(sql_db)
        db_connector.connect(postgres_db)
        db_connector.connect(redshift_db)
        print(sql_db.connected, postgres_db.connected, redshift_db.connected)

    Sortida:
        False False False
        True True True
"""

# Write class DatabaseConnector here

# Write class SQLDatabase here


# Write class PostgresDatabase here


# Write class RedshiftDatabase here


# Por la propia naturaleza del ejercicios no se puede probar imprimiendo por pantalla, 
# revisa los tests para revisar la corrección de tu propuesta de solución
# Per la pròpia naturalesa de l'exercicis no es pot provar imprimint per pantalla, 
# revisa els tests per a revisar la correcció de la teva proposta de solució
