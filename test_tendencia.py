from unittest import TestCase

import tendencia


class Test(TestCase):
    def test_calcular_media(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        self.assertEqual(tendencia.calcular_media(amostra), 41.5)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        self.assertEqual(tendencia.calcular_media(amostra), 41.5)

    def test_calcular_mediana(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        self.assertEqual(tendencia.calcular_mediana(amostra), 42)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        self.assertEqual(tendencia.calcular_mediana(amostra), 42)

    def test_calcular_frequencia(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        frequencia = tendencia.calcular_frequencia(amostra)
        self.assertEqual(frequencia[36], 2)
        self.assertEqual(frequencia[37], 1)
        self.assertEqual(frequencia[38], 1)
        self.assertEqual(frequencia[41], 1)
        self.assertEqual(frequencia[43], 2)
        self.assertEqual(frequencia[47], 3)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        frequencia = tendencia.calcular_frequencia(amostra)
        self.assertEqual(frequencia[13], 1)
        self.assertEqual(frequencia[22], 1)
        self.assertEqual(frequencia[28], 1)
        self.assertEqual(frequencia[32], 1)
        self.assertEqual(frequencia[37], 1)
        self.assertEqual(frequencia[47], 2)
        self.assertEqual(frequencia[57], 1)
        self.assertEqual(frequencia[62], 1)
        self.assertEqual(frequencia[70], 1)

    def test_calcular_moda(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        self.assertEqual(tendencia.calcular_moda(amostra), 47)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        self.assertEqual(tendencia.calcular_moda(amostra), 47)

    def test_calcular_ponto_medio(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        self.assertEqual(tendencia.calcular_ponto_medio(amostra), 41.5)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        self.assertEqual(tendencia.calcular_ponto_medio(amostra), 41.5)
