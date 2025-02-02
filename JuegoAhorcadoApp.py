import tkinter as tk
from CategoriaManager import CategoriaManager
from InterfazMenu import InterfazMenu
from InterfazJuego import InterfazJuego

class JuegoAhorcadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")
        self.categoria_manager = CategoriaManager()  # Inicializar el manejador de categorías

    def iniciar(self):
        """Inicia la aplicación mostrando el menú principal."""
        self.mostrar_menu()

    def mostrar_menu(self):
        """Muestra el menú principal."""
        InterfazMenu(self.root, self.iniciar_juego, self.categoria_manager).mostrar()

    def iniciar_juego(self, categoria):
        """Inicia el juego con la categoría seleccionada."""
        palabras = self.categoria_manager.obtener_palabras(categoria)
        InterfazJuego(self.root, palabras, self.mostrar_menu)  # Ya crea la interfaz
