def simulador_promocoes():
    print("Bem-vindo ao Simulador de Promoções para Audiovisual!")
    
    # Entrada do valor já gasto pelo cliente
    valor_gasto = float(input("Digite o valor já gasto pelo cliente (em R$): "))
    print(f"\nO cliente já gastou R$ {valor_gasto:.2f}.")

    # Preço padrão por serviço de gravação
    preco_gravacao = float(input("Digite o preço padrão por serviço de gravação (em R$): "))
    
    # Preço padrão por serviço de edição
    preco_edicao = float(input("Digite o preço padrão por serviço de edição (em R$): "))
    
    # Ofertas de desconto para pacotes de serviços
    descontos = {
        "Bronze": 0.05,  # 5% de desconto
        "Prata": 0.10,   # 10% de desconto
        "Ouro": 0.20     # 20% de desconto
    }

    # Número de serviços por pacote
    servicos_por_pacote = {
        "Bronze": {"gravacao": 3, "edicao": 2},
        "Prata": {"gravacao": 5, "edicao": 4},
        "Ouro": {"gravacao": 8, "edicao": 6}
    }

    print("\nOfertas disponíveis:")
    for pacote, desconto in descontos.items():
        servicos = servicos_por_pacote[pacote]
        valor_total_gravacao = preco_gravacao * servicos["gravacao"]
        valor_total_edicao = preco_edicao * servicos["edicao"]
        valor_total_sem_desconto = valor_total_gravacao + valor_total_edicao
        valor_com_desconto = valor_total_sem_desconto * (1 - desconto)
        print(f"- Pacote {pacote} ({servicos['gravacao']} gravações e {servicos['edicao']} edições): R$ {valor_com_desconto:.2f} (Desconto de {int(desconto * 100)}%)")

    # Simulação de escolha do cliente
    print("\nSimule a escolha do cliente:")
    escolha = input("Digite 'Bronze', 'Prata' ou 'Ouro' para selecionar o pacote: ").strip().capitalize()

    if escolha in descontos:
        servicos = servicos_por_pacote[escolha]
        desconto = descontos[escolha]
        valor_total_gravacao = preco_gravacao * servicos["gravacao"]
        valor_total_edicao = preco_edicao * servicos["edicao"]
        valor_total_sem_desconto = valor_total_gravacao + valor_total_edicao
        valor_com_desconto = valor_total_sem_desconto * (1 - desconto)

        print(f"\nVocê escolheu o Pacote {escolha}.")
        print(f"Número de gravações: {servicos['gravacao']}")
        print(f"Número de edições: {servicos['edicao']}")
        print(f"Valor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
        print(f"Desconto aplicado: {int(desconto * 100)}%")
        print(f"Valor final com desconto: R$ {valor_com_desconto:.2f}")
        print("\n💡 Dica: Ofereça pacotes completos para aumentar o valor agregado do serviço e fidelizar seus clientes!")
    else:
        print("\nOpção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    simulador_promocoes()
