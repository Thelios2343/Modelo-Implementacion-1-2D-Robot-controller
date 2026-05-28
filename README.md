# Robot 2D Controller

Proyecto desarrollado en Python y C para el control de un robot en un plano bidimensional utilizando una interfaz gráfica en Tkinter.

## Descripción

La aplicación simula el movimiento de un robot dentro de un área limitada.
El robot puede desplazarse en cuatro direcciones:

* Arriba
* Abajo
* Izquierda
* Derecha
* Reset

El sistema valida que el robot no salga de los límites establecidos del plano.

La lógica principal de movimiento fue implementada en C y conectada a Python mediante `ctypes`, mientras que la interfaz gráfica fue desarrollada usando Tkinter.

---

# Características

* Interfaz gráfica usando Tkinter
* Integración Python + C
* Validación de límites del plano
* Arquitectura modular
* Reinicio de posición
* Comunicación mediante librerías compartidas (`.so`)

---

# Estructura del proyecto

```text
.
├── robot.py
├── main.py
├── robot_calc.c
└── README.md
```

---

# Límites del plano

| Eje | Mínimo | Máximo |
| --- | ------ | ------ |
| X   | -50    | 50     |
| Y   | -25    | 25     |

---

# Requisitos

* Python 3
* Tkinter
* GCC
* Linux

---

# Instalación

## Instalar Tkinter

### Debian/Ubuntu

```bash
sudo apt install python3-tk
```

### Arch Linux

```bash
sudo pacman -S tk
```

---

# Compilación del módulo en C

```bash
gcc -shared -o robotcore.so -fPIC robotcore.c
```

---

# Ejecución

```bash
python3 main.py
```

---

# Arquitectura

El proyecto se divide en dos capas principales:

## Backend (C)

Responsable de:

* Validar movimientos
* Calcular posiciones
* Controlar límites

## Frontend (Python + Tkinter)

Responsable de:

* Mostrar la interfaz
* Capturar entradas del usuario
* Actualizar el estado visual

---

# Comunicación Python-C

La integración entre Python y C se realiza mediante la librería `ctypes`.

Ejemplo:

```python
_lib.calcular_nueva_pos.argtypes = [
    ctypes.c_int, ctypes.c_int,
    ctypes.c_char_p, ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
_lib.calcular_nueva_pos.restype = ctypes.c_int
```
---

# Casos de prueba

| Dirección | Pasos | Resultado           |
| --------- | ----- | ------------------- |
| Arriba    | 10    | (0,10)              |
| Derecha   | 60    | Movimiento inválido |
| Izquierda | 25    | (-25,0)             |
| Abajo     | 20    | (0,-20)             |

---

# Autores
Juan Pablo Roa Monterrosa,

Juan Jose Mosquera Nieva,

Laura Meneses Acosta
