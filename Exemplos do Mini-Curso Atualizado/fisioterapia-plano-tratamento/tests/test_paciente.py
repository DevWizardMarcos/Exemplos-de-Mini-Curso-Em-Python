import unittest
from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente(nome="João", idade=30, sexo="M", frequencia_repouso=70)

    def test_validar_idade(self):
        self.assertTrue(self.paciente.validar_idade(30))
        self.assertFalse(self.paciente.validar_idade(-5))

    def test_validar_sexo(self):
        self.assertTrue(self.paciente.validar_sexo("M"))
        self.assertTrue(self.paciente.validar_sexo("F"))
        self.assertFalse(self.paciente.validar_sexo("X"))

    def test_atributos_paciente(self):
        self.assertEqual(self.paciente.nome, "João")
        self.assertEqual(self.paciente.idade, 30)
        self.assertEqual(self.paciente.sexo, "M")
        self.assertEqual(self.paciente.frequencia_repouso, 70)

    def test_atualizar_frequencia_repouso(self):
        self.paciente.atualizar_frequencia_repouso(75)
        self.assertEqual(self.paciente.frequencia_repouso, 75)

if __name__ == '__main__':
    unittest.main()