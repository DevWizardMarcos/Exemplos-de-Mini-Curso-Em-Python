idade = int(input("Digite a idade do paciente: "))
frequencia_maxima = 220 - idade

zona_inferior = frequencia_maxima * 0.5
zona_superior = frequencia_maxima * 0.85

print(f"A frequência cardíaca máxima é: {frequencia_maxima} bpm")
print(f"A zona de frequência cardíaca ideal está entre {zona_inferior:.0f} bpm e {zona_superior:.0f} bpm")

# Cálculo do VO2 máximo
sexo = input("Digite o sexo do paciente (M para masculino, F para feminino): ").strip().upper()
frequencia_repouso = int(input("Digite a frequência cardíaca de repouso do paciente (em bpm): "))

if sexo == "M":
    vo2_maximo = 15.3 * (frequencia_maxima / frequencia_repouso)
elif sexo == "F":
    vo2_maximo = 14.7 * (frequencia_maxima / frequencia_repouso)
else:
    print("Sexo inválido. O cálculo do VO2 máximo não será realizado.")
    vo2_maximo = None

if vo2_maximo:
    print(f"O VO2 máximo estimado do paciente é: {vo2_maximo:.2f} ml/kg/min")