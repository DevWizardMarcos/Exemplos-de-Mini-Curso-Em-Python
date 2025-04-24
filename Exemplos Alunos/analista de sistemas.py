def simulador_servicos_analista_dados():
    print("📊 Bem-vindo ao Simulador de Serviços para Analistas de Dados Iniciantes!")

    # Entrada do valor já investido em cursos/capacitação
    valor_investido = float(input("💰 Quanto você já investiu em cursos/capacitação (R$)? "))
    print(f"\n🎓 Você já investiu R$ {valor_investido:.2f} em sua formação.")

    # Tabela de serviços comuns e margens de lucro sugeridas
    servicos = {
        "Dashboard de Vendas (Power BI/Excel)": {"preco": 600.0, "margem": 0.60},
        "Limpeza e Organização de Dados": {"preco": 400.0, "margem": 0.55},
        "Análise de Perfil de Clientes": {"preco": 700.0, "margem": 0.65},
        "Automação de Relatórios": {"preco": 800.0, "margem": 0.70},
        "Treinamento Básico para Equipe": {"preco": 500.0, "margem": 0.50}
    }

    # Pacotes estratégicos para clientes reais
    pacotes = {
        "Essencial": {
            "itens": {"Dashboard de Vendas (Power BI/Excel)": 1, "Limpeza e Organização de Dados": 1},
            "desconto": 0.10,
            "marketing": "Ideal para pequenas empresas começarem a entender seus dados"
        },
        "Crescimento": {
            "itens": {"Dashboard de Vendas (Power BI/Excel)": 1, "Análise de Perfil de Clientes": 1, "Automação de Relatórios": 1},
            "desconto": 0.18,
            "marketing": "Mais vendido! Para empresas que querem crescer com decisões baseadas em dados"
        },
        "Premium": {
            "itens": {"Dashboard de Vendas (Power BI/Excel)": 1, "Análise de Perfil de Clientes": 1, "Automação de Relatórios": 1, "Treinamento Básico para Equipe": 1},
            "desconto": 0.25,
            "marketing": "Pacote completo para transformar a cultura de dados da empresa"
        }
    }

    print("\n📦 Pacotes de Serviços Estratégicos:")
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
        print("🔥 Promoção válida para os 10 primeiros clientes do mês!\n")

    # Estratégia de marketing adicional (cross-sell)
    print("💡 Estratégia de Cross-Sell:")
    print("➡️ Ao fechar qualquer pacote, ofereça uma consultoria de 1h para diagnóstico de oportunidades por apenas R$ 99,00 (preço normal: R$ 199,00)!")
    print("📢 Gatilho de urgência: “Válido apenas para contratos fechados nesta semana!”")

    # Simulando escolha do cliente
    escolha = input("\n🛍️ Qual pacote o cliente escolheu? (Essencial, Crescimento, Premium): ").strip().title()

    if escolha in pacotes:
        pacote = pacotes[escolha]
        desconto = pacote["desconto"]
        total_sem_desconto = sum(servicos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        total_com_desconto = total_sem_desconto * (1 - desconto)

        print(f"\n✅ Cliente escolheu o pacote: {escolha}")
        print(f"🔎 Serviços incluídos:")
        for item, qtd in pacote["itens"].items():
            print(f"  - {qtd}x {item} (R$ {servicos[item]['preco']:.2f})")

        economia = total_sem_desconto - total_com_desconto
        print(f"💰 Economia total para o cliente: R$ {economia:.2f}")
        print(f"💳 Valor a receber: R$ {total_com_desconto:.2f}")
        print("\n🎉 Parabéns! Você fechou um pacote estratégico e valorizou seu trabalho!")
        print("📞 Dica: Faça acompanhamento pós-venda e peça depoimentos para fortalecer sua reputação.")
    else:
        print("❌ Opção inválida. Por favor, selecione um dos pacotes disponíveis.")

if __name__ == "__main__":
    simulador_servicos_analista_dados()