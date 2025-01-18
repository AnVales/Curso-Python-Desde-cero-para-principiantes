def valores(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio
    
lista = [1, 5, 3, 5, 6]
min, max, promedio = valores(lista)
print(min)
print(max)
print(promedio)