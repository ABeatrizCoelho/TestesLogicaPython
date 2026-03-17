palavra = input("Digite uma paravra: ")
vogais = 0

for x in palavra:
    print(x)
    if x in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
        
print(vogais)