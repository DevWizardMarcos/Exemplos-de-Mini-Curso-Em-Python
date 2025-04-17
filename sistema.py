def simulador_suporte_sistemas():
    print("=" * 60)
    print("🔧 BEM-VINDO AO SIMULADOR DE PLANOS DE SUPORTE TÉCNICO 🔧")
    print("=" * 60)

    # Entrada do valor já gasto pelo cliente com suporte anterior
    valor_gasto = float(input("\n💰 Digite o valor já gasto pelo cliente com suporte (em R$): "))
    print(f"📊 Histórico: O cliente já investiu R$ {valor_gasto:.2f} em suporte técnico.\n")

    # Preço padrão de atendimento técnico por ocorrência
    preco_ocorrencia = float(input("📌 Digite o preço padrão por ocorrência resolvida (em R$): "))

    # Planos principais com desconto
    planos = {
        "Básico": 0.05,
        "Intermediário": 0.15,
        "Premium": 0.30
    }

    atendimentos_por_plano = {
        "Básico": 5,
        "Intermediário": 10,
        "Premium": 20
    }

    # Pacotes adicionais de alto valor agregado
    pacotes_extras = {
        "Acompanhamento de Analista Dedicado": 1200.00,
        "Implementação de Banco de Dados Otimizado": 2200.00,
        "Treinamento para Equipe Técnica": 950.00,
        "Relatórios Mensais Inteligentes": 650.00
    }

    print("\n📦 PLANOS DE SUPORTE DISPONÍVEIS:")
    print("-" * 60)
    for nome, desconto in planos.items():
        qtd = atendimentos_por_plano[nome]
        valor_bruto = preco_ocorrencia * qtd
        valor_final = valor_bruto * (1 - desconto)
        print(f"📘 Plano {nome:<14} | Atendimentos: {qtd:<3} | "
              f"Valor: R$ {valor_final:7.2f} (🔻 {int(desconto * 100)}% OFF)")

    print("\n🧩 PACOTES EXTRAS RECOMENDADOS (ALTA MARGEM E VALOR):")
    print("-" * 60)
    for pacote, valor in pacotes_extras.items():
        desconto = 0.10 if valor > 1000 else 0.05  # Estratégia de margem maior
        valor_descontado = valor * (1 - desconto)
        print(f"🔧 {pacote:<40} 👉 De: R$ {valor:.2f} | Por: R$ {valor_descontado:.2f} ({int(desconto*100)}% de desconto)")

    # Identificação das dores
    print("\n😟 QUAIS SÃO AS PRINCIPAIS DORES DO CLIENTE?")
    dores = {
        "1": "Lentidão no sistema",
        "2": "Erros frequentes",
        "3": "Falta de atualizações",
        "4": "Suporte demorado",
        "5": "Falta de monitoramento preventivo"
    }

    for k, v in dores.items():
        print(f"{k}. {v}")

    selecionadas = input("Digite os números das dores identificadas (ex: 1,3,5): ").split(",")

    print("\n📌 DORES IDENTIFICADAS:")
    for cod in selecionadas:
        desc = dores.get(cod.strip())
        if desc:
            print(f"✅ {desc}")

    # Escolha do plano principal
    escolha = input("\n🎯 Escolha um plano (Básico, Intermediário, Premium): ").strip().capitalize()

    if escolha in planos:
        qtd = atendimentos_por_plano[escolha]
        desconto = planos[escolha]
        valor_bruto = preco_ocorrencia * qtd
        valor_final = valor_bruto * (1 - desconto)

        print("\n💼 RESUMO DO PLANO ESCOLHIDO")
        print("-" * 60)
        print(f"📘 Plano: {escolha}")
        print(f"📌 Atendimentos inclusos: {qtd}")
        print(f"💵 Valor original: R$ {valor_bruto:.2f}")
        print(f"💸 Desconto aplicado: {int(desconto * 100)}%")
        print(f"✅ Valor final: R$ {valor_final:.2f}")

        # Estratégia de marketing emocional
        print("\n🎯 ESTRATÉGIA DE VENDA CONSULTIVA")
        print("-" * 60)
        print("💡 Destaque como o plano soluciona as dores mencionadas com:")
        print("✔ Respostas rápidas")
        print("✔ Monitoramento proativo")
        print("✔ Economia comprovada")
        print("✔ Acesso a especialistas")

        # Sugestão de pacote adicional
        print("\n✨ Sugestão Premium: Combine com o pacote de 'Acompanhamento de Analista' para atendimento personalizado e ganho de produtividade.")

    else:
        print("❌ Opção inválida. Por favor, tente novamente.")

    print("\n🧠 Dica final: Ofereça a opção de pagamento recorrente com descontos e garanta fidelização!")

# Executa o programa
if __name__ == "__main__":
    simulador_suporte_sistemas()
