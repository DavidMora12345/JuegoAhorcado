import tkinter as tk 

class InterfazMenu:
    def _init_(self, root, iniciar_juego, categoria_manager):
        self.root = root
        self.iniciar_juego = iniciar_juego
        self.categoria_manager = categoria_manager

    def mostrar(self):
        """Muestra el menú inicial para seleccionar una categoría."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Título del menú
        tk.Label(self.root, text="Seleccione una categoría", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333").pack(pady=20)

        # Botones para las categorías
        categorias = self.categoria_manager.obtener_categorias()
        for categoria in categorias:
            tk.Button(
                self.root,
                text=categoria,
                font=("Arial", 14),
                bg="#007acc",
                fg="white",
                width=15,
                command=lambda c=categoria: self.iniciar_juego(c)
            ).pack(pady=10)