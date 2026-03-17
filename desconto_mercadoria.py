preco_mercadoria = float(input("Digite o valor da mercadoria: "))
porcentagem_desconto = float(input("Digite o valor do desconto: "))

desconto = preco_mercadoria * porcentagem_desconto / 100

valorfinal = preco_mercadoria - desconto

print("%0f" % valorfinal)