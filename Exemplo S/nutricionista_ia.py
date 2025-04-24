import openai

# Configure sua chave da API da OpenAI
openai.api_key = "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"

def gerar_plano_alimentar(calorias):
    prompt = f"""
    Você é um nutricionista experiente. Crie um plano alimentar detalhado de 7 dias, equilibrado e saudável, para uma pessoa que precisa consumir aproximadamente {calorias} calorias por dia. 
    Estruture o plano dividindo claramente as refeições por dia:
    - Café da manhã
    - Almoço
    - Jantar
    - Lanches intermediários (manhã e tarde)
    Forneça quantidades aproximadas para cada refeição.
    """
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um nutricionista especialista na elaboração de planos alimentares balanceados."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao gerar o plano alimentar: {e}"

def main():
    print("Bem-vindo ao Nutricionista com IA!")
    try:
        idade = int(input("Digite sua idade: "))
        genero = input("Digite seu gênero (M para masculino, F para feminino): ").strip().upper()
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em cm: "))

        calorias = calcular_calorias(idade, genero, peso, altura)
        print(f"\nVocê deve consumir aproximadamente {calorias} calorias por dia.")

        print("\nGerando seu plano alimentar de 7 dias...")
        plano = gerar_plano_alimentar(calorias)
        print("\nPlano Alimentar:")
        print(plano)

    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()