def story_generator():
    import random

    # Listas adaptadas para situações reais de fisioterapia
    characters = ["uma fisioterapeuta dedicada", "um paciente em busca de qualidade de vida", "uma equipe de reabilitação", "um atleta em recuperação", "uma mãe preocupada com a saúde"]
    settings = ["durante uma sessão de reabilitação", "em um programa personalizado de fisioterapia", "em uma avaliação postural", "em um tratamento para dores crônicas", "durante um acompanhamento esportivo"]
    conflicts = [
        "alcançou uma recuperação surpreendente", 
        "superou limitações físicas", 
        "voltou a praticar atividades que amava", 
        "melhorou sua qualidade de vida", 
        "atingiu seus objetivos de saúde"
    ]

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)

    story = f"Era uma vez {character} {setting} que {conflict}."
    return story

def generate_fisioterapia_post():
    story = story_generator()
    call_to_action = (
        "\n\n💪 Cuide da sua saúde com um atendimento personalizado!"
        "\n🌟 Agende uma avaliação gratuita e descubra como podemos ajudar você a alcançar seus objetivos."
        "\n📞 Entre em contato agora mesmo e dê o primeiro passo para uma vida sem dores!"
    )
    return story + call_to_action

if __name__ == "__main__":
    print("Post de Fisioterapia Gerado:\n")
    print(generate_fisioterapia_post())