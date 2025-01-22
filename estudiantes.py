class Estudiante:
    
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final
        
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años y su nota final es de {self.nota_final}"
        
        
class Clase:
    
    def __init__(self):
        self.estudiantes = []
        
    def agregar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):  # Validación opcional
            self.estudiantes.append(estudiante)
        else:
            raise ValueError("El objeto debe ser una instancia de la clase Estudiante.")
        
    def eliminar_estudiante(self, estudiante):
        self.estudiantes = [est for est in self.estudiantes if est.nombre != estudiante.nombre]
        
        
