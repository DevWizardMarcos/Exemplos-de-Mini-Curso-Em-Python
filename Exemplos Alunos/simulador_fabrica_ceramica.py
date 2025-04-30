def simulador_producao_ceramica():
    print("=" * 65)
    print("🏭 SIMULADOR DE CONTROLE DE PRODUÇÃO E PERDAS - FÁBRICA DE CERÂMICA 🏭")
    print("=" * 65)

    # Cadastro dos processos produtivos
    processos = [
        "Barbotina",
        "Plaqueira",
        "Biscoito",
        "Esmaltação",
        "Queima 1",
        "Queima 2",
        "Entrega"
    ]

    # Entrada de dados de produção
    producao_total = int(input("\n🔢 Quantas peças foram planejadas para produção hoje? "))
    perdas_total = 0
    funcionarios = int(input("👷 Quantos funcionários estão na linha de produção hoje? "))

    print("\n📋 Informe as perdas em cada etapa do processo:")
    perdas_por_processo = {}
    producao_por_processo = {}
    restante = producao_total

    for processo in processos:
        perda = int(input(f"❌ Peças perdidas em '{processo}': "))
        perdas_por_processo[processo] = perda
        restante -= perda
        producao_por_processo[processo] = max(restante, 0)

    perdas_total = sum(perdas_por_processo.values())
    percentual_perda = (perdas_total / producao_total) * 100 if producao_total > 0 else 0

    print("\n📊 RESUMO DA PRODUÇÃO DO DIA:")
    print("-" * 65)
    print(f"🔢 Peças planejadas: {producao_total}")
    print(f"✅ Peças produzidas e entregues: {producao_por_processo['Entrega']}")
    print(f"❌ Total de perdas: {perdas_total} ({percentual_perda:.2f}%)")
    print(f"👷 Funcionários envolvidos: {funcionarios}")

    print("\n🔎 DETALHAMENTO DAS PERDAS POR PROCESSO:")
    for processo in processos:
        print(f"• {processo:<12}: {perdas_por_processo[processo]} perdas | Restantes após etapa: {producao_por_processo[processo]}")

    # Principais desafios e soluções
    print("\n😟 DESAFIOS MAIS COMUNS NA FÁBRICA DE CERÂMICA:")
    desafios = {
        "1": "Dificuldade em identificar onde ocorrem mais perdas",
        "2": "Falta de padronização nos processos",
        "3": "Baixa produtividade dos funcionários",
        "4": "Problemas de qualidade na queima",
        "5": "Retrabalho e desperdício de material",
        "6": "Falta de treinamento da equipe",
        "7": "Dificuldade no controle de estoque e insumos"
    }
    for k, v in desafios.items():
        print(f"{k}. {v}")

    selecionados = input("Selecione os desafios enfrentados (ex: 1,3,5): ").split(",")

    print("\n📌 DESAFIOS IDENTIFICADOS:")
    for cod in selecionados:
        desc = desafios.get(cod.strip())
        if desc:
            print(f"✅ {desc}")

    solucoes = {
        "1": "Implantar controle digital por etapa e relatórios diários de perdas.",
        "2": "Padronizar procedimentos e treinar operadores para cada processo.",
        "3": "Definir metas claras e premiar equipes com melhor desempenho.",
        "4": "Ajustar parâmetros de queima e monitorar temperatura/humidade.",
        "5": "Reaproveitar material sempre que possível e revisar processos.",
        "6": "Realizar treinamentos periódicos e reciclagem de boas práticas.",
        "7": "Usar sistema integrado para controle de estoque e consumo."
    }
    print("\n🛠️ SUGESTÕES DE MELHORIA:")
    for cod in selecionados:
        sol = solucoes.get(cod.strip())
        if sol:
            print(f"💡 {sol}")

    # Surpresa: Ranking de eficiência por funcionário (simulação)
    print("\n🏅 SIMULAÇÃO DE EFICIÊNCIA POR FUNCIONÁRIO:")
    if funcionarios > 0:
        eficiencia = producao_por_processo['Entrega'] / funcionarios
        print(f"Cada funcionário entregou em média: {eficiencia:.2f} peças.")
        if eficiencia < 20:
            print("⚠️ Atenção: Eficiência baixa, avalie treinamento e processos.")
        elif eficiencia < 50:
            print("🔄 Eficiência razoável, mas pode melhorar com ajustes.")
        else:
            print("✅ Excelente produtividade! Continue assim.")
    else:
        print("Nenhum funcionário informado para cálculo de eficiência.")

    print("\n🧠 Dica final: Controle diário e feedback rápido reduzem perdas e aumentam o lucro!")
    print("🚀 Obrigado por usar o simulador da fábrica de cerâmica. Bons resultados!")

# Executa o programa
if __name__ == "__main__":
    simulador_producao_ceramica()