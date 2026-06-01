# Arxiu sensor.py

import random

class Sensor():    
    def detectar_obstacle(self):
        # getrandbits en 2 perquè hi hagi més probabilitat d'un True [0, 1 ,2]
        return bool(random.getrandbits(2))

    def cercar_ruta_alternativa(self):
        print("Cercant ruta alternativa")