def simulador_vendas_corretor_imobiliario():
    print("🏡 Bem-vindo ao Simulador de Vendas para Corretores Imobiliários!")

    # Entrada do valor já investido
    valor_investido = float(input("💰 Valor já investido pelo cliente em imóveis (em R$): "))
    print(f"\n📊 Cliente já investiu R$ {valor_investido:.2f} em imóveis anteriormente.")

    # Tabela de imóveis com preços e características
    imoveis = {
        "Apartamento 2 Quartos": {"preco": 250000.0, "caracteristicas": "Ideal para famílias pequenas"},
        "Casa 3 Quartos": {"preco": 450000.0, "caracteristicas": "Espaço amplo e quintal"},
        "Cobertura Duplex": {"preco": 800000.0, "caracteristicas": "Vista panorâmica e área de lazer"},
        "Sala Comercial": {"preco": 300000.0, "caracteristicas": "Localização central e alta visibilidade"},
        "Chácara": {"preco": 600000.0, "caracteristicas": "Perfeita para quem busca tranquilidade"}
    }

    # Pacotes recomendados com foco em imóveis de diferentes faixas de preço
    pacotes = [
        {
            "nome": "Início de Vida",
            "itens": {"Apartamento 2 Quartos": 1},
            "marketing": "Ideal para jovens casais e famílias em início de vida."
        },
        {
            "nome": "Espaço e Conforto",
            "itens": {"Casa 3 Quartos": 1, "Chácara": 1},
            "marketing": "Para quem busca espaço e conforto."
        },
        {
            "nome": "Investimento Comercial",
            "itens": {"Sala Comercial": 1, "Cobertura Duplex": 1},
            "marketing": "Pacote para investidores em imóveis comerciais."
        }
    ]

    print("\n🏠 Pacotes Imobiliários Recomendados:")
    for idx, pacote in enumerate(pacotes, 1):
        total = sum(imoveis[item]["preco"] for item in pacote["itens"])
        print(f"\n{idx}. 🔹 {pacote['nome']} - {pacote['marketing']}")
        for item in pacote["itens"]:
            print(f"  - {item} (R$ {imoveis[item]['preco']:.2f})")
        print(f"💸 Valor total: R$ {total:.2f}")

    # Estratégia de marketing adicional
    print("💡 Estratégia de Marketing: Ofereça uma consultoria gratuita para os primeiros 10 clientes!")
    print("📢 Gatilho de urgência: “Válido apenas para os 10 primeiros interessados do mês!”")

    # Simulando escolha do cliente
    escolha = input("\n🛍️ Qual pacote o cliente escolheu? (Digite 1, 2 ou 3): ").strip()

    if escolha in ["1", "2", "3"]:
        idx = int(escolha) - 1
        pacote = pacotes[idx]
        print(f"\n✅ Cliente escolheu o pacote: {pacote['nome']}")
        print(f"🔎 Itens incluídos:")
        for item in pacote["itens"]:
            print(f"  - {item} (R$ {imoveis[item]['preco']:.2f})")
        print("🎉 Parabéns! Cliente garantiu um pacote imobiliário de sucesso!")
    else:
        print("❌ Opção inválida. Por favor, selecione 1, 2 ou 3.")

if __name__ == "__main__":
    simulador_vendas_corretor_imobiliario()