numeros = [1, 4, 7, 8, 10, 13, 16]

numeros_pares = 0

for n in numeros:
    if n % 2 == 0:
        print(n)
        numeros_pares += 1
        
print(numeros_pares)