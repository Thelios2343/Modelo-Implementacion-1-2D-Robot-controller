import ctypes
import os


# Cargar la librería C
_lib_path = os.path.join(os.path.dirname(__file__), "robot_calc.so")
_lib = ctypes.CDLL(_lib_path)

# Indicacion a ctypes los tipos de la función
_lib.calcular_nueva_pos.argtypes = [
    ctypes.c_int, ctypes.c_int,
    ctypes.c_char_p, ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
_lib.calcular_nueva_pos.restype = ctypes.c_int


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def mover(self, direccion: str, pasos: int) -> tuple[bool, str]:
        """
        Intenta mover el robot. Devuelve (éxito, mensaje).
        """
        nueva_x = ctypes.c_int(0)
        nueva_y = ctypes.c_int(0)

        valido = _lib.calcular_nueva_pos(
            self.x, self.y,
            direccion.lower().encode("utf-8"),
            pasos,
            ctypes.byref(nueva_x),
            ctypes.byref(nueva_y),
        )

        if valido:
            self.x = nueva_x.value
            self.y = nueva_y.value
            return True, f"Posición: ({self.x}, {self.y})"
        else:
            return False, f"Movimiento inválido. Posición actual: ({self.x}, {self.y})"
    # --- Funcion para volver a la posicion inicial ---
    def reset(self):
        self.x = 0
        self.y = 0
