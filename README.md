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








# Mini Sistema de Concesionario en Python

**Nombre:** Magis  
**Fecha:** Noviembre 2025  

Este proyecto implementa un mini sistema de concesionario de vehículos en Python, aplicando los cuatro pilares fundamentales de la Programación Orientada a Objetos (POO): encapsulamiento, herencia, abstracción y polimorfismo. El sistema permite crear diferentes tipos de vehículos (automóviles y motos), calcular su precio final incluyendo impuestos específicos según su tipo y mostrar una ficha descriptiva de cada uno, además del valor total del inventario. Está diseñado para ser claro, modular y fácilmente ampliable.

## 📁 Estructura del proyecto

concesionario/
├── vehiculo.py # Clase abstracta padre (Vehiculo)
├── automovil.py # Clase hija Automovil
├── moto.py # Clase hija Moto
└── main.py # Script principal que ejecuta el sistema



## ⚙️ Requisitos previos

- Python **3.8 o superior** instalado en el sistema operativo.  
- Un editor o entorno para ejecutar código Python (por ejemplo **Visual Studio Code**, **PyCharm**, o la terminal del sistema).  
- No requiere librerías externas, solo Python estándar.

## 🚀 Cómo ejecutar el programa

### Opción 1: Clonar el repositorio desde GitHub

1. Abre una terminal o consola.  
2. Clona el repositorio ejecutando:
git clone https://github.com/TU_USUARIO/concesionario-poo-python.git

css
Copiar código
3. Ingresa a la carpeta del proyecto:
cd concesionario-poo-python

markdown
Copiar código
4. Ejecuta el programa principal:
python main.py

yaml
Copiar código

---

### Opción 2: Descargar los scripts manualmente

1. Entra al repositorio en GitHub.  
2. Haz clic en el botón verde **"Code" → "Download ZIP"**.  
3. Descomprime el archivo ZIP en tu computadora.  
4. Abre la carpeta del proyecto (por ejemplo `concesionario/`) en tu editor o terminal.  
5. Dentro de esa carpeta deben estar los archivos:
vehiculo.py
automovil.py
moto.py
main.py

markdown
Copiar código
6. Desde la terminal, ejecuta el programa principal con:
python main.py

yaml
Copiar código
7. Si Python no está en tu PATH o usas Windows, también puedes ejecutar:
py main.py

yaml
Copiar código

---

## 🧩 Ejemplo de salida esperada

Automovil | Toyota Yaris ($40000.00) | 5 puertas | Final: $43200.00
Automovil | Mazda 3 ($27000.00) | 4 puertas | Final: $29160.00
Moto | Honda CB190R ($12000.00) | 190 cc | Final: $12600.00
Moto | BMW G310R ($20000.00) | 313 cc | Final: $21800.00

Valor total del inventario: $106760.00

yaml
Copiar código

---

## 🧠 Conceptos aplicados de Programación Orientada a Objetos

- **Encapsulamiento:** Los atributos de las clases están protegidos y se accede a ellos mediante métodos o propiedades.  
- **Herencia:** Las clases `Automovil` y `Moto` heredan la estructura y métodos de la clase abstracta `Vehiculo`.  
- **Abstracción:** `Vehiculo` define un método abstracto `impuesto()` que las clases hijas implementan según sus reglas.  
- **Polimorfismo:** El programa maneja una lista de objetos `Vehiculo` que pueden ser `Automovil` o `Moto`, ejecutando el método correcto en cada caso.

---

## 💡 Créditos

Proyecto desarrollado por **Magis**, estudiante de ingeniería, como ejercicio académico para aplicar los conceptos de Programación Orientada a Objetos en Python.  
Diseñado para comprender la estructura modular, el uso de clases y la relación entre objetos en un entorno práctico.
