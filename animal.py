class Animal:
    
    def hacer_sonido(self):
        return "El animal hace un sonido"

    
class Perro:
    
    def hacer_sonido(self):
        return "El perro ladra"
    
class Gato:
    
    def hacer_sonido(self):
        return "El gato maulla"

# Comprobacion
animales = [Perro(), Gato(), Animal()]

for animal in animales:
    print(animal.hacer_sonido())