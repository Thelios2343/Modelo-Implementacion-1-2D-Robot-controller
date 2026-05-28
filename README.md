# Robot Pozz - Controlador 2D

Proyecto desarrollado en Python y C para simular el movimiento de un robot en un plano bidimensional utilizando una interfaz gráfica con Tkinter.

---

# Descripción

La aplicación permite controlar un robot dentro de un espacio limitado en un plano cartesiano.

El usuario puede mover el robot en cuatro direcciones:

* Arriba
* Abajo
* Izquierda
* Derecha

El sistema valida automáticamente que el robot no salga de los límites definidos.

La lógica de movimiento fue implementada en lenguaje C y conectada con Python mediante `ctypes`.

La interfaz gráfica fue desarrollada usando Tkinter.

---

# Características

* Interfaz gráfica en Tkinter
* Integración Python + C
* Librerías compartidas (`.so` y `.dll`)
* Validación de límites
* Arquitectura modular
* Soporte multiplataforma
* Reinicio de posición

---

# Límites del plano

| Eje | Mínimo | Máximo |
| --- | ------ | ------ |
| X   | -50    | 50     |
| Y   | -25    | 25     |

---

# Tecnologías utilizadas

* Python 3
* Tkinter
* C
* ctypes
* GCC

---

# Estructura del proyecto

```text id="6r9j8o"
.
├── main.py
├── robot.py
├── robot_calc.c
└── README.md
```

---

# Requisitos

## Linux

* Python 3
* GCC
* Tkinter

## Windows

* Python 3
* GCC/MinGW (opcional si desea recompilar)

---

# Instalación de Tkinter

## Debian / Ubuntu

```bash id="jlwm4m"
sudo apt install python3-tk
```

## Arch Linux

```bash id="jlwm4w"
sudo pacman -S tk
```

---

# Compilación del módulo en C

## Linux

```bash id="jlwm57"
gcc -shared -o robotcore.so -fPIC robotcore.c
```

## Windows (MinGW)

```bash id="jlwm5g"
gcc -shared -o robotcore.dll robotcore.c
```

---

# Ejecución

```bash id="jlwm5q"
python3 main.py
```

---

# Arquitectura

El proyecto se divide en dos partes principales:

## Backend (C)

Responsable de:

* Validación de movimientos
* Cálculo de posiciones
* Restricciones del plano

## Frontend (Python + Tkinter)

Responsable de:

* Mostrar la interfaz gráfica
* Capturar entradas del usuario
* Actualizar el estado visual del robot

---

# Comunicación Python-C

La integración entre Python y C se realiza usando `ctypes`.

Ejemplo:

```python id="jlwm60"
_lib.calcular_nueva_pos(
    self.x,
    self.y,
    direccion.encode("utf-8"),
    pasos,
    ctypes.byref(nueva_x),
    ctypes.byref(nueva_y)
)
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

# Captura de funcionamiento

Interfaz gráfica para el control del robot mediante botones direccionales y validación de movimiento.

---

# Autores

Juan Pablo Roa Monterrosa.

Juan Jose Mosquera Nieva.

Laura Meneses Acosta.
