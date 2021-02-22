from unittest import TestCase

import variabilidade


class Test(TestCase):
    def test_calcular_desvio(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        desvio = variabilidade.calcular_desvio(amostra)

        self.assertEqual(desvio[0][0], 36)
        self.assertEqual(desvio[0][1], -5.5)

        self.assertEqual(desvio[1][0], 36)
        self.assertEqual(desvio[1][1], -5.5)

        self.assertEqual(desvio[2][0], 37)
        self.assertEqual(desvio[2][1], -4.5)

        self.assertEqual(desvio[3][0], 38)
        self.assertEqual(desvio[3][1], -3.5)

        self.assertEqual(desvio[4][0], 41)
        self.assertEqual(desvio[4][1], -0.5)

        self.assertEqual(desvio[5][0], 43)
        self.assertEqual(desvio[5][1], 1.5)

        self.assertEqual(desvio[6][0], 43)
        self.assertEqual(desvio[6][1], 1.5)

        self.assertEqual(desvio[7][0], 47)
        self.assertEqual(desvio[7][1], 5.5)

        self.assertEqual(desvio[8][0], 47)
        self.assertEqual(desvio[8][1], 5.5)

        self.assertEqual(desvio[9][0], 47)
        self.assertEqual(desvio[9][1], 5.5)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        desvio = variabilidade.calcular_desvio(amostra)

        self.assertEqual(desvio[0][0], 13)
        self.assertEqual(desvio[0][1], -28.5)

        self.assertEqual(desvio[1][0], 22)
        self.assertEqual(desvio[1][1], -19.5)

        self.assertEqual(desvio[2][0], 28)
        self.assertEqual(desvio[2][1], -13.5)

        self.assertEqual(desvio[3][0], 32)
        self.assertEqual(desvio[3][1], -9.5)

        self.assertEqual(desvio[4][0], 37)
        self.assertEqual(desvio[4][1], -4.5)

        self.assertEqual(desvio[5][0], 47)
        self.assertEqual(desvio[5][1], 5.5)

        self.assertEqual(desvio[6][0], 47)
        self.assertEqual(desvio[6][1], 5.5)

        self.assertEqual(desvio[7][0], 57)
        self.assertEqual(desvio[7][1], 15.5)

        self.assertEqual(desvio[8][0], 62)
        self.assertEqual(desvio[8][1], 20.5)

        self.assertEqual(desvio[9][0], 70)
        self.assertEqual(desvio[9][1], 28.5)

    def test_calcular_desvio_padrao(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        self.assertEqual(variabilidade.calcular_desvio_padrao(amostra), 4.576510072581994)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        self.assertEqual(variabilidade.calcular_desvio_padrao(amostra), 18.31362577123626)

    def test_calcular_coeficiente_variacao(self):
        amostra = [36, 36, 37, 38, 41, 43, 43, 47, 47, 47]
        self.assertEqual(variabilidade.calcular_coeficiente_variacao(amostra, True), 11.027735114655405)

        amostra = [13, 22, 28, 32, 37, 47, 47, 57, 62, 70]
        self.assertEqual(variabilidade.calcular_coeficiente_variacao(amostra, True), 44.12921872587051)

    def test_calcular_escore_padronizado(self):
        self.fail()
