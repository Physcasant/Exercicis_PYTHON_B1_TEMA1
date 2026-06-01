"""
Enunciado:
Implementa la función 'create_read_file()', que no recibe ningún
parámetro debido a que esta función debe crear un archivo de texto 
'text_file.txt', dentro de dicho archivo se deben escribir tres líneas de
información. La primera línea debe contener un nombre, la segunda línea un
apellido y finalmente, la edad. A continuación se debe leer el archivo e imprimir
por consola todas las líneas del mismo.

Parámetro:
- No recibe ningún parámetro debido a que dentro de esta función se crea un
archivo de texto.

Ejemplo:
    Salida:
        Juan
        Perez
        30

Enunciat:
Implementa la funció 'create_read_file()', que no rep cap
paràmetre pel fet que aquesta funció ha de crear un fitxer de text
'text_file.txt', dins d'aquest fitxer cal escriure tres línies d'
informació. La primera línia ha de contenir un nom, la segona línia un
cognom i, finalment, l'edat. A continuació cal llegir el fitxer i imprimir
per consola totes les línies del mateix.

Paràmetre:
- No rep cap paràmetre pel fet que dins d'aquesta funció es crea un
fitxer de text.

Exemple:
     Sortida:
         Joan
         Perez
         30

"""
def create_read_file():
    # Primer creem el fitxer i hi escrivim tres línies
    with open("text_file.txt", "w") as file:
        file.write("Joan\n")
        file.write("Perez\n")
        file.write("30\n")

    # Després obrim el fitxer en mode lectura
    with open("text_file.txt", "r") as file:
        lines = file.readlines()

    # Finalment imprimim totes les línies
    for line in lines:
        print(line.strip())


create_read_file()



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# create_read_file()
