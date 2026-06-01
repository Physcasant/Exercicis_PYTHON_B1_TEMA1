# Arxiu motor.py

from abc import ABC, abstractmethod

class Motor(ABC):
    def __init__(self):
        self.encesa = False
    
    @abstractmethod
    def engegar(self):
        self.encesa = True
    
    @abstractmethod
    def accelerar(self, quantitat):
        # accelerem el motor en la quantitat especificada
        pass
    
    @abstractmethod
    def apagar(self):
        self.encesa = False

# Creem una classe concreta per a un motor elèctric
class MotorElectric(Motor):

    def __init__(self):
        super().__init__()

    def engegar(self):
        self.encesa = True
        print("Engegant cotxe amb motor elèctric, estat:", self.encesa)

    def accelerar(self, quantitat):
        print(f"Accelerant el cotxe a {quantitat}")
    
    def apagar(self):
        self.encesa = False
        print("Apagant cotxe amb motor elèctric, estat:", self.encesa)