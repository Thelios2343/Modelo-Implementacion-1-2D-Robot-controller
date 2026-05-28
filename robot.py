import os
import ctypes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if os.name == "nt":
    LIB_NAME = "robot_calc.dll"
else:
    LIB_NAME = "robot_calc.so"

_lib_path = os.path.join(BASE_DIR, LIB_NAME)
_lib = ctypes.CDLL(_lib_path)


# Tipos de argumentos
_lib.calcular_nueva_pos.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]

# Tipo de retorno
_lib.calcular_nueva_pos.restype = ctypes.c_int


class Robot:

    def __init__(self):
        self.x = 0
        self.y = 0

    def mover(self, direccion: str, pasos: int) -> tuple[bool, str]:
        """
        Intenta mover el robot.
        Devuelve (éxito, mensaje).
        """

        nueva_x = ctypes.c_int(0)
        nueva_y = ctypes.c_int(0)

        valido = _lib.calcular_nueva_pos(
            self.x,
            self.y,
            direccion.lower().encode("utf-8"),
            pasos,
            ctypes.byref(nueva_x),
            ctypes.byref(nueva_y),
        )

        if valido:
            self.x = nueva_x.value
            self.y = nueva_y.value

            return True, f"Posición: ({self.x}, {self.y})"

        return False, (
            f"Movimiento inválido. "
            f"Posición actual: ({self.x}, {self.y})"
        )

    # Reiniciar posición
    def reset(self):
        self.x = 0
        self.y = 0

