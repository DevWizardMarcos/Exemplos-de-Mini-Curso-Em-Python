valor_compra = float(input("Digite o valor da sua compra: R$ "))

if valor_compra >= 200:
    desconto = valor_compra * 0.10  # 10% de desconto
    total = valor_compra - desconto
    print(f"Você ganhou um desconto de R$ {desconto:.2f}. Total a pagar: R$ {total:.2f}")
elif valor_compra >= 100:
    desconto = valor_compra * 0.05  # 5% de desconto
    total = valor_compra - desconto
    print(f"Você ganhou um desconto de R$ {desconto:.2f}. Total a pagar: R$ {total:.2f}")
else:
    print(f"Sem desconto aplicado. Total a pagar: R$ {valor_compra:.2f}")
