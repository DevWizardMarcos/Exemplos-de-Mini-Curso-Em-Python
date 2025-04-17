def calcular_promocao_por_percentual(preco_original, percentual_desconto):
    if percentual_desconto < 0 or percentual_desconto > 100:
        return "❗ Percentual de desconto inválido. Digite um valor entre 0 e 100."

    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_com_desconto = preco_original - valor_desconto

    print(f"\n💰 Você economizou R${valor_desconto:.2f}")
    print(f"💳 Preço com desconto: R${preco_com_desconto:.2f}")
    print(f"📉 Desconto aplicado: {percentual_desconto:.2f}%")

    if percentual_desconto >= 50:
        return "🔥 Promoção incrível!"
    elif 20 <= percentual_desconto < 50:
        return "👍 Boa promoção!"
    else:
        return "😕 Desconto pequeno, talvez não valha a pena."


def main():
    try:
        preco_original = float(input("Digite o preço original do produto: R$ "))
        percentual_desconto = float(input("Digite a porcentagem de desconto (%): "))

        if preco_original <= 0:
            print("❗ O preço original deve ser maior que zero.")
            return

        resultado = calcular_promocao_por_percentual(preco_original, percentual_desconto)
        print(resultado)

    except ValueError:
        print("❗ Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
