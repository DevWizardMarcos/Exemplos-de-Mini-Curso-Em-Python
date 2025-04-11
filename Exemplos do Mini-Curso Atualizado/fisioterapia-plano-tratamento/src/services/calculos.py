def calcular_frequencia_maxima(idade):
    return 220 - idade

def calcular_zona_frequencia(frequencia_maxima):
    zona_inferior = frequencia_maxima * 0.5
    zona_superior = frequencia_maxima * 0.85
    return zona_inferior, zona_superior

def calcular_vo2_maximo(frequencia_maxima, frequencia_repouso, sexo):
    if sexo == "M":
        return 15.3 * (frequencia_maxima / frequencia_repouso)
    elif sexo == "F":
        return 14.7 * (frequencia_maxima / frequencia_repouso)
    else:
        return None