import random

class JuegoManager:
    def __init__(self, palabras):
        self.palabras = palabras
        self.reiniciar_juego()

    def reiniciar_juego(self):
        """Reinicia el estado del juego."""
        self.palabra = random.choice(self.palabras)  # Elegir una nueva palabra
        self.letras_adivinadas = random.sample(self.palabra, k=min(2, len(self.palabra) - 1))  # Prellenar algunas letras
        self.intentos = 6  # Reiniciar los intentos

    def adivinar_letra(self, letra):
        """Procesa la letra ingresada por el usuario."""
        if not letra.isalpha() or len(letra) != 1:
            return "Por favor, ingresa una sola letra válida."

        if letra in self.letras_adivinadas:
            return "Ya adivinaste esa letra. Intenta con otra."

        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
            return "¡Correcto! La letra está en la palabra."
        else:
            self.intentos -= 1
            return "Incorrecto. La letra no está en la palabra."

    def obtener_progreso(self):
        """Devuelve el progreso actual de la palabra."""
        progreso = ""
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        return progreso.strip()

    def juego_terminado(self):
        """Verifica si el juego ha terminado."""
        if all(letra in self.letras_adivinadas for letra in self.palabra):
            return "Ganaste"
        elif self.intentos <= 0:
            return "Perdiste"
        return None
