class Ruta:

    nombre : str
    origen : str
    destino : str
    distancia : float
    vehiculo : object
    paradas : list

    def __init__(self, nombre : str, origen : str, destino : str, distancia : float, vehiculo):

        if nombre.strip() == "":
            raise ValueError("El nombre de la ruta no puede estar vacío")

        if origen.strip() == "" or destino.strip() == "":
            raise ValueError("El origen y el destino no pueden estar vacíos")

        if distancia <= 0:
            raise ValueError("La distancia debe ser mayor a 0")

        self.nombre = nombre
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.vehiculo = vehiculo
        self.paradas = []

    def agregar_parada(self, parada : str):

        if parada.strip() == "":
            raise ValueError("La parada no puede estar vacía")

        if parada in self.paradas:
            raise ValueError("La parada ya existe en la ruta")

        self.paradas.append(parada)

    def eliminar_parada(self, parada : str):

        if parada not in self.paradas:
            raise ValueError("La parada no existe en la ruta")

        self.paradas.remove(parada)

    def calcular_costo_viaje(self):

        return self.vehiculo.calcular_tarifa()

    def mostrar_datos(self):
        print(f"Ruta : {self.nombre}")
        print(f"Origen : {self.origen}")
        print(f"Destino : {self.destino}")
        print(f"Distancia : {self.distancia} km")
        print(f"Tarifa : ${self.calcular_costo_viaje():.2f}")
        print("Paradas :")

        if len(self.paradas) == 0:
            print("  (sin paradas)")
        else:
            for i in range(len(self.paradas)):
                print(f"  {i + 1}. {self.paradas[i]}")


if __name__ == "__main__":

    from vehiculos import Bus, Metro

    bus = Bus("ABC-123", 40, True, 5)
    metro = Metro("QWE-789", 30, True, 3)

    ruta1 = Ruta("Ruta 1", "Norte", "Sur", 12.5, bus)
    ruta2 = Ruta("Ruta 2", "Centro", "Valle", 8.0, metro)

    try:
        ruta1.agregar_parada("Parada A")
        ruta1.agregar_parada("Parada B")
        ruta1.agregar_parada("Parada A")
    except ValueError as error:
        print(f"Error: {error}")

    for ruta in [ruta1, ruta2]:
        ruta.mostrar_datos()
        print("-------------------")