class Paciente:
    def __init__(self, nome, idade, sexo, frequencia_repouso, condicoes_saude):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.frequencia_repouso = frequencia_repouso
        self.condicoes_saude = condicoes_saude

    def validar_dados(self):
        # Validação dos dados do paciente
        return self.idade > 0 and self.frequencia_repouso > 0