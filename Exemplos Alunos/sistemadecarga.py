def simulador_carga_carros():
    print("=" * 70)
    print("🚛 BEM-VINDO AO SIMULADOR DE CARGA E LOGÍSTICA PARA CLIENTES 🚛")
    print("=" * 70)

    # Entrada básica
    valor_unitario = float(input("\n💰 Valor unitário de cada carro (R$): "))
    quantidade = int(input("🚗 Quantos carros serão transportados? "))
    valor_total_carga = valor_unitario * quantidade

    print(f"\n📦 Valor total da carga: R$ {valor_total_carga:.2f}")

    # Locais de entrega e suas taxas
    locais_entrega = {
        "São Paulo": 1200.00,
        "Rio de Janeiro": 1500.00,
        "Belo Horizonte": 1100.00,
        "Porto Alegre": 1800.00,
        "Salvador": 1700.00
    }

    print("\n🗺️ LOCAIS DISPONÍVEIS PARA ENTREGA:")
    for local, taxa in locais_entrega.items():
        print(f"📍 {local:<15} - R$ {taxa:.2f}")

    locais_selecionados = input("\n✏️ Digite os locais de entrega separados por vírgula: ").split(",")
    total_entrega = 0

    print("\n🚚 RESUMO DAS ENTREGAS:")
    for local in locais_selecionados:
        local = local.strip()
        if local in locais_entrega:
            taxa = locais_entrega[local]
            total_entrega += taxa
            print(f"✅ {local}: R$ {taxa:.2f}")
        else:
            print(f"⚠️ Local '{local}' não encontrado.")

    # Seguro opcional
    print("\n🔒 BENEFÍCIO OPCIONAL: Seguro Total por R$ 500.00")
    seguro = input("Deseja adicionar seguro? (s/n): ").lower()
    valor_seguro = 500.00 if seguro == "s" else 0.00

    # SELEÇÃO DE PACOTE
    print("\n🎁 PACOTES CORPORATIVOS DISPONÍVEIS:")
    pacotes = {
        "Bronze": {"desconto_entrega": 0.00, "frete_gratis": [], "prioridade": False},
        "Prata": {"desconto_entrega": 0.10, "frete_gratis": ["São Paulo"], "prioridade": True},
        "Ouro": {"desconto_entrega": 0.15, "frete_gratis": ["São Paulo", "Rio de Janeiro"], "prioridade": True},
        "Platina": {"desconto_entrega": 0.20, "frete_gratis": list(locais_entrega.keys()), "prioridade": True}
    }

    for nome, dados in pacotes.items():
        print(f"🌟 {nome} | Desconto entrega: {int(dados['desconto_entrega']*100)}% | Frete grátis: {', '.join(dados['frete_gratis']) or 'Nenhum'}")

    pacote_escolhido = input("\n📦 Escolha um pacote (Bronze, Prata, Ouro, Platina): ").strip().capitalize()
    if pacote_escolhido not in pacotes:
        print("❌ Pacote inválido, usaremos o padrão Bronze.")
        pacote_escolhido = "Bronze"

    pacote = pacotes[pacote_escolhido]
    desconto = pacote["desconto_entrega"]
    frete_gratis = pacote["frete_gratis"]

    # Cálculo de taxas de entrega com frete grátis
    total_entrega_final = 0
    for local in locais_selecionados:
        local = local.strip()
        if local in locais_entrega and local not in frete_gratis:
            taxa = locais_entrega[local]
            total_entrega_final += taxa

    valor_desconto = total_entrega_final * desconto
    total_entrega_final -= valor_desconto

    # Valor final
    valor_total_final = valor_total_carga + total_entrega_final + valor_seguro

    print("\n💼 RESUMO FINAL")
    print("-" * 70)
    print(f"📘 Pacote selecionado: {pacote_escolhido}")
    print(f"🚗 Valor da carga ({quantidade} carro(s)):        R$ {valor_total_carga:.2f}")
    print(f"🚚 Taxas de entrega (com frete grátis e desconto): R$ {total_entrega_final:.2f}")
    print(f"🔐 Seguro:                                        R$ {valor_seguro:.2f}")
    print(f"🎯 TOTAL GERAL:                                   R$ {valor_total_final:.2f}")
    print("-" * 70)

    # Estratégia de fechamento
    print("\n🤝 PROPOSTA DE PARCERIA:")
    print("Estamos abertos a firmar parcerias com empresas que movimentam grandes volumes.")
    print("✅ Condições exclusivas para contratos mensais e anuais.")
    print("✅ Atendimento dedicado e consultoria logística gratuita.")
    print("✅ Sistema de rastreamento incluso.")
    print("\n📞 Entre em contato para agendar uma reunião ou solicite um orçamento personalizado.")
    print("📧 Email: comercial@logitechbr.com | 📱 WhatsApp: (11) 99999-9999")
    print("💡 Juntos, podemos acelerar seus negócios com eficiência e economia!")

# Executa o programa
if __name__ == "__main__":
    simulador_carga_carros()
