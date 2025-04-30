def simulador_projetos_arquitetura():
    print("🏛️ Bem-vindo ao Simulador Estratégico de Projetos de Arquitetura!")

    # Problemas comuns e complexos
    problemas = {
        "Medidas Incorretas": "Solução: Uso de laser scanner e dupla conferência em campo. Ofereça medição gratuita na primeira visita.",
        "Falta de Criatividade": "Solução: Apresente moodboards digitais e visitas virtuais em 3D. Inclua brainstorming colaborativo com o cliente.",
        "Orçamento Limitado": "Solução: Proponha fases de execução e materiais alternativos. Mostre simulações de custo-benefício.",
        "Aprovação em Condomínio/Prefeitura": "Solução: Inclua assessoria completa de documentação e acompanhamento de aprovação.",
        "Dificuldade em Visualizar o Projeto": "Solução: Ofereça tour virtual 360º e maquete eletrônica grátis para projetos acima de R$ 50 mil.",
        "Prazo Apertado": "Solução: Apresente cronograma detalhado e equipe de parceiros para acelerar etapas críticas."
    }

    print("\n🔎 Principais problemas enfrentados por arquitetos e soluções estratégicas:")
    for problema, solucao in problemas.items():
        print(f"• {problema}: {solucao}")

    # Pacotes de projetos com diferenciais e estratégias de marketing
    pacotes = {
        "Essencial": {
            "itens": ["Planta baixa otimizada", "Consultoria de medidas", "Sugestão de layout inteligente"],
            "desconto": 0.05,
            "marketing": "Ideal para quem quer transformar ambientes sem gastar muito"
        },
        "Premium": {
            "itens": ["Projeto 3D completo", "Moodboard personalizado", "Acompanhamento de aprovação", "Tour virtual"],
            "desconto": 0.12,
            "marketing": "Mais vendido! Visualização total antes da obra e suporte completo"
        },
        "Signature": {
            "itens": ["Projeto autoral exclusivo", "Maquete eletrônica", "Consultoria de iluminação", "Gestão de obra", "Brinde surpresa"],
            "desconto": 0.18,
            "marketing": "Para clientes exigentes que querem exclusividade e inovação"
        }
    }

    precos_base = {
        "Essencial": 8000.0,
        "Premium": 18000.0,
        "Signature": 35000.0
    }

    print("\n📦 Pacotes de Projeto com Estratégia de Valor:")
    for nome, pacote in pacotes.items():
        preco = precos_base[nome]
        desconto = pacote["desconto"]
        preco_final = preco * (1 - desconto)
        print(f"\n🔹 {nome} - {pacote['marketing']}")
        print("  Inclui:")
        for item in pacote["itens"]:
            print(f"    - {item}")
        print(f"💸 Valor sem desconto: R$ {preco:.2f}")
        print(f"✅ Desconto aplicado: {int(desconto*100)}%")
        print(f"🎯 Valor final: R$ {preco_final:.2f}")
        print("🔥 Condição especial para fechar este mês!\n")

    # Estratégia de marketing adicional (cross-sell e gatilhos)
    print("💡 Estratégias para fechar mais projetos:")
    print("➡️ Fechando qualquer pacote, ganhe consultoria de decoração online grátis (valor de mercado: R$ 1.200,00)!")
    print("➡️ Indique um amigo e ambos ganham upgrade para tour virtual 360º.")
    print("📢 Gatilho de urgência: “Válido para os 10 primeiros contratos do mês!”")
    print("💬 Dica: Mostre portfólio de projetos anteriores e depoimentos de clientes satisfeitos.")

    # Simulando escolha do cliente
    escolha = input("\n🏠 Qual pacote o cliente escolheu? (Essencial, Premium, Signature): ").strip().title()

    if escolha in pacotes:
        pacote = pacotes[escolha]
        preco = precos_base[escolha]
        desconto = pacote["desconto"]
        preco_final = preco * (1 - desconto)
        economia = preco - preco_final

        print(f"\n✅ Cliente escolheu o pacote: {escolha}")
        print("🔎 Itens incluídos:")
        for item in pacote["itens"]:
            print(f"  - {item}")
        print(f"💰 Economia total: R$ {economia:.2f}")
        print(f"💳 Valor a pagar: R$ {preco_final:.2f}")
        print("\n🎉 Parabéns! Cliente garantiu um projeto de alto valor e diferencial.")
        print("📞 Reforce o pós-venda com acompanhamento, brindes e feedbacks para gerar novas indicações.")
    else:
        print("❌ Opção inválida. Por favor, selecione um dos pacotes disponíveis.")

if __name__ == "__main__":
    simulador_projetos_arquitetura()