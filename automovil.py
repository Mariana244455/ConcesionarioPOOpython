# automovil.py

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, precioBase, puertas):
        # Llamamos al constructor de la clase padre con super()
        super().__init__(marca, modelo, precioBase)

        # Validamos que el número de puertas sea válido
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que cero.")
        self._puertas = puertas

    # Implementación  del método abstracto impuesto()
    def impuesto(self) -> float:
        # Se calcula el 8% del precio base
        impuestoBase = self.precioBase * 0.08
        # Si tiene 5 puertas, se resta 1% del precio base al impuesto
        descuento = self.precioBase * 0.01 if self._puertas == 5 else 0
        return impuestoBase - descuento

    # Sobrescribimos ficha() para incluir el número de puertas
    def ficha(self) -> str:
        return f"Automovil | {super().ficha()} | {self._puertas} puertas"
