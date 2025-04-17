def validar_idade(idade):
    if isinstance(idade, int) and 0 <= idade <= 120:
        return True
    return False

def validar_sexo(sexo):
    return sexo in ['M', 'F']

def formatar_dados(dados):
    return {key: str(value).strip() for key, value in dados.items()}