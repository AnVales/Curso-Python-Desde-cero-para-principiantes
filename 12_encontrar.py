numeros = [3, 5, 1, 2, 1]

max_num = numeros[0]
min_num = numeros[0]

for i in numeros:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
        
print(max_num, min_num)