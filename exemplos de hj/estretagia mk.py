import flet as ft

def main(page: ft.Page):
    page.title = "Simulador de Serviços de Marketing"
    page.scroll = "auto"

    # Dados dos serviços e pacotes
    servicos = {
        "Gestão de Redes Sociais": 2000.00,
        "Campanha Google Ads": 3000.00,
        "Criação de Conteúdo": 1500.00,
        "Consultoria Estratégica": 2500.00,
        "Design Gráfico": 1200.00
    }
    pacotes = {
        "1": {"nome": "Essencial", "desconto": 0.00, "consultoria": False, "relatorio": False},
        "2": {"nome": "Avançado", "desconto": 0.10, "consultoria": True, "relatorio": True},
        "3": {"nome": "Premium", "desconto": 0.20, "consultoria": True, "relatorio": True}
    }

    # Campos do formulário
    nome_cliente = ft.TextField(label="Nome do cliente", width=300)
    objetivo = ft.TextField(label="Objetivo da campanha", width=300)
    investimento = ft.TextField(label="Investimento disponível (R$)", width=200, value="0")
    servicos_checks = [ft.Checkbox(label=f"{s} - R$ {v:.2f}") for s, v in servicos.items()]
    pacote_dropdown = ft.Dropdown(
        label="Pacote de Marketing",
        options=[
            ft.dropdown.Option("1", "Essencial"),
            ft.dropdown.Option("2", "Avançado"),
            ft.dropdown.Option("3", "Premium"),
        ],
        value="1"
    )
    resultado = ft.Text("", selectable=True)

    def calcular_resumo(e):
        selecionados = [s.label.split(" - ")[0] for s in servicos_checks if s.value]
        total_servicos = sum(servicos[s] for s in selecionados if s in servicos)
        pacote = pacotes[pacote_dropdown.value]
        desconto = pacote["desconto"]
        total_final = total_servicos * (1 - desconto)
        resumo = f"👤 Cliente: {nome_cliente.value}\n"
        resumo += f"🎯 Objetivo: {objetivo.value}\n"
        resumo += f"🛠️ Serviços contratados:\n"
        for s in selecionados:
            resumo += f"   - {s}: R$ {servicos[s]:.2f}\n"
        resumo += f"📘 Pacote: {pacote['nome']}\n"
        resumo += f"💸 Desconto: R$ {(total_servicos * desconto):.2f}\n"
        resumo += f"🎯 TOTAL GERAL: R$ {total_final:.2f}\n"
        resumo += "\n⏳ Oferta exclusiva: Feche agora e ganhe uma análise gratuita do seu funil de vendas digital!\n"
        if pacote["consultoria"]:
            resumo += "\n🤝 Consultoria estratégica incluída!\n"
        if pacote["relatorio"]:
            resumo += "📊 Relatório detalhado semanal incluso!\n"
        resumo += "\n✨ DICA EXCLUSIVA PARA VOCÊ:\n"
        resumo += "Ao escolher nossos pacotes avançados, sua marca ganha mais visibilidade, relatórios detalhados e consultoria estratégica para potencializar resultados!\n"
        resumo += "\n🤝 POR QUE FECHAR COM NOSSA AGÊNCIA?\n"
        resumo += "✔️ Estratégias personalizadas para cada tipo de negócio.\n"
        resumo += "✔️ Relatórios detalhados para acompanhamento e prestação de contas.\n"
        resumo += "✔️ Consultoria estratégica para potencializar resultados.\n"
        resumo += "✔️ Atendimento humanizado e suporte dedicado.\n"
        resumo += "✔️ Garantia de satisfação ou seu dinheiro de volta!\n"
        resumo += "\n🎁 Feche agora e ganhe um mês de acompanhamento premium grátis para testar todos os benefícios!\n"
        resumo += "📞 comercial@agenciamkt.com | WhatsApp: (11) 99999-9999\n"
        resumo += "💡 Agência MKT: Sua marca, nosso compromisso!"
        resultado.value = resumo
        page.update()

    # Layout
    page.add(
        ft.Text("Simulador de Serviços de Marketing", size=24, weight="bold"),
        nome_cliente,
        objetivo,
        investimento,
        ft.Text("Selecione os serviços desejados:"),
        ft.Column(servicos_checks, spacing=2),
        pacote_dropdown,
        ft.ElevatedButton("Calcular Resumo", on_click=calcular_resumo),
        ft.Divider(),
        resultado
    )

if __name__ == "__main__":
    import flet as ft
    ft.app(target=main)