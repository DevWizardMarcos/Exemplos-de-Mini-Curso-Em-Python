import unittest
from src.services.recomendacao import Recomendacao
from src.models.paciente import Paciente

class TestRecomendacao(unittest.TestCase):

    def setUp(self):
        self.paciente1 = Paciente(nome="João", idade=30, sexo="M", frequencia_repouso=70, condicoes_saude=[])
        self.paciente2 = Paciente(nome="Maria", idade=25, sexo="F", frequencia_repouso=65, condicoes_saude=["lesão no joelho"])
        self.recomendacao = Recomendacao()

    def test_recomendacao_tratamento_basico(self):
        plano = self.recomendacao.gerar_plano(self.paciente1)
        self.assertIn("exercícios aeróbicos", plano)
        self.assertIn("alongamentos", plano)

    def test_recomendacao_tratamento_avancado(self):
        plano = self.recomendacao.gerar_plano(self.paciente2)
        self.assertIn("fisioterapia para lesão no joelho", plano)
        self.assertIn("exercícios de fortalecimento", plano)

    def test_recomendacao_sexo(self):
        plano_masculino = self.recomendacao.gerar_plano(self.paciente1)
        plano_feminino = self.recomendacao.gerar_plano(self.paciente2)
        self.assertNotEqual(plano_masculino, plano_feminino)

    def test_recomendacao_idade(self):
        plano_jovem = self.recomendacao.gerar_plano(Paciente(nome="Ana", idade=20, sexo="F", frequencia_repouso=60, condicoes_saude=[]))
        plano_idoso = self.recomendacao.gerar_plano(Paciente(nome="Carlos", idade=70, sexo="M", frequencia_repouso=75, condicoes_saude=[]))
        self.assertNotEqual(plano_jovem, plano_idoso)

if __name__ == '__main__':
    unittest.main()