import unittest
from src.services.calculos import calcular_frequencia_maxima, calcular_vo2_maximo

class TestCalculos(unittest.TestCase):

    def test_calcular_frequencia_maxima(self):
        idade = 30
        resultado = calcular_frequencia_maxima(idade)
        self.assertEqual(resultado, 190)  # 220 - 30

    def test_calcular_vo2_maximo_masculino(self):
        frequencia_maxima = 190
        frequencia_repouso = 60
        resultado = calcular_vo2_maximo('M', frequencia_maxima, frequencia_repouso)
        self.assertAlmostEqual(resultado, 47.25, places=2)  # 15.3 * (190 / 60)

    def test_calcular_vo2_maximo_feminino(self):
        frequencia_maxima = 190
        frequencia_repouso = 60
        resultado = calcular_vo2_maximo('F', frequencia_maxima, frequencia_repouso)
        self.assertAlmostEqual(resultado, 46.85, places=2)  # 14.7 * (190 / 60)

    def test_calcular_vo2_maximo_sexo_invalido(self):
        frequencia_maxima = 190
        frequencia_repouso = 60
        resultado = calcular_vo2_maximo('X', frequencia_maxima, frequencia_repouso)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()