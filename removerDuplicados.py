numeros = [1,2,3,2,4,5,3,6]

lista_nova = []

for n in numeros:
    if n not in lista_nova:
        lista_nova.append(n)
        
print(lista_nova)