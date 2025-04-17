class Recomendacao:
    def __init__(self, paciente):
        self.paciente = paciente

    def gerar_plano_tratamento(self):
        plano = []
        
        if self.paciente.idade < 18:
            plano.append("Incluir exercícios de mobilidade e fortalecimento.")
            plano.append("Focar em atividades lúdicas e recreativas.")
        elif 18 <= self.paciente.idade < 60:
            plano.append("Incluir exercícios aeróbicos e de resistência.")
            plano.append("Trabalhar na correção postural.")
        else:
            plano.append("Focar em exercícios de equilíbrio e flexibilidade.")
            plano.append("Incluir atividades de baixo impacto.")

        if self.paciente.sexo == "F":
            plano.append("Considerar exercícios que promovam a saúde óssea.")
        
        if self.paciente.condicoes_saude:
            plano.append("Adaptar os exercícios conforme as condições de saúde do paciente.")

        return plano

    def exibir_plano(self):
        plano = self.gerar_plano_tratamento()
        print("Plano de Tratamento Recomendado:")
        for item in plano:
            print(f"- {item}")