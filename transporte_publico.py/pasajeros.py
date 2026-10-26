
class TarjetaPasajero:

    titular : str
    __saldo : float

    def __init__(self, titular : str, saldo : float):

        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):

        return self.__saldo

    def recargar(self, cantidad : float):

        if cantidad <= 0:
            raise ValueError("La cantidad a recargar debe ser mayor a 0")

        self.__saldo += cantidad

    def pagar(self, cantidad : float):

        if cantidad <= 0:
            raise ValueError("La cantidad a pagar debe ser mayor a 0")

        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")

        self.__saldo -= cantidad

if __name__ == "__main__":
    
    from vehiculos import Bus, Metro

    tarjeta = TarjetaPasajero("Wilkeissber", 10.0)

    bus = Bus("ABC-123", 40, True, 5)
    metro = Metro("QWE-789", 30, False, 3)

    for vehiculo in [bus, metro]:
        try:
            vehiculo.realizar_viaje(tarjeta)
            print(f"Viaje realizado: {type(vehiculo).__name__}")
            print(f"Saldo restante: ${tarjeta.get_saldo():.2f}")
        except ValueError as error:
            print(f"No se pudo realizar el viaje: {error}")