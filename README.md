# ConcesionarioPOOpython
sistema de concesionario en Python aplicando POO.

Nombre: Mariana Sierra
Fecha: 2 de Noviembre de 2025  

---

## Descripción
Este proyecto implementa sistema de concesionario en Python, aplicando  pilares de la Programación Orientada a Objetos (POO):
- Encapsulamiento  
- Herencia  
- Abstracción  
- Polimorfismo  

El sistema permite crear diferentes tipos de vehículos (automóviles y motos), calcular su precio final incluyendo impuestos y mostrar la ficha detallada de cada uno.

---

## Estructura

concesionario
- vehiculo.py # Clase abstracta padre (Vehiculo)
- automovil.py # Clase hija (Automovil)
- moto.py # Clase hija (Moto)
- main.py # Script principal (usa polimorfismo)


__________________


##  Requisitos previos

- Python  instalado en el sistema operativo.  
- Un editor o entorno para ejecutar código Python (por ejemplo **Visual Studio Code**, **PyCharm**, o la terminal del sistema).  
- No requiere librerías externas, solo Python estándar.

## Cómo ejecutar el programa

---

###  Descargar los scripts 

1. Entra al repositorio en GitHub.  
2. Haz clic en el botón verde **"Code" → "Download ZIP"**.  
3. Descomprime el archivo ZIP en tu computadora.  
4. Abre la carpeta del proyecto (por ejemplo `concesionarioPOOpython/`) en tu editor o terminal.  
5. Dentro de esa carpeta deben estar los archivos:
vehiculo.py
automovil.py
moto.py
main.py


6. Desde la terminal, ejecuta el programa principal con:
python main.py

---

##  salida esperada

Automovil | Toyota Yaris ($40000.00) | 5 puertas | Final: $43200.00
Automovil | Mazda 3 ($27000.00) | 4 puertas | Final: $29160.00
Moto | Honda CB190R ($12000.00) | 190 cc | Final: $12600.00
Moto | BMW G310R ($20000.00) | 313 cc | Final: $21800.00

Valor total del inventario: $106760.00


---

