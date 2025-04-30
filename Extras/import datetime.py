import datetime

treinadores = []
exercicios = []
planos = []

def cadastrar_treinador():
    nome = input("Nome do treinador: ")
    cref = input("CREF: ")
    treinadores.append({"nome": nome, "cref": cref})
    print(f"Treinador {nome} cadastrado com sucesso!\n")

def cadastrar_exercicio():
    nome = input("Nome do exercício: ")
    grupo = input("Grupo muscular: ")
    exercicios.append({"nome": nome, "grupo": grupo})
    print(f"Exercício {nome} cadastrado para o grupo {grupo}!\n")

def avaliacao_fisica():
    print("=== Avaliação Física ===")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    idade = int(input("Idade: "))
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}")
    return {"peso": peso, "altura": altura, "idade": idade, "imc": imc}

def criar_plano():
    cliente = input("Nome do cliente: ")
    treinador = input("Nome do treinador responsável: ")
    data_inicio = input("Data de início (dd/mm/aaaa): ")
    data_fim = input("Data de término (dd/mm/aaaa): ")
    avaliacao = avaliacao_fisica()
    plano = {
        "cliente": cliente,
        "treinador": treinador,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "avaliacao": avaliacao,
        "treinos": []
    }
    planos.append(plano)
    print(f"Plano de treino criado para {cliente}!\n")

def adicionar_treino():
    if not planos:
        print("Nenhum plano cadastrado.\n")
        return
    cliente = input("Para qual cliente deseja adicionar treino? ")
    plano = next((p for p in planos if p["cliente"] == cliente), None)
    if not plano:
        print("Plano não encontrado.\n")
        return
    print("Adicione exercícios ao treino:")
    treino = []
    while True:
        nome_exercicio = input("Nome do exercício (ou 'fim' para terminar): ")
        if nome_exercicio.lower() == "fim":
            break
        carga = input("Carga (kg): ")
        series = input("Séries: ")
        repeticoes = input("Repetições: ")
        treino.append({
            "exercicio": nome_exercicio,
            "carga": carga,
            "series": series,
            "repeticoes": repeticoes
        })
    plano["treinos"].append({
        "data": datetime.date.today().isoformat(),
        "exercicios": treino
    })
    print("Treino adicionado ao plano!\n")

def consultar_planos():
    for plano in planos:
        print(f"\nCliente: {plano['cliente']}")
        print(f"Treinador: {plano['treinador']}")
        print(f"Período: {plano['data_inicio']} a {plano['data_fim']}")
        print(f"Avaliação Física: Peso {plano['avaliacao']['peso']}kg, Altura {plano['avaliacao']['altura']}m, IMC {plano['avaliacao']['imc']:.2f}")
        print("Treinos:")
        for treino in plano["treinos"]:
            print(f"  Data: {treino['data']}")
            for ex in treino["exercicios"]:
                print(f"    {ex['exercicio']}: {ex['carga']}kg, {ex['series']}x{ex['repeticoes']}")

def menu():
    while True:
        print("\n=== Sistema de Consultoria Fitness ===")
        print("1. Cadastrar treinador")
        print("2. Cadastrar exercício")
        print("3. Criar plano de treino")
        print("4. Adicionar treino ao plano")
        print("5. Consultar planos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_treinador()
        elif opcao == "2":
            cadastrar_exercicio()
        elif opcao == "3":
            criar_plano()
        elif opcao == "4":
            adicionar_treino()
        elif opcao == "5":
            consultar_planos()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()