numeros = [1,2,2,3,4,4,5,1]

sem_duplicados = []

for n in numeros:
    if n not in sem_duplicados:
        sem_duplicados.append(n)

print(sem_duplicados)