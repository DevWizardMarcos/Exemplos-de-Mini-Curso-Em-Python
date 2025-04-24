import flet as ft

def simulador_servicos_personalizacao_legendas(page: ft.Page):
    page.title = "Simulador de Serviços - Legendas de Músicas"
    page.theme_mode = "light"
    page.window_width = 700

    # Serviços e pacotes
    servicos = {
        "Legenda para Vídeo no YouTube": {"preco": 80.0, "margem": 0.60},
        "Legenda para Instagram Reels": {"preco": 60.0, "margem": 0.55},
        "Legenda para TikTok": {"preco": 50.0, "margem": 0.50},
        "Legenda para Shows/Apresentações": {"preco": 150.0, "margem": 0.65},
        "Tradução e Sincronização de Legendas": {"preco": 120.0, "margem": 0.70}
    }
    pacotes = {
        "Básico": {
            "itens": {"Legenda para Vídeo no YouTube": 1, "Legenda para Instagram Reels": 1},
            "desconto": 0.10,
            "marketing": "Ideal para quem está começando a divulgar músicas nas redes"
        },
        "Influencer": {
            "itens": {"Legenda para TikTok": 2, "Legenda para Instagram Reels": 2, "Legenda para Vídeo no YouTube": 1},
            "desconto": 0.15,
            "marketing": "Mais vendido! Para quem quer presença forte em todas as plataformas"
        },
        "Profissional": {
            "itens": {"Legenda para Shows/Apresentações": 1, "Tradução e Sincronização de Legendas": 1, "Legenda para Vídeo no YouTube": 1},
            "desconto": 0.20,
            "marketing": "Pacote completo para músicos e produtores profissionais"
        }
    }

    valor_investido = ft.TextField(label="Quanto você já investiu em equipamentos/capacitação (R$)?", width=350)
    escolha_pacote = ft.Dropdown(
        label="Escolha um pacote",
        options=[ft.dropdown.Option(nome) for nome in pacotes.keys()],
        width=350
    )
    resultado = ft.Text("")
    checklist_column = ft.Column()
    status_column = ft.Column()
    btn_checklist = ft.ElevatedButton("Atualizar Check-list", visible=False)
    checklist = {}

    def mostrar_pacotes(e):
        pacotes_text = []
        for nome, pacote in pacotes.items():
            total_sem_desconto = sum(servicos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
            desconto = pacote["desconto"]
            total_com_desconto = total_sem_desconto * (1 - desconto)
            itens = "\n".join([f"• {qtd}x {item} (R$ {servicos[item]['preco']:.2f})" for item, qtd in pacote["itens"].items()])
            pacotes_text.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"{nome} - {pacote['marketing']}", weight="bold", size=16),
                        ft.Text(itens),
                        ft.Text(f"Valor sem desconto: R$ {total_sem_desconto:.2f}"),
                        ft.Text(f"Desconto: {int(desconto*100)}%"),
                        ft.Text(f"Valor final: R$ {total_com_desconto:.2f}", weight="bold", color=ft.colors.GREEN),
                        ft.Text("🔥 Promoção válida para os 10 primeiros clientes do mês!", italic=True, color=ft.colors.ORANGE)
                    ]),
                    bgcolor=ft.colors.BLUE_50,
                    border_radius=10,
                    padding=10,
                    margin=5
                )
            )
        page.controls[3].controls = pacotes_text
        page.update()

    def simular(e):
        status_column.controls.clear()
        checklist_column.controls.clear()
        resultado.value = ""
        if not valor_investido.value or not escolha_pacote.value:
            resultado.value = "Preencha todos os campos!"
            page.update()
            return

        pacote = pacotes[escolha_pacote.value]
        desconto = pacote["desconto"]
        total_sem_desconto = sum(servicos[item]["preco"] * qtd for item, qtd in pacote["itens"].items())
        total_com_desconto = total_sem_desconto * (1 - desconto)
        economia = total_sem_desconto - total_com_desconto

        resultado.value = (
            f"✅ Pacote escolhido: {escolha_pacote.value}\n"
            f"💰 Economia para o cliente: R$ {economia:.2f}\n"
            f"💳 Valor a receber: R$ {total_com_desconto:.2f}\n"
            "💡 Cross-sell: revisão extra de legendas por apenas R$ 29,00!\n"
            "📢 Gatilho de urgência: Válido apenas para contratos fechados nesta semana!"
        )

        # Monta check-list
        checklist.clear()
        for item in pacote["itens"]:
            checklist[item] = {"concluido": False, "pago": False}
            checklist_column.controls.append(
                ft.Row([
                    ft.Checkbox(label=f"{item} - Concluído", value=False, on_change=lambda ev, i=item: atualizar_checklist(i, "concluido", ev.control.value)),
                    ft.Checkbox(label="Pago", value=False, on_change=lambda ev, i=item: atualizar_checklist(i, "pago", ev.control.value)),
                ])
            )
        btn_checklist.visible = True
        page.update()

    def atualizar_checklist(item, campo, valor):
        checklist[item][campo] = valor

    def mostrar_status(e):
        status_column.controls.clear()
        for item, status in checklist.items():
            status_legenda = "Concluída" if status["concluido"] else "Pendente"
            status_pagamento = "Pago" if status["pago"] else "Em aberto"
            status_column.controls.append(
                ft.Text(f"{item}: {status_legenda} | {status_pagamento}")
            )
        page.update()

    # Adicionando o conteúdo principal dentro de um ScrollView (Column com scroll)
    conteudo = ft.Column(
        [
            ft.Text("🎶 Simulador de Serviços para Personalização de Legendas de Músicas", size=22, weight="bold"),
            valor_investido,
            escolha_pacote,
            ft.Column([]),  # Pacotes serão exibidos aqui
            ft.Row([
                ft.ElevatedButton("Mostrar Pacotes", on_click=mostrar_pacotes),
                ft.ElevatedButton("Simular Contrato", on_click=simular)
            ]),
            resultado,
            ft.Text("📋 Check-list de Legendas:", size=16, weight="bold"),
            checklist_column,
            btn_checklist,
            ft.Text("✅ Status das Legendas:", size=16, weight="bold"),
            status_column
        ],
        scroll=ft.ScrollMode.ALWAYS
    )

    page.add(conteudo)
    btn_checklist.on_click = mostrar_status

if __name__ == "__main__":
    import flet as ft
    ft.app(target=simulador_servicos_personalizacao_legendas)