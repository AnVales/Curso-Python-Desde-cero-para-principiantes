def generador_pares(limite):
    num = 0
    while num <= limite:
        yield num
        num += 2

# Usar el generador para crear un iterador de números pares
pares = generador_pares(10)

# Recorrer los números pares usando un iterador
for par in pares:
    print(par)