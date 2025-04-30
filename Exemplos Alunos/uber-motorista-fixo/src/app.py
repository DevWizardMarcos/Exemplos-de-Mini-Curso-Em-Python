import random

# Preço por quilômetro
PRECO_POR_KM = 2.50  # Valor em R$

# Estrutura para armazenar informações do cliente fixo
class ClienteFixo:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.corridas = []

    def adicionar_corrida(self, distancia):
        self.corridas.append(distancia)

    def calcular_total_corridas(self):
        return sum(self.corridas) * PRECO_POR_KM

# Função para calcular a tarifa com base na distância
def calcular_tarifa(distancia):
    return distancia * PRECO_POR_KM

# Função para interagir com o cliente
def interagir_com_cliente(cliente):
    print(f"Olá, {cliente.nome}! Como posso ajudá-lo hoje?")
    distancia = float(input("Digite a distância da corrida em km: "))
    tarifa = calcular_tarifa(distancia)
    cliente.adicionar_corrida(distancia)
    print(f"A tarifa para sua corrida de {distancia} km é R$ {tarifa:.2f}.")
    print(f"Total acumulado em corridas: R$ {cliente.calcular_total_corridas():.2f}")

# Função para oferecer promoções
def oferecer_promocao(cliente):
    if len(cliente.corridas) > 5:
        desconto = random.uniform(0.1, 0.3)  # Desconto aleatório entre 10% e 30%
        print(f"🎉 Parabéns, {cliente.nome}! Você ganhou um desconto de {desconto*100:.0f}% na próxima corrida!")
    else:
        print("Continue utilizando nossos serviços para ganhar promoções exclusivas!")

# Função principal
def main():
    cliente_fixo = ClienteFixo("João Silva", "11999999999")
    while True:
        interagir_com_cliente(cliente_fixo)
        oferecer_promocao(cliente_fixo)
        continuar = input("Deseja realizar outra corrida? (s/n): ").lower()
        if continuar != 's':
            break

# Executa o programa
if __name__ == "__main__":
    main()