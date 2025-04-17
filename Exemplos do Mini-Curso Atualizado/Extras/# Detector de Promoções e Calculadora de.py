import flet as ft

def calcular_margem_lucro(preco_custo, preco_venda):
    return ((preco_venda - preco_custo) / preco_custo) * 100

def calcular_promocao(preco_original, preco_desconto):
    desconto = ((preco_original - preco_desconto) / preco_original) * 100
    if desconto > 50:
        return "🎉 Promoção incrível!", desconto
    elif 20 <= desconto <= 50:
        return "👍 Boa promoção!", desconto
    else:
        return "⚠️ Desconto pequeno, avalie com cuidado.", desconto

def main(page: ft.Page):
    page.title = "Detector de Promoções com Lucro e Estratégias"
    page.theme_mode = "black"
    
    preco_original = ft.TextField(label="Preço original (R$)", width=500)
    preco_desconto = ft.TextField(label="Preço com desconto (R$)", width=500)
    preco_custo = ft.TextField(label="Preço de custo (R$)", width=500)
    preco_venda = ft.TextField(label="Preço de venda (R$)", width=500)

    resultado = ft.Text("")
    estrategia = ft.Text("")

    def calcular(e):
        try:
            original = float(preco_original.value)
            desconto = float(preco_desconto.value)
            custo = float(preco_custo.value)
            venda = float(preco_venda.value)

            if original <= 0 or desconto < 0 or custo <= 0 or venda <= 0:
                resultado.value = "⚠️ Todos os valores devem ser positivos!"
                page.update()
                return

            margem = calcular_margem_lucro(custo, venda)
            mensagem, perc_desconto = calcular_promocao(original, desconto)
            valor_desconto = original - desconto

            resultado.value = (
                f"📊 Resultado da Análise:\n"
                f"Preço original: R$ {original:.2f}\n"
                f"Preço com desconto: R$ {desconto:.2f}\n"
                f"Valor do desconto: R$ {valor_desconto:.2f} ({perc_desconto:.2f}%)\n"
                f"{mensagem}\n\n"
                f"💼 Margem de Lucro: {margem:.2f}%"
            )

            if margem >= 100:
                estrategia.value = "💰 Estratégia: Essa margem permite até promoções agressivas com lucro excelente! Reforce o valor agregado ao cliente."
            elif 50 <= margem < 100:
                estrategia.value = "📦 Estratégia: Boa margem. Ofereça brindes, upgrades ou frete grátis para aumentar o ticket médio."
            elif 20 <= margem < 50:
                estrategia.value = "📈 Estratégia: Margem ok. Use escassez ('últimas unidades'), urgência ('só hoje!') e parcelamento."
            else:
                estrategia.value = "🛑 Alerta: Margem baixa. Reveja fornecedores ou negocie volumes maiores antes de aplicar descontos."

        except ValueError:
            resultado.value = "❌ Por favor, insira valores numéricos válidos."
        
        page.update()

    page.add(
        ft.Text("💸 Detector de Promoções com Análise de Lucro", size=22, weight="bold"),
        preco_original,
        preco_desconto,
        preco_custo,
        preco_venda,
        ft.ElevatedButton("Analisar Promoção", on_click=calcular),
        resultado,
        estrategia
    )

if __name__ == "__main__":
    ft.app(target=main)
