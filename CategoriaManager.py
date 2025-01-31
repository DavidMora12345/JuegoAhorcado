class CategoriaManager:
    def _init_(self):
        self.categorias = {
            "Frutas": ["manzana", "pera", "naranja", "uva", "platano"],
            "Animales": ["elefante", "tigre", "leon", "gato", "perro"],
            "Colores": ["rojo", "azul", "verde", "amarillo", "morado"],
            "Cosas": ["mesa", "silla", "puerta", "ventana", "cama"]
        }

    def obtener_categorias(self):
        return list(self.categorias.keys())

    def obtener_palabras(self, categoria):
        return self.categorias.get(categoria, [])