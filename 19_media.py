def calcular_media(lista):
    suma = 0
    
    for i in lista:
        suma += i
    
    return suma/(len(lista))


lista1 = [1,2,3]
resultado = calcular_media(lista1)
print(resultado)
        
    
    