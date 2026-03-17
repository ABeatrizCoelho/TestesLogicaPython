senha_correta = "python123"

for i in range(3):
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso permitido")
        break
else:
    print("Acesso bloqueado")