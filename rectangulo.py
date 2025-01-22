class Rectangulo:
    
    # atributos
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    # metodos
    def area(self):
        area = self.ancho * self.alto 
        return area
    
    def perimetro(self):
        perimetro = 2 * self.ancho + 2 * self.alto
        return perimetro
    
    def es_cuadrado(self):
        print( self.ancho == self.alto)