import random
import time

def gerar_codigo_rastreio():
    return "AGRO" + str(random.randint(100000, 999999))

def simular_status_entrega():
    status = [
        "Pedido recebido na fazenda",
        "Carga em inspeção fitossanitária",
        "Em trânsito para o silo regional",
        "A caminho do porto/exportação",
        "Entrega prevista para hoje"
    ]
    return random.choice(status)

def simulador_rastreamento_agro():
    print("=" * 70)
    print("🌱 OPERADOR DE RASTREAMENTO CORPORATIVO AGROLOG | AGROLOGÍSTICA INTELIGENTE 🌱")
    print("=" * 70)

    # Entrada básica
    empresa = input("\n🏢 Nome da empresa agrícola: ")
    produto = input("🌾 Produto a ser transportado (ex: soja, milho, algodão): ")
    valor_unitario = float(input(f"💰 Valor unitário da tonelada de {produto} (R$): "))
    quantidade = int(input(f"🚜 Quantas toneladas de {produto} serão transportadas? "))
    valor_total_carga = valor_unitario * quantidade

    print(f"\n📦 Valor total da carga: R$ {valor_total_carga:.2f}")

    # Locais de entrega e suas taxas
    locais_entrega = {
        "Silo Central": 900.00,
        "Porto de Santos": 2500.00,
        "Terminal Ferroviário": 1800.00,
        "Armazém Alfandegado": 2200.00,
        "Fábrica de Rações": 1500.00
    }

    print("\n🗺️ LOCAIS DISPONÍVEIS PARA ENTREGA:")
    for local, taxa in locais_entrega.items():
        print(f"📍 {local:<20} - R$ {taxa:.2f}")

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
    print("\n🔒 BENEFÍCIO OPCIONAL: Seguro Agrícola Total por R$ 800.00")
    seguro = input("Deseja adicionar seguro agrícola? (s/n): ").lower()
    valor_seguro = 800.00 if seguro == "s" else 0.00

    # Pacotes de rastreamento corporativo
    print("\n🎁 PACOTES CORPORATIVOS DE RASTREAMENTO AGRO:")
    pacotes = {
        "1": {"desconto_entrega": 0.00, "rastreio": False, "prioridade": False, "relatorio": False, "consultoria": False},
        "2": {"desconto_entrega": 0.12, "rastreio": True, "prioridade": True, "relatorio": True, "consultoria": True},
        "3": {"desconto_entrega": 0.20, "rastreio": True, "prioridade": True, "relatorio": True, "consultoria": True}
    }

    for nome, dados in pacotes.items():
        print(f"🌟 {nome} | Desconto entrega: {int(dados['desconto_entrega']*100)}% | Rastreamento: {'Sim' if dados['rastreio'] else 'Não'} | Relatório: {'Sim' if dados['relatorio'] else 'Não'} | Consultoria Agro: {'Sim' if dados['consultoria'] else 'Não'}")

    pacote_escolhido = input("\n📦 Escolha um pacote (1, 2, 3): ").strip().capitalize()
    if pacote_escolhido not in pacotes:
        print("❌ Pacote inválido, usaremos o padrão Básico.")
        pacote_escolhido = "1"

    pacote = pacotes[pacote_escolhido]
    desconto = pacote["desconto_entrega"]

    # Cálculo de taxas de entrega
    total_entrega_final = total_entrega * (1 - desconto)

    # Valor final
    valor_total_final = valor_total_carga + total_entrega_final + valor_seguro

    print("\n💼 RESUMO FINAL")
    print("-" * 70)
    print(f"🏢 Empresa: {empresa}")
    print(f"🌾 Produto: {produto}")
    print(f"📘 Pacote selecionado: {pacote_escolhido}")
    print(f"🚚 Taxas de entrega (com desconto): R$ {total_entrega_final:.2f}")
    print(f"🔐 Seguro agrícola:                R$ {valor_seguro:.2f}")
    print(f"🎯 TOTAL GERAL:                    R$ {valor_total_final:.2f}")
    print("-" * 70)

    # Geração de código de rastreio e simulação de status
    if pacote["rastreio"]:
        codigo = gerar_codigo_rastreio()
        print(f"\n🔎 Seu código de rastreio exclusivo: {codigo}")
        print("Acompanhe o status da sua carga agrícola em tempo real pelo nosso portal AgroLog ou WhatsApp!")
        for i in range(3):
            status = simular_status_entrega()
            print(f"📍 Status atualizado: {status}")
            time.sleep(1)
        print("✅ Rastreamento ativo 24h para sua tranquilidade e compliance!")
    else:
        print("\nℹ️ Pacote Básico não inclui rastreamento em tempo real. Considere um upgrade para mais segurança e controle!")

    # Relatório detalhado
    if pacote["relatorio"]:
        print("\n📊 Relatório detalhado será enviado por e-mail a cada etapa da entrega.")
        print("Inclui fotos, horários, laudos fitossanitários e assinatura digital do responsável.")

    # Consultoria agro
    if pacote["consultoria"]:
        print("\n🌽 Consultoria logística agro personalizada inclusa!")
        print("Receba recomendações para otimizar rotas, reduzir perdas e garantir a máxima eficiência no transporte da sua safra.")

    # Estratégia de fechamento e diferenciais para o agro
    print("\n🤝 POR QUE FECHAR COM A AGROLOG?")
    print("✔️ Especialistas em logística agrícola e compliance internacional.")
    print("✔️ Rastreamento em tempo real e suporte humanizado 24h.")
    print("✔️ Relatórios detalhados para auditoria e exportação.")
    print("✔️ Seguro agrícola opcional para sua total tranquilidade.")
    print("✔️ Consultoria logística gratuita para grandes volumes.")
    print("✔️ Garantia de entrega ou seu dinheiro de volta!")
    print("\n🎁 Feche agora e ganhe um mês de consultoria logística agro grátis!")
    print("📞 Entre em contato: agro@agrolog.com | WhatsApp: (11) 98888-8888")
    print("💡 AgroLog: Sua produção, nosso compromisso com o campo e o futuro!")

# Executa o programa
if __name__ == "__main__":
    simulador_rastreamento_agro()