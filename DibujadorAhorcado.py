class DibujadorAhorcado:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ojos_felices = None
        self.boca_feliz = None
        self.ojos_tristes = None
        self.boca_triste = None
        self.cabeza = None

    def dibujar_estructura(self):
        """Dibuja la estructura del ahorcado sin el cuerpo."""
        self.canvas.create_line(50, 250, 250, 250, width=4)  # Base
        self.canvas.create_line(100, 250, 100, 50, width=4)  # Poste vertical
        self.canvas.create_line(100, 50, 200, 50, width=4)   # Poste horizontal
        self.canvas.create_line(200, 50, 200, 80, width=4)   # Cuerda

    def dibujar_ahorcado(self, errores):
        """Dibuja las partes del cuerpo y cambia la cara cuando pierde."""

        if errores == 1:
            # Dibujar cabeza con carita feliz
            self.cabeza = self.canvas.create_oval(180, 80, 220, 120, width=2)
            self.ojos_felices = [
                self.canvas.create_oval(190, 90, 195, 95, fill="black"),  # Ojo izquierdo
                self.canvas.create_oval(205, 90, 210, 95, fill="black")   # Ojo derecho
            ]
            self.boca_feliz = self.canvas.create_arc(190, 100, 210, 110, start=0, extent=-180, style="arc", width=2)

        elif errores == 2:
            self.canvas.create_line(200, 120, 200, 180, width=2)  # Cuerpo
        elif errores == 3:
            self.canvas.create_line(200, 140, 180, 160, width=2)  # Brazo izquierdo
        elif errores == 4:
            self.canvas.create_line(200, 140, 220, 160, width=2)  # Brazo derecho
        elif errores == 5:
            self.canvas.create_line(200, 180, 180, 220, width=2)  # Pierna izquierda
        elif errores == 6:
            self.canvas.create_line(200, 180, 220, 220, width=2)  # Pierna derecha
            
            # Borrar carita feliz antes de dibujar carita con X
            if self.ojos_felices:
                for ojo in self.ojos_felices:
                    self.canvas.delete(ojo)
            if self.boca_feliz:
                self.canvas.delete(self.boca_feliz)

            # Dibujar carita con X y boca triste
            self.ojos_tristes = [
                self.canvas.create_line(190, 90, 195, 95, width=2, fill="red"),
                self.canvas.create_line(195, 90, 190, 95, width=2, fill="red"),
                self.canvas.create_line(205, 90, 210, 95, width=2, fill="red"),
                self.canvas.create_line(210, 90, 205, 95, width=2, fill="red")
            ]
            self.boca_triste = self.canvas.create_arc(190, 110, 210, 100, start=0, extent=180, style="arc", width=2, outline="red")
