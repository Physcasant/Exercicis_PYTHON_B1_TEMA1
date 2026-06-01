"""
Enunciado:
Se tiene el paquete 'ej3a3_time_package' el cual tiene dos módulos llamados:
'convert_date_format' y 'date_operations', los módulos ya están hechos,
por lo tanto, se requiere configurar el archivo '__init__.py' del paquete.
Se tiene la siguiente estructura:

    ej3a3_time_package/
        __init__.py
        convert_date_format.py
        date_operations.py

El módulo 'convert_date_format.py' contiene dos funciones:
'string_to_datetime(date_string, date_format)',
'datetime_to_string(date_time, date_format)'.

El módulo 'date_operations.py' tiene funciones como: 'add_days(date, days)',
'middle_day_between_two_dates(initial_date, final_date)'

El paquete 'ej3a3_time_package' se debe importar desde el script 'ej3a3_main.py'
por ello, se debe configurar el archivo '__init__.py'. Por tanto es necesario crear este archivo.

Ejemplo:
    Entrada:
    convert_date_format.string_to_datetime("2023-12-25")
    date_operations.add_days(datetime.datetime(2023, 12, 25, 0, 0), 10)
    date_operations.middle_day_between_two_dates(
        datetime.datetime(2023, 12, 25, 0, 0),
        datetime.datetime(2024, 1, 4, 0, 0)
    )

    Salida:
    2023-12-25 00:00:00
    2024-01-04 00:00:00
    2023-12-30 00:00:00

Enunciat:

Es té el paquet 'ej3a3_time_package' el qual té dos mòduls anomenats:
'convert_date_format' i 'date_operations', els mòduls ja estan fets,
per tant, cal configurar el fitxer '__init__.py' del paquet.
Es té la següent estructura:

     ej3a3_time_package/
         __init__.py
         convert_date_format.py
         date_operations.py

El mòdul 'convert_date_format.py' conté dues funcions:
'string_to_datetime(date_string, date_format)',
'datetime_to_string(date_time, date_format)'.

El mòdul 'date_operations.py' té funcions com: 'add_days(date, days)',
'middle_day_between_two_dates(initial_date, final_date)'

El paquet 'ej3a3_time_package' s'ha d'importar des de l'script 'ej3a3_main.py'
per això, cal configurar el fitxer '__init__.py'.

Exemple:
     Entrada:
     convert_date_format.string_to_datetime("2023-12-25")
     date_operations.add_days(datetime.datetime(2023, 12, 25, 0, 0), 10)
     date_operations.middle_day_between_two_dates(
         datetime.datetime(2023, 12, 25, 0, 0),
         datetime.datetime(2024, 1, 4, 0, 0)
     )

     Sortida:
     2023-12-25 00:00:00
     2024-01-04 00:00:00
     2023-12-30 00:00:00

"""

from ej3a3_time_package import convert_date_format, date_operations

initial_date = convert_date_format.string_to_datetime("2023-12-25")
final_date = date_operations.add_days(initial_date, 10)
middle_date = date_operations.middle_day_between_two_dates(initial_date, final_date)

print(initial_date)
print(final_date)
print(
    f"Día medio entre la fecha {initial_date.date()} y {final_date.date()} "
    f"es: {middle_date.date()}"
)
