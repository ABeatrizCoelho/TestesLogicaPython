distancia_a_percorrer = int(input("Digite quantos km precisa percorrer para chegar ao seu destino: "))
velocidade_media = int(input("Qual a velocidade média que deseja percorrer essa distância? "))
tempo = distancia_a_percorrer / velocidade_media
print("Voce vai percorrer a distancia desejada em %.2f horas" % tempo)