archivo = open('prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close

archivo = open('prueba.txt', 'w')
archivo.write('Hola mundo\n')
archivo.close

archivo = open('prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close

with open('prueba.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
    
with open('prueba.txt', 'w') as archivo:
    archivo.write('Adios\n')
    print(contenido)
    
with open('prueba.txt', 'a') as archivo:
    archivo.write('Hola2')