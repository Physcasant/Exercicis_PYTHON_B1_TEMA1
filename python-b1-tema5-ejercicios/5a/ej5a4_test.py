from ej5a4 import *


def test_connect_sql():
    connector = DatabaseConnector()
    sql_db = SQLDatabase()
    connector.connect(sql_db)
    assert sql_db.connected == True, "SQL database connection failed"


def test_connect_postgres():
    connector = DatabaseConnector()
    postgres_db = PostgresDatabase()
    connector.connect(postgres_db)
    assert postgres_db.connected == True, "Postgres database connection failed"


def test_connect_redshift():
    connector = DatabaseConnector()
    redshift_db = RedshiftDatabase()
    connector.connect(redshift_db)
    assert redshift_db.connected == True, "Redshift database connection failed"
