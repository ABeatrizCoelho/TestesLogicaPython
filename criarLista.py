resposta = 1
lista = []

while(True):
    resposta = (int(input("Digite um numero: ")))
    if resposta == 0 :
        break
    lista.append(resposta)
    
print(lista)