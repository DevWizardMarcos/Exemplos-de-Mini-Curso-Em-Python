convidados = []

print("Cadastro de convidados. Digite 'sair' para encerrar.")

while True:
    nome = input("Digite o nome do convidado: ")
    if nome.lower() == "sair":
        break
    if nome in convidados:
        print(f"{nome} já está na lista.")
    else:
        convidados.append(nome)
        print(f"{nome} foi adicionado à lista.")

print("\nLista final de convidados:")
for convidado in convidados:
    print(f"- {convidado}")