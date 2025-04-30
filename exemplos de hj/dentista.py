import flet as ft

def main(page: ft.Page):
    page.title = "Primeiro Contato - Clínica Odontológica"
    page.scroll = "auto"

    # Serviços odontológicos
    servicos = {
        "Limpeza e Prevenção": 150.00,
        "Clareamento Dental": 800.00,
        "Implante Dentário": 3500.00,
        "Aparelho Ortodôntico": 2500.00,
        "Estética do Sorriso": 1200.00
    }
    pacotes = {
        "1": {"nome": "Consulta Inicial", "desconto": 0.00, "brinde": "Kit Higiene Bucal"},
        "2": {"nome": "Sorriso Perfeito", "desconto": 0.10, "brinde": "Sessão de clareamento grátis"},
        "3": {"nome": "VIP Odonto", "desconto": 0.20, "brinde": "Check-up digital completo"}
    }

    # Campos do formulário
    nome_cliente = ft.TextField(label="Seu nome", width=300)
    contato = ft.TextField(label="WhatsApp ou Telefone", width=300)
    motivo = ft.TextField(label="O que motivou seu contato?", width=400, multiline=True)
    servicos_checks = [ft.Checkbox(label=f"{s} - R$ {v:.2f}") for s, v in servicos.items()]
    pacote_dropdown = ft.Dropdown(
        label="Escolha seu pacote de atendimento",
        options=[
            ft.dropdown.Option("1", "Consulta Inicial"),
            ft.dropdown.Option("2", "Sorriso Perfeito"),
            ft.dropdown.Option("3", "VIP Odonto"),
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
        resumo = f"🦷 Olá, {nome_cliente.value}! Que alegria receber seu contato!\n"
        resumo += f"📱 Entraremos em contato pelo número: {contato.value}\n"
        resumo += f"💬 Motivo do contato: {motivo.value}\n"
        resumo += "\n✨ Serviços de interesse:\n"
        for s in selecionados:
            resumo += f"   - {s}: R$ {servicos[s]:.2f}\n"
        resumo += f"\n🌟 Pacote escolhido: {pacote['nome']}\n"
        resumo += f"💸 Desconto especial: R$ {(total_servicos * desconto):.2f}\n"
        resumo += f"🎯 TOTAL ESTIMADO: R$ {total_final:.2f}\n"
        resumo += f"\n🎁 Brinde exclusivo: {pacote['brinde']}\n"
        resumo += "\n🚀 Surpresa: Ao agendar sua consulta hoje, você garante prioridade no atendimento e um presente especial preparado com carinho para você!\n"
        resumo += "\nPor que escolher nossa clínica?\n"
        resumo += "✔️ Atendimento humanizado e personalizado desde o primeiro contato.\n"
        resumo += "✔️ Tecnologia de ponta para seu conforto e segurança.\n"
        resumo += "✔️ Equipe apaixonada por transformar sorrisos.\n"
        resumo += "✔️ Ambiente acolhedor e pensado para você.\n"
        resumo += "\n💬 Clique em 'Agendar Consulta' e surpreenda-se com uma experiência odontológica única!\n"
        resumo += "📞 WhatsApp: (11) 99999-9999 | contato@clinicadental.com\n"
        resumo += "💙 Clínica Dental: Seu sorriso, nossa paixão!"
        resultado.value = resumo
        page.update()

    # Layout
    page.add(
        ft.Text("Bem-vindo à Clínica Odontológica", size=24, weight="bold"),
        ft.Text("Preencha seus dados e surpreenda-se com nosso atendimento!"),
        nome_cliente,
        contato,
        motivo,
        ft.Text("Selecione os serviços de seu interesse:"),
        ft.Column(servicos_checks, spacing=2),
        pacote_dropdown,
        ft.ElevatedButton("Agendar Consulta", on_click=calcular_resumo),
        ft.Divider(),
        resultado
    )

if __name__ == "__main__":
    import flet as ft
    ft.app(target=main)