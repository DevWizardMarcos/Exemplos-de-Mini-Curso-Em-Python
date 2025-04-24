import random
import time

def gerar_codigo_rastreio():
    return "LTBR" + str(random.randint(100000, 999999))

def simular_status_entrega():
    status = [
        "Pedido recebido",
        "Carga em preparação",
        "Em trânsito para o centro logístico",
        "A caminho do destino",
        "Entrega prevista para hoje"
    ]
    return random.choice(status)

def simulador_rastreamento_carga():
    print("=" * 70)
    print("📦 BEM-VINDO AO OPERADOR DE RASTREAMENTO DE CARGAS LOGITECH 📦")
    print("=" * 70)

    # Entrada básica
    cliente = input("\n👤 Nome do cliente: ")
    valor_unitario = float(input("💰 Valor unitário de cada item (R$): "))
    quantidade = int(input("🚚 Quantos itens serão transportados? "))
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

    # Pacotes de rastreamento
    print("\n🎁 PACOTES DE RASTREAMENTO DISPONÍVEIS:")
    pacotes = {
        "1": {"desconto_entrega": 0.00, "rastreio": False, "prioridade": False, "relatorio": False},
        "2": {"desconto_entrega": 0.10, "rastreio": True, "prioridade": True, "relatorio": True},
        "3": {"desconto_entrega": 0.20, "rastreio": True, "prioridade": True, "relatorio": True}
    }

    for nome, dados in pacotes.items():
        print(f"🌟 {nome} | Desconto entrega: {int(dados['desconto_entrega']*100)}% | Rastreamento: {'Sim' if dados['rastreio'] else 'Não'} | Relatório detalhado: {'Sim' if dados['relatorio'] else 'Não'}")

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
    print(f"👤 Cliente: {cliente}")
    print(f"📘 Pacote selecionado: {pacote_escolhido}")
    print(f"🚚 Taxas de entrega (com desconto): R$ {total_entrega_final:.2f}")
    print(f"🔐 Seguro:                        R$ {valor_seguro:.2f}")
    print(f"🎯 TOTAL GERAL:                   R$ {valor_total_final:.2f}")
    print("-" * 70)

    # Geração de código de rastreio e simulação de status
    if pacote["rastreio"]:
        codigo = gerar_codigo_rastreio()
        print(f"\n🔎 Seu código de rastreio exclusivo: {codigo}")
        print("Acompanhe o status da sua carga em tempo real pelo nosso portal ou WhatsApp!")
        for i in range(3):
            status = simular_status_entrega()
            print(f"📍 Status atualizado: {status}")
            time.sleep(1)
        print("✅ Rastreamento ativo 24h para sua tranquilidade!")
    else:
        print("\nℹ️ Pacote Básico não inclui rastreamento em tempo real. Considere um upgrade para mais segurança!")

    # Relatório detalhado
    if pacote["relatorio"]:
        print("\n📊 Relatório detalhado será enviado por e-mail a cada etapa da entrega.")
        print("Inclui fotos, horários e assinatura digital do destinatário.")

    # Estratégia de fechamento e diferenciais
    print("\n🤝 POR QUE FECHAR COM A LOGITECH?")
    print("✔️ Rastreamento em tempo real e suporte humanizado 24h.")
    print("✔️ Relatórios detalhados para auditoria e compliance.")
    print("✔️ Seguro opcional para sua total tranquilidade.")
    print("✔️ Atendimento personalizado e consultoria logística gratuita.")
    print("✔️ Garantia de entrega ou seu dinheiro de volta!")
    print("\n🎁 Feche agora e ganhe um mês de rastreamento premium grátis para testar todos os benefícios!")
    print("📞 Entre em contato: comercial@logitechbr.com | WhatsApp: (11) 99999-9999")
    print("💡 Logitech: Sua carga, nosso compromisso!")

# Executa o programa
if __name__ == "__main__":
    simulador_rastreamento_carga()