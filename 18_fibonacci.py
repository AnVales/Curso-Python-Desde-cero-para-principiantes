def secuencia_fibonacci(n):
    
    lista_fib = []
    
    if n == 1:
        lista_fib.append(0)
    elif n == 2:
        lista_fib = [0, 1]
    elif n > 2:
        lista_fib = [0, 1]
        i = 2
        while i < n:
            lista_fib.append(lista_fib[-1]+lista_fib[-2])
            i += 1
    
    return lista_fib

sol = secuencia_fibonacci(4)
print(sol)