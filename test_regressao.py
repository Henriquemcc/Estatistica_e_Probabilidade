from unittest import TestCase

import regressao


class Test(TestCase):
    def test_calcular_somatorio(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        somatorio = regressao.calcular_somatorio(x)
        self.assertEqual(somatorio, 57)

        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        somatorio = regressao.calcular_somatorio(y)
        self.assertEqual(somatorio, 565)

    def test_calcular_somatorio_ao_quadrado(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        somatorio_ao_quadrado = regressao.calcular_somatorio_ao_quadrado(x)
        self.assertEqual(somatorio_ao_quadrado, 383)

        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        somatorio_ao_quadrado = regressao.calcular_somatorio_ao_quadrado(y)
        self.assertEqual(somatorio_ao_quadrado, 32581)

    def test_calcular_somatorio_xy(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        somatorio_xy = regressao.calcular_somatorio_xy(x, y)
        self.assertEqual(somatorio_xy, 3392)

    def test_calcular_sxx_ou_syy(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        sxx = regressao.calcular_sxx_ou_syy(x)
        self.assertEqual(sxx, 581)

        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        syy = regressao.calcular_sxx_ou_syy(y)
        self.assertEqual(syy, 6585)

    def test_calcular_sxy(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        sxy = regressao.calcular_sxy(x, y)
        self.assertEqual(sxy, 1715)

    def test_calcular_correlacao_simples(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        correlacao = regressao.calcular_correlacao_simples(x, y)
        self.assertEqual(round(correlacao, 4), 0.8768)

    def test_calcular_b_um(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        b_um = regressao.calcular_b_um(x, y)
        self.assertEqual(round(b_um, 4), 2.9518)

    def test_calcular_b_zero(self):
        x = [2, 3, 4, 5, 4, 6, 7, 8, 8, 10]
        y = [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]
        b_zero = regressao.calcular_b_zero(x, y)
        self.assertEqual(round(b_zero, 4), 39.6747)