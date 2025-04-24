def simulador_vendas_marketing():
    print("📈 Bem-vindo ao Simulador de Vendas para Estrategistas de Marketing!")

    # Entrada do valor já investido
    valor_investido = float(input("💰 Valor já investido em campanhas de marketing (em R$): "))
    print(f"\n📊 Cliente já investiu R$ {valor_investido:.2f} em campanhas anteriores.")

    # Tabela de serviços de marketing digital
    servicos = {
        "Campanha de Anúncios em Redes Sociais": {"preco": 1500.0, "margem": 0.40},
        "SEO e Otimização de Site": {"preco": 2000.0, "margem": 0.35},
        "Email Marketing": {"preco": 800.0, "margem": 0.50},
        "Consultoria de Marketing Digital": {"preco": 2500.0, "margem": 0.45},
        "Gestão de Mídias Sociais": {"preco": 1200.0, "margem": 0.30}
    }

    # Pacotes recomendados com foco em serviços de marketing
    pacotes = {
        "Pacote Inicial": {
            "itens": {"Campanha de Anúncios em Redes Sociais": 1, "Email Marketing": 1},
            "desconto": 0.10,
            "marketing": "Ideal para pequenas empresas começando no marketing digital"
        },
        "Pacote Avançado": {
            "itens": {"SEO e Otimização de Site": 1, "Gestão de Mídias Sociais": 1},
            "desconto": 0.15,
            "marketing": "Para empresas que buscam aumentar sua presença online"
        },
        "Pacote Completo": {
            "itens": {"Consultoria de Marketing Digital": 1, "Campanha de Anúncios em Redes Sociais": 2},
            "desconto": 0.20,
            "marketing": "Pacote completo para uma estratégia de marketing robusta"
        }
    }

    print("\n📦 Pacotes de Serviços de Marketing Disponíveis:")
    for nome, pacote in pacotes.items():
        total_sem_desconto = sum(servicos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        desconto = pacote["desconto"]
        total_com_desconto = total_sem_desconto * (1 - desconto)
        print(f"\n🔹 {nome} - {pacote['marketing']}")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {servicos[item]['preco']:.2f} cada)")
        print(f"💸 Valor sem desconto: R$ {total_sem_desconto:.2f}")
        print(f"✅ Desconto aplicado: {int(desconto * 100)}%")
        print(f"🎯 Valor final: R$ {total_com_desconto:.2f}")
        print("🔥 Promoção válida somente nesta semana!\n")

    # Estratégia de marketing adicional (cross-sell)
    print("💡 Estratégia de Cross-Sell:")
    print("➡️ Ao adquirir qualquer pacote, ofereça um eBook de Marketing Digital por apenas R$ 29,90 (preço normal: R$ 49,90)!")
    print("📢 Gatilho de urgência: “Válido apenas para os 10 primeiros pedidos do mês!”")

    # Simulando escolha do cliente
    escolha = input("\n🛍️ Qual pacote o cliente escolheu? (Pacote Inicial, Pacote Avançado, Pacote Completo): ").strip().title()

    if escolha in pacotes:
        pacote = pacotes[escolha]
        desconto = pacote["desconto"]
        total_sem_desconto = sum(servicos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        total_com_desconto = total_sem_desconto * (1 - desconto)

        print(f"\n✅ Cliente escolheu o pacote: {escolha}")
        print(f"🔎 Itens incluídos:")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {servicos[item]['preco']:.2f})")

        economia = total_sem_desconto - total_com_desconto
        print(f"💰 Economia total: R$ {economia:.2f}")
        print(f"💳 Valor a pagar: R$ {total_com_desconto:.2f}")
        print("\n🎉 Parabéns! Cliente garantiu um pacote de marketing eficaz!")
        print("📞 Reforce a recompra com acompanhamento pós-venda e ofertas exclusivas.")
    else:
        print("❌ Opção inválida. Por favor, selecione um dos pacotes disponíveis.")

if __name__ == "__main__":
    simulador_vendas_marketing()