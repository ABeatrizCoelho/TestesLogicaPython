numero = int(input("Digite um valor: "))
maior = numero
menor = numero

for i in range(4):
    numero = int(input("Digite um valor: "))
    
    if numero > maior:
        maior = numero
        
    if numero < menor:
        menor = numero

print("Maior:", maior)
print("Menor:", menor)