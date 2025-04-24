def simulador_vendas_engenheiro_civil():
    print("🏗️ Bem-vindo ao Simulador de Vendas para Engenheiros Civis!")

    # Entrada do valor já gasto
    valor_gasto = float(input("💰 Valor já gasto pelo cliente em materiais de construção (em R$): "))
    print(f"\n📊 Cliente já investiu R$ {valor_gasto:.2f} em materiais anteriormente.")

    # Tabela de materiais com margens de lucro e preço unitário
    materiais = {
        "Cimento": {"preco": 25.0, "margem": 0.20},
        "Areia": {"preco": 15.0, "margem": 0.15},
        "Brita": {"preco": 20.0, "margem": 0.25},
        "Tijolo": {"preco": 0.80, "margem": 0.10},
        "Aço": {"preco": 5.0, "margem": 0.30}
    }

    # Pacotes recomendados com foco em materiais de construção
    pacotes = {
        "Pacote Básico": {
            "itens": {"Cimento": 10, "Areia": 5},
            "desconto": 0.05,
            "marketing": "Ideal para pequenas obras e reformas"
        },
        "Pacote Completo": {
            "itens": {"Cimento": 20, "Brita": 10, "Aço": 5},
            "desconto": 0.10,
            "marketing": "Perfeito para grandes construções"
        },
        "Pacote Premium": {
            "itens": {"Cimento": 30, "Tijolo": 100, "Aço": 10},
            "desconto": 0.15,
            "marketing": "Pacote completo para projetos de alta demanda"
        }
    }

    print("\n📦 Pacotes de Materiais de Construção:")
    for nome, pacote in pacotes.items():
        total_sem_desconto = sum(materiais[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        desconto = pacote["desconto"]
        total_com_desconto = total_sem_desconto * (1 - desconto)
        print(f"\n🔹 {nome} - {pacote['marketing']}")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {materiais[item]['preco']:.2f} cada)")
        print(f"💸 Valor sem desconto: R$ {total_sem_desconto:.2f}")
        print(f"✅ Desconto aplicado: {int(desconto * 100)}%")
        print(f"🎯 Valor final: R$ {total_com_desconto:.2f}")
        print("🔥 Promoção válida somente nesta semana!\n")

    # Estratégia de marketing adicional (cross-sell)
    print("💡 Estratégia de Cross-Sell:")
    print("➡️ Ao adquirir qualquer pacote, ofereça o serviço de consultoria por apenas R$ 199,90 (preço normal: R$ 299,90)!")
    print("📢 Gatilho de urgência: “Válido apenas para os 10 primeiros contratos do mês!”")

    # Simulando escolha do cliente
    escolha = input("\n🛍️ Qual pacote o cliente escolheu? (Pacote Básico, Pacote Completo, Pacote Premium): ").strip().title()

    if escolha in pacotes:
        pacote = pacotes[escolha]
        desconto = pacote["desconto"]
        total_sem_desconto = sum(materiais[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        total_com_desconto = total_sem_desconto * (1 - desconto)

        print(f"\n✅ Cliente escolheu o pacote: {escolha}")
        print(f"🔎 Itens incluídos:")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {materiais[item]['preco']:.2f})")

        economia = total_sem_desconto - total_com_desconto
        print(f"💰 Economia total: R$ {economia:.2f}")
        print(f"💳 Valor a pagar: R$ {total_com_desconto:.2f}")
        print("\n🎉 Parabéns! Cliente garantiu um pacote de materiais de construção!")
        print("📞 Reforce a recompra com acompanhamento pós-venda e ofertas especiais.")
    else:
        print("❌ Opção inválida. Por favor, selecione um dos pacotes disponíveis.")

if __name__ == "__main__":
    simulador_vendas_engenheiro_civil()