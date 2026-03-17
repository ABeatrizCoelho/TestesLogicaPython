# ===============================
# REVISÃO PYTHON BÁSICO - ENTREVISTA
# ===============================

# -------------------------------
# 1. INPUT E OUTPUT
# -------------------------------

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Olá", nome)
print(f"Você tem {idade} anos")


# -------------------------------
# 2. IF / ELSE
# -------------------------------

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
elif numero == 0:
    print("Zero")
else:
    print("Número negativo")


# -------------------------------
# 3. PAR OU ÍMPAR
# -------------------------------

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")


# -------------------------------
# 4. FOR LOOP
# -------------------------------

for i in range(1, 11):
    print(i)


# -------------------------------
# 5. SOMA DE NÚMEROS
# -------------------------------

numeros = [5, 8, 3, 10]

soma = 0

for n in numeros:
    soma += n

print("Soma:", soma)


# -------------------------------
# 6. MAIOR NÚMERO DA LISTA
# -------------------------------

numeros = [4, 7, 1, 9, 3, 10]

maior = numeros[0]

for n in numeros:
    if n > maior:
        maior = n

print("Maior número:", maior)


# -------------------------------
# 7. CONTAR VOGAIS
# -------------------------------

palavra = input("Digite uma palavra: ")

vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        vogais += 1

print("Quantidade de vogais:", vogais)


# -------------------------------
# 8. TABUADA
# -------------------------------

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# -------------------------------
# 9. FIZZBUZZ
# -------------------------------

for i in range(1, 51):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)


# -------------------------------
# 10. VERIFICAR PALÍNDROMO
# -------------------------------

palavra = input("Digite uma palavra: ")

invertida = ""

for letra in palavra:
    invertida = letra + invertida

if palavra == invertida:
    print("É palíndromo")
else:
    print("Não é palíndromo")


# -------------------------------
# 11. NÚMERO PRIMO
# -------------------------------

numero = int(input("Digite um número: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("Número primo")
else:
    print("Não é primo")


# -------------------------------
# 12. REMOVER DUPLICADOS
# -------------------------------

numeros = [1,2,3,2,4,5,3,6]

lista_nova = []

for n in numeros:
    if n not in lista_nova:
        lista_nova.append(n)

print(lista_nova)


# -------------------------------
# 13. CONTAR OCORRÊNCIAS
# -------------------------------

numeros = [1,2,3,2,4,2,5]

buscar = int(input("Digite um número para buscar: "))

contador = 0

for n in numeros:
    if n == buscar:
        contador += 1

print(f"O número aparece {contador} vezes")


# -------------------------------
# 14. SENHA COM 3 TENTATIVAS
# -------------------------------

senha_correta = "python123"

for tentativa in range(3):

    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido")
        break

else:
    print("Acesso bloqueado")