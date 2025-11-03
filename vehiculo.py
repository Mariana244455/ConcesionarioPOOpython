# vehiculo.py

from abc import ABC, abstractmethod  # ABC para  clase abstracta en Python

class Vehiculo(ABC):
    # inicializar atributos encapsulados con  guion bajo _
    def __init__(self, marca, modelo, precioBase):
        # Los atributos se "protegen" con un guion bajo. No son privados como en Java, 
        
        self._marca = marca
        self._modelo = modelo

        # Validación del precio base -  debe ser positivo
        if precioBase <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")
        self._precioBase = precioBase

    
    #  @property para acceder a los atributos encapsulados sin exponerlos directamente
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def precioBase(self):
        return self._precioBase

    # MÉTODO ABSTRACTO: impuesto()

    @abstractmethod
    def impuesto(self) -> float:
        pass

    # MÉTODO precioFinal()
    # Devuelve el precio total sumando el precio base y el impuesto calculado
    def precioFinal(self) -> float:
        return self._precioBase + self.impuesto()

    # MÉTODO ficha(): devuelve una descripción del vehículo
    def ficha(self) -> str:
        return f"{self._marca} {self._modelo} (${self._precioBase:.2f})"

    # Método especial __str__ permite imprimir objetos directamente 
    def __str__(self) -> str:
        return f"{self.ficha()} | Final: ${self.precioFinal():.2f}"
