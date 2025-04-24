def simulador_promocoes():
    print("Bem-vindo ao Simulador de Promoções para Fisioterapia!")
    
    # Entrada do valor já gasto pelo cliente
    valor_gasto = float(input("Digite o valor já gasto pelo cliente (em R$): "))
    print(f"\nO cliente já gastou R$ {valor_gasto:.2f}.")

    # Preço padrão por sessão
    preco_sessao = float(input("Digite o preço padrão por sessão (em R$): "))
    
    # Ofertas de desconto
    descontos = {
        "Bronze": 0.05,  # 5% de desconto
        "Prata": 0.10,   # 10% de desconto
        "Ouro": 0.20     # 20% de desconto
    }

    # Número de sessões por pacote
    sessoes_por_pacote = {
        "Bronze": 5,
        "Prata": 10,
        "Ouro": 20
    }

    print("\nOfertas disponíveis:")
    for pacote, desconto in descontos.items():
        num_sessoes = sessoes_por_pacote[pacote]
        valor_total_sem_desconto = preco_sessao * num_sessoes
        valor_com_desconto = valor_total_sem_desconto * (1 - desconto)
        print(f"- Pacote {pacote} ({num_sessoes} sessões): R$ {valor_com_desconto:.2f} (Desconto de {int(desconto * 100)}%)")

    # Simulação de escolha do cliente
    print("\nSimule a escolha do cliente:")
    escolha = input("Digite 'Bronze', 'Prata' ou 'Ouro' para selecionar o pacote: ").strip().capitalize()

    if escolha in descontos:
        num_sessoes = sessoes_por_pacote[escolha]
        desconto = descontos[escolha]
        valor_total_sem_desconto = preco_sessao * num_sessoes
        valor_com_desconto = valor_total_sem_desconto * (1 - desconto)

        print(f"\nVocê escolheu o Pacote {escolha}.")
        print(f"Número de sessões: {num_sessoes}")
        print(f"Valor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
        print(f"Desconto aplicado: {int(desconto * 100)}%")
        print(f"Valor final com desconto: R$ {valor_com_desconto:.2f}")
        print("\n💡 Dica: Mostre ao cliente como ele economiza e ganha mais sessões pelo mesmo valor!")
    else:
        print("\nOpção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    simulador_promocoes()