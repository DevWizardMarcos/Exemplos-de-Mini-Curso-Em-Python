def simulador_vendas_odontologia_estrategico():
    print("🦷 Bem-vindo ao Simulador de Vendas Estratégicas para Itens Odontológicos!")

    # Entrada do valor já gasto
    valor_gasto = float(input("💰 Valor já gasto pelo cliente com materiais (em R$): "))
    print(f"\n📊 Cliente já investiu R$ {valor_gasto:.2f} em compras anteriores.")

    # Tabela de produtos com margens de lucro e preço unitário
    produtos = {
        "Luva de Procedimento": {"preco": 30.0, "margem": 0.30},
        "Resina Composta Premium": {"preco": 120.0, "margem": 0.45},
        "Broca Diamantada": {"preco": 15.0, "margem": 0.50},
        "Alginato de Moldagem": {"preco": 35.0, "margem": 0.40},
        "Clareador Dental Kit": {"preco": 200.0, "margem": 0.60}
    }

    # Pacotes recomendados com foco em produtos de maior margem
    pacotes = {
        "Smart Start": {
            "itens": {"Broca Diamantada": 10, "Luva de Procedimento": 5},
            "desconto": 0.10,
            "marketing": "Ideal para clínicas em início de expansão"
        },
        "Performance Pro": {
            "itens": {"Resina Composta Premium": 5, "Alginato de Moldagem": 5},
            "desconto": 0.15,
            "marketing": "Mais vendida! Excelente para consultórios de alto desempenho"
        },
        "Elite Plus": {
            "itens": {"Clareador Dental Kit": 5, "Broca Diamantada": 10},
            "desconto": 0.25,
            "marketing": "Pacote exclusivo com os itens de maior margem e entrega expressa"
        }
    }

    print("\n📦 Pacotes Promocionais com Estratégia de Margem Alta:")
    for nome, pacote in pacotes.items():
        total_sem_desconto = sum(produtos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        desconto = pacote["desconto"]
        total_com_desconto = total_sem_desconto * (1 - desconto)
        print(f"\n🔹 {nome} - {pacote['marketing']}")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {produtos[item]['preco']:.2f} cada)")
        print(f"💸 Valor sem desconto: R$ {total_sem_desconto:.2f}")
        print(f"✅ Desconto aplicado: {int(desconto * 100)}%")
        print(f"🎯 Valor final: R$ {total_com_desconto:.2f}")
        print("🔥 Promoção válida somente nesta semana!\n")

    # Estratégia de marketing adicional (cross-sell)
    print("💡 Estratégia de Cross-Sell:")
    print("➡️ Ao adquirir qualquer pacote, ofereça o Kit de Espelho e Sonda por apenas R$ 39,90 (preço normal: R$ 59,90)!")
    print("📢 Gatilho de urgência: “Válido apenas para os 20 primeiros pedidos do mês!”")

    # Simulando escolha do cliente
    escolha = input("\n🛍️ Qual pacote o cliente escolheu? (Smart Start, Performance Pro, Elite Plus): ").strip().title()

    if escolha in pacotes:
        pacote = pacotes[escolha]
        desconto = pacote["desconto"]
        total_sem_desconto = sum(produtos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        total_com_desconto = total_sem_desconto * (1 - desconto)

        print(f"\n✅ Cliente escolheu o pacote: {escolha}")
        print(f"🔎 Itens incluídos:")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {produtos[item]['preco']:.2f})")

        economia = total_sem_desconto - total_com_desconto
        print(f"💰 Economia total: R$ {economia:.2f}")
        print(f"💳 Valor a pagar: R$ {total_com_desconto:.2f}")
        print("\n🎉 Parabéns! Cliente garantiu um pacote de alto valor e alta performance!")
        print("📞 Reforce a recompra com acompanhamento pós-venda e brindes.")
    else:
        print("❌ Opção inválida. Por favor, selecione um dos pacotes disponíveis.")

if __name__ == "__main__":
    simulador_vendas_odontologia_estrategico()
