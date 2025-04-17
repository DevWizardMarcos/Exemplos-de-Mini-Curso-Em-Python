nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
sexo = input("Digite o sexo do paciente (M para masculino, F para feminino): ").strip().upper()
frequencia_repouso = int(input("Digite a frequência cardíaca de repouso do paciente (em bpm): "))
condicoes_saude = input("Digite as condições de saúde do paciente (separadas por vírgula): ").strip()

# Aqui você pode instanciar a classe Paciente e a classe Recomendacao
# do módulo de serviços para gerar um plano de tratamento.

from services.recomendacao import Recomendacao
from models.paciente import Paciente

# Criação do objeto Paciente
paciente = Paciente(
    nome=nome,
    idade=idade,
    sexo=sexo,
    frequencia_repouso=frequencia_repouso,
    condicoes_saude=condicoes_saude
)

# Verificação se os dados do paciente são válidos
if paciente.validar_dados():
    recomendacao = Recomendacao()
    plano_tratamento = recomendacao.gerar_plano(paciente)
    print(plano_tratamento)
else:
    print("Dados do paciente inválidos. Verifique as informações fornecidas.")