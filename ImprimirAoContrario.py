palavra = input("Digite uma palavra: ")

invertida = ""

for letra in palavra:
    invertida = letra + invertida

if (invertida == palavra):
    print("É um palídromo")
else:
    print('Não é um palindromo')