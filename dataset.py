class DataSet():
    
    # atributo de clase
    tipo_dato = 'numerico'
    
    # atributo de instancia
    def __init__(self, data):
        self.data = data
    
    # añadir dato
    def añadir_dato(self, nuevo_dato):
        self.data.append(nuevo_dato)
    
    # otros metodos
    def media(self):
        return sum(self.data) / len(self.data)
    
    def mediana(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        midpoint = n//2
        if n % 2 == 0:
            return (sorted_data[midpint - 1] + sorted_data[midpoint]) / 2
        else:
            return sorted_data[midpoint]
        
        
        