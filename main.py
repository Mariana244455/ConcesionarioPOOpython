# main.py

from automovil import Automovil
from moto import Moto

def main():
    #  lista polimórfica de vehículos
    inventario = [
        Automovil("Toyota", "Yaris", 40000, 5),
        Automovil("Mazda", "3", 27000, 4),
        Moto("Honda", "CB190R", 12000, 190),
        Moto("BMW", "G310R", 20000, 313)
    ]

    # Variable para acumular el valor total del inventario
    totalInventario = 0

    # Recorremos cada vehículo y usamos sus métodos sobrescritos
    for vehiculo in inventario:
        print(vehiculo)  
        totalInventario += vehiculo.precioFinal()

    # Se imprime el total general con formato de 2 decimales
    print(f"\nValor total del inventario: ${totalInventario:.2f}")

# Este condicional evita que el código se ejecute si se importa este archivo en otro módulo
if __name__ == "__main__":
    main()
