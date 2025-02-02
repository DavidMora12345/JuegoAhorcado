from tkinter import Tk
from JuegoAhorcadoApp import JuegoAhorcadoApp

if __name__ == "__main__":
    # Crear la ventana principal
    root = Tk()
    root.geometry("500x600")
    root.configure(bg="#f4f4f4")
    
    # Inicializar la aplicación
    app = JuegoAhorcadoApp(root)
    app.iniciar()
    
    # Iniciar el loop principal de Tkinter
    root.mainloop()
