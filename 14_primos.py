import math as mth

def es_primo(num):
    if num<2:
        return False
    for i in range(2, int(mth.sqrt(num))+1):
        if i % num == 0:
            return False
    return True


solucion = es_primo(5) 
print(solucion)  
        
        