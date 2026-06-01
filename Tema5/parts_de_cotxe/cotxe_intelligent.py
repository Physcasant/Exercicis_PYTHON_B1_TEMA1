# Arxiu cotxe_intelligent.py
from parts_de_cotxe import (motor,suspensio,frens,sensor)
#from . import motor
#from . import suspensio
#from . import frens
#from . import sensor

class CotxeIntelligent:
    def __init__(self):
        self.motor = motor.MotorElectric()
        self.frens = frens.Frens()
        self.suspensio = suspensio.Suspensio()
        self.sensor = sensor.Sensor()

    def engegar(self):
        self.motor.engegar()

    def accelerar(self, quantitat):
        self.motor.accelerar(quantitat)

    def apagar(self):
        self.motor.apagar()

    def frenar(self):
        self.frens.frenar()
        print(f"Frenant el cotxe")

    def girar(self, direccio):
        self.suspensio.girar(direccio)
        print(f"Girant {direccio} graus")

    def evitar_obstacle(self):
        obstacle_detectat = self.sensor.detectar_obstacle()
        if obstacle_detectat:
            print("obstacle detectat")
            self.frenar()
            self.sensor.cercar_ruta_alternativa()
#cotxe_intelligent_x10 = CotxeIntelligent()
#cotxe_intelligent_x10.engegar()
#cotxe_intelligent_x10.accelerar(10)
#cotxe_intelligent_x10.girar(45)
#cotxe_intelligent_x10.evitar_obstacle()
#cotxe_intelligent_x10.frenar()
#cotxe_intelligent_x10.apagar()    