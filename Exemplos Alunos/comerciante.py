def simulador_venda_doces():
    print("=" * 60)
    print("🍬 BEM-VINDO AO SIMULADOR DE COMBOS DOCES DA DONA DELÍCIA 🍬")
    print("=" * 60)

    # Histórico de compras anteriores
    valor_gasto = float(input("\n💰 Digite quanto o cliente já gastou com doces (em R$): "))
    print(f"📊 Histórico: O cliente já investiu R$ {valor_gasto:.2f} em momentos doces e felizes!\n")

    preco_unitario = float(input("📌 Digite o preço médio de uma unidade de doce (em R$): "))

    # Combos promocionais
    combos = {
        "Mini": 0.05,
        "Festa": 0.15,
        "Premium": 0.30
    }

    doces_por_combo = {
        "Mini": 6,
        "Festa": 12,
        "Premium": 25
    }

    # Extras irresistíveis
    brindes_extras = {
        "Caixinha personalizada com nome": 15.00,
        "Mensagem surpresa especial": 10.00,
        "Cartão artesanal com tema da data": 12.00,
        "Mini pelúcia do amor": 25.00
    }

    print("\n🎁 COMBOS DISPONÍVEIS:")
    print("-" * 60)
    for nome, desconto in combos.items():
        qtd = doces_por_combo[nome]
        valor_bruto = preco_unitario * qtd
        valor_final = valor_bruto * (1 - desconto)
        print(f"🍭 Combo {nome:<10} | Doces: {qtd:<2} | "
              f"De: R$ {valor_bruto:6.2f} 👉 Por: R$ {valor_final:6.2f} (🔻 {int(desconto * 100)}% OFF)")

    print("\n✨ BRINDES EXTRAS (GATILHOS DE VALOR E EMOÇÃO):")
    print("-" * 60)
    for brinde, valor in brindes_extras.items():
        desconto = 0.10 if valor > 20 else 0.05
        valor_descontado = valor * (1 - desconto)
        print(f"🎀 {brinde:<35} 👉 De: R$ {valor:.2f} | Por: R$ {valor_descontado:.2f} ({int(desconto*100)}% OFF)")

    print("\n🎯 QUAL O OBJETIVO DA COMPRA DO CLIENTE?")
    desejos = {
        "1": "Presente romântico",
        "2": "Festa infantil",
        "3": "Aniversário de amigo",
        "4": "Surpresa de desculpas",
        "5": "Autoestima / mimo pessoal"
    }

    for k, v in desejos.items():
        print(f"{k}. {v}")

    selecionadas = input("Digite os números das motivações (ex: 1,3,5): ").split(",")

    print("\n💞 DESEJOS IDENTIFICADOS:")
    for cod in selecionadas:
        desc = desejos.get(cod.strip())
        if desc:
            print(f"✅ {desc}")

    escolha = input("\n🍫 Escolha um combo (Mini, Festa, Premium): ").strip().capitalize()

    if escolha in combos:
        qtd = doces_por_combo[escolha]
        desconto = combos[escolha]
        valor_bruto = preco_unitario * qtd
        valor_final = valor_bruto * (1 - desconto)

        print("\n💼 RESUMO DO COMBO ESCOLHIDO")
        print("-" * 60)
        print(f"🍭 Combo: {escolha}")
        print(f"📦 Quantidade de doces: {qtd}")
        print(f"💵 Valor original: R$ {valor_bruto:.2f}")
        print(f"💸 Desconto aplicado: {int(desconto * 100)}%")
        print(f"✅ Valor final: R$ {valor_final:.2f}")

        # Marketing emocional e persuasivo
        print("\n💬 ESTRATÉGIA DE VENDA ENCANTADORA")
        print("-" * 60)
        print("💡 Use frases como:")
        print("✔ 'Transforme o dia de alguém em um momento doce!'")
        print("✔ 'Com esse combo, você vai arrancar sorrisos ❤️'")
        print("✔ 'Mais do que doces: experiências inesquecíveis!'")
        print("✔ 'Garanta já o mimo perfeito e surpreenda de verdade!'")

        print("\n🎀 Dica: Combine com o brinde 'Caixinha personalizada' para transformar o presente em algo único!")

    else:
        print("❌ Opção inválida. Por favor, escolha um combo válido.")

    print("\n🧠 Dica final: Ofereça combos temáticos em datas especiais (Dia das Mães, Namorados, Natal) com descontos progressivos e crie urgência com frases como 'Últimas unidades!'")

# Executa o programa
if __name__ == "__main__":
    simulador_venda_doces()
