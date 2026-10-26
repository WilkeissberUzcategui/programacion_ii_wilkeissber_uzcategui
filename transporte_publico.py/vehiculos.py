
from abc import ABC, abstractmethod

class Vehiculo(ABC):

    placa : str
    capacidad : int
    activo : bool

    def __init__(self, placa : str, capacidad : int, activo : bool):
        self.placa = placa
        self.capacidad = capacidad
        self.activo = activo
    
    @abstractmethod
    def calcular_tarifa(self):
        pass

    def mostrar_datos(self):
        print(f"Placa del Vehiculo : {self.placa}") 
        print(f"Capacidad del Vehiculo : {self.capacidad}") 
        print(f"Vehiculo activo : {self.activo}") 

    def esta_activo(self):
        return self.activo

    def realizar_viaje(self, tarjeta):
        if not self.activo:
            raise ValueError("El vehículo está inactivo")

        tarjeta.pagar(self.calcular_tarifa())

class Bus(Vehiculo):

    rutas : int

    def __init__(self, placa : str, capacidad : int, activo : bool, rutas : int):
        super().__init__(placa, capacidad, activo)
        self.rutas = rutas

    def calcular_tarifa(self):
        return 0.35

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Rutas : {self.rutas}") 

        
class Metro(Vehiculo):

    vagones : int

    def __init__(self, placa : str, capacidad : int, activo : bool, vagones : int):
        super().__init__(placa, capacidad, activo)
        self.vagones = vagones

    def calcular_tarifa(self):
        return 0.45

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Vagones : {self.vagones}") 


if __name__ == "__main__":
    bus = Bus("ABC-123", 40, True, 5)
    metro = Metro("QWE-789", 30, False, 3)

    vehiculos = [bus, metro]

    for vehiculo in vehiculos:
        vehiculo.mostrar_datos()
        print("-------------------")
