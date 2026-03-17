numeros = [1,2,3,2,4,2,5]
pergunta = int(input("Digite o numero que deseja procurar"))
contador = 0

for n in numeros:
    if pergunta == n:
        contador += 1
        
if contador == 1:
    palavra = "vez"
else:
    palavra = "vezes"
        
print(f'{pergunta} aparece {contador} {palavra}')