import tkinter as tk
from JuegoManager import JuegoManager
from DibujadorAhorcado import DibujadorAhorcado  # Importar DibujadorAhorcado


class InterfazJuego:
    def __init__(self, root, palabras, regresar_menu_callback):
        self.root = root
        self.juego_manager = JuegoManager(palabras)
        self.regresar_menu_callback = regresar_menu_callback

        self.crear_interfaz()

    def crear_interfaz(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Etiquetas principales
        tk.Label(self.root, text="Juego del Ahorcado", font=("Arial", 24, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

        self.etiqueta_intentos = tk.Label(self.root, text=f"Intentos restantes: {self.juego_manager.intentos}", font=("Arial", 16), bg="#f4f4f4", fg="#333")
        self.etiqueta_intentos.pack(pady=10)

        self.etiqueta_palabra = tk.Label(self.root, text=self.juego_manager.obtener_progreso(), font=("Courier", 20), bg="#f4f4f4", fg="#007acc")
        self.etiqueta_palabra.pack(pady=20)

        # Entrada y botón para adivinar letras
        self.entrada_letra = tk.Entry(self.root, font=("Arial", 14), width=5, justify="center", bd=2, relief="solid")
        self.entrada_letra.pack(pady=10)

        self.boton_enviar = tk.Button(self.root, text="Adivinar", font=("Arial", 14), bg="#007acc", fg="white", command=self.adivinar_letra)
        self.boton_enviar.pack(pady=10)

        # Mensaje dinámico
        self.etiqueta_mensaje = tk.Label(self.root, text="", font=("Arial", 14), bg="#f4f4f4", fg="blue")
        self.etiqueta_mensaje.pack(pady=10)

        # Canvas para el dibujo del ahorcado
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white", bd=2, relief="solid")
        self.canvas.pack(pady=20)
        self.dibujador = DibujadorAhorcado(self.canvas)
        self.dibujador.dibujar_estructura()

        # Botones para reintentar y volver al menú (ocultos al inicio)
        self.botones_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.botones_frame.pack(pady=10)

        self.boton_reiniciar = tk.Button(self.botones_frame, text="Reintentar", font=("Arial", 14), bg="#28a745", fg="white", command=self.reiniciar_juego)
        self.boton_reiniciar.grid(row=0, column=0, padx=5)
        self.boton_reiniciar.grid_remove()

        self.boton_menu = tk.Button(self.botones_frame, text="Menú Principal", font=("Arial", 14), bg="#ff5722", fg="white", command=self.regresar_menu_callback)
        self.boton_menu.grid(row=0, column=1, padx=5)
        self.boton_menu.grid_remove()

    def adivinar_letra(self):
        letra = self.entrada_letra.get().lower()
        self.entrada_letra.delete(0, tk.END)

        mensaje = self.juego_manager.adivinar_letra(letra)
        self.etiqueta_mensaje.config(text=mensaje)

        self.etiqueta_palabra.config(text=self.juego_manager.obtener_progreso())
        self.etiqueta_intentos.config(text=f"Intentos restantes: {self.juego_manager.intentos}")

        # Actualizar dibujo en cada intento fallido
        self.dibujador.dibujar_ahorcado(6 - self.juego_manager.intentos)

        # Verificar estado del juego
        estado = self.juego_manager.juego_terminado()
        if estado == "Ganaste":
            self.etiqueta_mensaje.config(text="¡Felicidades, ganaste!", fg="green")
            self.boton_enviar.config(state="disabled")
            self.mostrar_botones_fin()
        elif estado == "Perdiste":
            self.etiqueta_mensaje.config(text=f"Perdiste. La palabra era: {self.juego_manager.palabra}", fg="red")
            self.boton_enviar.config(state="disabled")
            self.dibujador.dibujar_ahorcado(6)  # Dibujo completo del ahorcado
            self.mostrar_botones_fin()

    def reiniciar_juego(self):
        """Reinicia el juego actual."""
        self.juego_manager.reiniciar_juego()
        self.crear_interfaz()

    def mostrar_botones_fin(self):
        """Muestra los botones de 'Reintentar' y 'Menú Principal'."""
        self.boton_reiniciar.grid()
        self.boton_menu.grid()
