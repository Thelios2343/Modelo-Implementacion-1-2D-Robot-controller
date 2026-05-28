import tkinter as tk
from tkinter import ttk
from robot import Robot


def crear_ventana():
    robot = Robot()

    ventana = tk.Tk()
    ventana.title("Robot Pozz")
    ventana.resizable(False, False)

    # --- Zona de posición ---
    frame_pos = ttk.LabelFrame(ventana, text="Posición actual", padding=10)
    frame_pos.pack(padx=20, pady=(20, 10), fill="x")

    lbl_pos = ttk.Label(frame_pos, text="(0, 0)", font=("Courier", 18, "bold"))
    lbl_pos.pack()

    lbl_mensaje = ttk.Label(frame_pos, text="", foreground="gray")
    lbl_mensaje.pack()

    # --- Pasos ---
    frame_ctrl = ttk.LabelFrame(ventana, text="Control", padding=10)
    frame_ctrl.pack(padx=20, pady=10, fill="x")

    ttk.Label(frame_ctrl, text="Número de pasos:").grid(row=0, column=0, sticky="w")
    entrada_pasos = ttk.Entry(frame_ctrl, width=8)
    entrada_pasos.insert(0, "1")
    entrada_pasos.grid(row=0, column=1, padx=(8, 0))

    # --- Botones de dirección ---
    frame_dir = ttk.Frame(ventana, padding=10)
    frame_dir.pack(padx=20, pady=(0, 20))

    def mover(dir_str):
        try:
            pasos = int(entrada_pasos.get())
        except ValueError:
            lbl_mensaje.config(text="Los Pasos debe ser un número entero", foreground="red")
            return

        exito, msg = robot.mover(dir_str, pasos)
        lbl_pos.config(text=f"({robot.x}, {robot.y})")
        color = "green" if exito else "red"
        lbl_mensaje.config(text=msg, foreground=color)

    # --- Cambio de estado a 0-0 ---
    
    def reset():
        robot.reset()
        lbl_mensaje.config(text="Posición reiniciada", foreground="gray")
        lbl_pos.config(text=f"({robot.x}, {robot.y})") 

    # Distribucion en Cruz
    ttk.Button(frame_dir, text="▲  Arriba",    width=12,
               command=lambda: mover("arriba")).grid(row=0, column=1, pady=4)
    ttk.Button(frame_dir, text="◄  Izquierda", width=12,
               command=lambda: mover("izquierda")).grid(row=1, column=0, padx=4)
    ttk.Button(frame_dir, text="●  Reset",     width=12,
               command=reset).grid(row=1, column=1)
    ttk.Button(frame_dir, text="Derecha  ►",   width=12,
               command=lambda: mover("derecha")).grid(row=1, column=2, padx=4)
    ttk.Button(frame_dir, text="▼  Abajo",     width=12,
               command=lambda: mover("abajo")).grid(row=2, column=1, pady=4)

    ventana.mainloop()


if __name__ == "__main__":
    crear_ventana()
