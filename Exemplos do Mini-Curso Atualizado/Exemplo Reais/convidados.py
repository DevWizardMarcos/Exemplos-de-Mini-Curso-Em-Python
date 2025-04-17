convidados = ["Ana", "Carlos", "Mariana", "João", "Fernanda"]

nome = input("Digite seu nome para verificar a presença: ")

if nome in convidados:
    print(f"Bem-vindo(a), {nome}! Você está na lista de convidados.")
else:
    print("Desculpe, seu nome não está na lista.")
