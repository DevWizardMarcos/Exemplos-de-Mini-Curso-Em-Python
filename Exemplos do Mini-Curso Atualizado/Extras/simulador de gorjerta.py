def simulador_gorjetas():
    print("Bem-vindo ao Simulador de Gorjetas!")
    
    # Entrada do valor da conta
    valor_conta = float(input("Digite o valor da sua conta (em R$): "))
    
    # Percentuais de gorjeta baseados na qualidade do serviço
    gorjetas = {
        "Ótimo": 0.20,  # 20%
        "Bom": 0.15,    # 15%
        "Ruim": 0.10    # 10%
    }
    
    print("\nRecomendações de gorjeta:")
    for qualidade, percentual in gorjetas.items():
        valor_gorjeta = valor_conta * percentual
        valor_total = valor_conta + valor_gorjeta
        print(f"- {qualidade}: R$ {valor_gorjeta:.2f} (Total: R$ {valor_total:.2f})")
    
    print("\nEscolha a qualidade do serviço para calcular o valor final:")
    escolha = input("Digite 'Ótimo', 'Bom' ou 'Ruim': ").strip().capitalize()
    
    if escolha in gorjetas:
        valor_gorjeta = valor_conta * gorjetas[escolha]
        valor_total = valor_conta + valor_gorjeta
        print(f"\nVocê escolheu '{escolha}'.")
        print(f"Gorjeta: R$ {valor_gorjeta:.2f}")
        print(f"Valor final com gorjeta: R$ {valor_total:.2f}")
    else:
        print("\nOpção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    simulador_gorjetas()