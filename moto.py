# moto.py

from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precioBase, cc):
        # Se invoca el constructor de la clase base
        super().__init__(marca, modelo, precioBase)

        # Validamos el cilindraje (cc)
        if cc <= 0:
            raise ValueError("El cilindraje debe ser mayor que cero.")
        self._cc = cc

    # Implementación concreta del método abstracto impuesto()
    def impuesto(self) -> float:
        # Si el cilindraje es menor o igual a 250, se aplica el 5%
        tasa = 0.05 if self._cc <= 250 else 0.09
        return self.precioBase * tasa

    # Sobrescribimos ficha() para incluir el cilindraje
    def ficha(self) -> str:
        return f"Moto | {super().ficha()} | {self._cc} cc"

