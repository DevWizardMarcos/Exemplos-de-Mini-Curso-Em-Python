def simulador_suporte_ti():
    print("=" * 60)
    
    print("💻 SIMULADOR DE PLANOS DE SUPORTE PARA TI EMPRESARIAL 💻")
    print("=" * 60)

    # Entrada de informações básicas
    qtd_funcionarios = int(input("\n👥 Quantos funcionários usam computadores na empresa? "))
    qtd_servidores = int(input("🖥️ Quantos servidores ou sistemas críticos existem? "))
    valor_gasto = float(input("💰 Valor médio mensal já gasto com TI (em R$): "))

    print(f"\n📊 Sua empresa possui {qtd_funcionarios} usuários e {qtd_servidores} servidores.")
    print(f"💸 Gasto médio mensal atual: R$ {valor_gasto:.2f}")

    # Planos de suporte
    planos = {
        "Essencial": {"usuarios": 10, "servidores": 1, "desconto": 0.05},
        "Profissional": {"usuarios": 30, "servidores": 3, "desconto": 0.15},
        "Corporativo": {"usuarios": 100, "servidores": 10, "desconto": 0.25}
    }
    preco_usuario = 60.0
    preco_servidor = 250.0

    print("\n📦 PLANOS DE SUPORTE DISPONÍVEIS:")
    print("-" * 60)
    for nome, dados in planos.items():
        valor = (dados["usuarios"] * preco_usuario) + (dados["servidores"] * preco_servidor)
        valor_final = valor * (1 - dados["desconto"])
        print(f"📘 {nome:<12} | Até {dados['usuarios']} usuários, {dados['servidores']} servidores | "
              f"R$ {valor_final:.2f} (🔻 {int(dados['desconto']*100)}% OFF)")

    # Pacotes extras
    pacotes_extras = {
        "Backup em Nuvem Gerenciado": 400.00,
        "Firewall e Segurança Avançada": 650.00,
        "Treinamento em Segurança Digital": 350.00,
        "Monitoramento 24/7": 800.00
    }
    print("\n🧩 PACOTES EXTRAS RECOMENDADOS:")
    print("-" * 60)
    for pacote, valor in pacotes_extras.items():
        desconto = 0.10 if valor > 500 else 0.05
        valor_descontado = valor * (1 - desconto)
        print(f"🔧 {pacote:<35} 👉 De: R$ {valor:.2f} | Por: R$ {valor_descontado:.2f} ({int(desconto*100)}% OFF)")

    # Principais dores reais de TI
    print("\n😟 PRINCIPAIS PROBLEMAS DE TI NAS EMPRESAS:")
    dores = {
        "1": "Lentidão e travamentos frequentes nas máquinas",
        "2": "Ataques de vírus, ransomware ou phishing",
        "3": "Perda de dados por falta de backup",
        "4": "Quedas de sistemas e indisponibilidade",
        "5": "Usuários sem treinamento causando incidentes",
        "6": "Falta de atualização e manutenção preventiva",
        "7": "Suporte demorado ou ineficiente",
        "8": "Problemas de rede e internet instável"
    }
    for k, v in dores.items():
        print(f"{k}. {v}")

    selecionadas = input("Digite os números dos problemas enfrentados (ex: 2,4,7): ").split(",")

    print("\n📌 PROBLEMAS IDENTIFICADOS:")
    for cod in selecionadas:
        desc = dores.get(cod.strip())
        if desc:
            print(f"✅ {desc}")

    # Soluções para cada dor
    solucoes = {
        "1": "Realizar manutenção preventiva e upgrade de hardware periodicamente.",
        "2": "Implantar antivírus corporativo, firewall e treinar usuários.",
        "3": "Contratar backup em nuvem e testar restauração regularmente.",
        "4": "Monitorar sistemas 24/7 e implementar redundância.",
        "5": "Oferecer treinamentos regulares em boas práticas de TI.",
        "6": "Agendar atualizações automáticas e revisões técnicas.",
        "7": "Ter SLA claro e equipe de suporte dedicada.",
        "8": "Revisar infraestrutura de rede e contratar links redundantes."
    }
    print("\n🛠️ SUGESTÕES DE SOLUÇÃO PARA OS PROBLEMAS:")
    for cod in selecionadas:
        sol = solucoes.get(cod.strip())
        if sol:
            print(f"💡 {sol}")

    # Escolha do plano
    escolha = input("\n🎯 Escolha um plano (Essencial, Profissional, Corporativo): ").strip().capitalize()
    if escolha in planos:
        dados = planos[escolha]
        valor = (dados["usuarios"] * preco_usuario) + (dados["servidores"] * preco_servidor)
        valor_final = valor * (1 - dados["desconto"])
        economia = valor - valor_final

        print("\n💼 RESUMO DO PLANO ESCOLHIDO")
        print("-" * 60)
        print(f"📘 Plano: {escolha}")
        print(f"👥 Usuários inclusos: {dados['usuarios']}")
        print(f"🖥️ Servidores inclusos: {dados['servidores']}")
        print(f"💵 Valor original: R$ {valor:.2f}")
        print(f"💸 Desconto aplicado: {int(dados['desconto']*100)}%")
        print(f"✅ Valor final: R$ {valor_final:.2f}")
        print(f"💰 Economia direta: R$ {economia:.2f}")

        print("\n🎯 COMO O PLANO AJUDA SUA EMPRESA:")
        print("✔ Reduz riscos de parada e perda de dados")
        print("✔ Melhora a produtividade dos usuários")
        print("✔ Garante suporte rápido e especializado")
        print("✔ Ajuda a empresa a crescer com tecnologia segura")

        print("\n✨ Sugestão: Combine com 'Monitoramento 24/7' para máxima tranquilidade!")

    else:
        print("❌ Opção inválida. Por favor, tente novamente.")

    print("\n🧠 Dica final: Invista em TI preventiva e evite prejuízos futuros!")
    print("🚀 Obrigado por utilizar o simulador de TI! Sucesso e tecnologia sem dor de cabeça!")

# Executa o programa
if __name__ == "__main__":
    simulador_suporte_ti()