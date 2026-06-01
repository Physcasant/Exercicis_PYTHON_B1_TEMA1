"""
Enunciado:
Implementa la función 'average_score_ram(scores_dict)' que recibe un
diccionario con el nombre y la calificación de los estudiantes y calcula
el promedio de calificaciones. Se debe usar un bucle 'for' para ilustrar
el uso de RAM.

La función 'average_score_heap(scores_dict)' ya está implementada y
debe almacenar el promedio de calificaciones en el Heap; sin embargo, existe un error 
en este cálculo identifícalo y corrígelo.

Parámetros:
- scores_dict: Diccionario con el nombre del estudiante como clave y su
calificación como valor.

Ejemplo:
    Entrada:
        average_score_ram({'Juan': 8, 'Maria': 7, 'Pedro': 9})
        average_score_heap({'Juan': 8, 'Maria': 7, 'Pedro': 9})
        
    Salida:
        8.0
        8.0        
        
Enunciat:

Implementa la funció 'average_score_ram(scores_dict)' que rep un
diccionari amb el nom i la qualificació dels estudiants i calcula
la mitjana de qualificacions. Cal utilitzar un bucle 'for' per il·lustrar
l'ús de RAM.

La funció 'average_score_heap(scores_dict)' ja està implementada i ha d'emmagatzemar
la mitjana de qualificacions al Heap; no obstant això, hi ha un error en aquest càlcul 
identifica'l i corregeix-lo.

Paràmetres:
- scores_dict: Diccionari amb el nom de l'estudiant com a clau i la seva
qualificació com a valor.

Exemple:
     Entrada:
         average_score_ram({'Juan': 8, 'Maria': 7, 'Pedro': 9})
         average_score_heap({'Juan': 8, 'Maria': 7, 'Pedro': 9})
        
     Sortida:
         8.0
         8.0
    
"""


def average_score_ram(scores_dict):
    total_score = 0
    count = 0
    for score in scores_dict.values():
        total_score += score
        count += 1
    average = total_score / count
    return average


def average_score_heap(scores_dict):
    # Store the dictionary in Heap    
    score_list = list(scores_dict.values())
    # You should correct and overwrite something in the following line.
    heap_average = sum(score_list) /len(score_list)
    return heap_average

scores_dict = {"Juan": 6.7, "Maria": 9.1, "Pedro": 6.5, "Tomas": 8.2, "Julio": 9}
print(average_score_ram(scores_dict))
print(average_score_heap(scores_dict))

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# scores_dict = {"Juan": 6.7, "Maria": 9.1, "Pedro": 6.5, "Tomas": 8.2, "Julio": 9}

# print(average_score_ram(scores_dict))
# print(average_score_heap(scores_dict))
