from unittest import TestCase

import histograma


class Test(TestCase):
    def test_obter_quartil(self):
        amostra = [70, 80, 37, 61, 64, 74, 75, 38, 67, 56, 70, 72, 61, 66, 58, 68, 70, 68, 58, 58, 63]
        quartil_1 = histograma.obter_quartil(amostra, 1)
        self.assertEqual(quartil_1, 58)
        quartil_3 = histograma.obter_quartil(amostra, 3)
        self.assertEqual(quartil_3, 70)

    def test_calcular_amplitude_interquartil(self):
        amostra = [8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 14, 14,
                   15, 16, 17]
        amplitude_interquartil = histograma.calcular_amplitude_interquartil(amostra)
        self.assertEqual(amplitude_interquartil, 4)

        amostra = [70, 80, 37, 61, 64, 74, 75, 38, 67, 56, 70, 72, 61, 66, 58, 68, 70, 68, 58, 58, 63]
        amplitude_interquartil = histograma.calcular_amplitude_interquartil(amostra)
        self.assertEqual(amplitude_interquartil, 12)

    def test_calcular_lower_fence(self):
        pass

    def test_calcular_upper_fence(self):
        pass

    def test_obter_outliers(self):
        amostra = [70, 80, 37, 61, 64, 74, 75, 38, 67, 56, 70, 72, 61, 66, 58, 68, 70, 68, 58, 58, 63]
        outliers = histograma.obter_outliers(amostra)

        self.assertEqual(len(outliers), 2)
        self.assertEqual(37 in outliers, True)
        self.assertEqual(38 in outliers, True)

    def test_calcular_extreme_lower_fence(self):
        pass

    def test_calcular_extreme_upper_fence(self):
        pass

    def test_obter_outliers_extremos(self):
        amostra = [70, 80, 37, 61, 64, 74, 75, 38, 67, 56, 70, 72, 61, 66, 58, 68, 70, 68, 58, 58, 63]
        outliers_extremos = histograma.obter_outliers_extremos(amostra)
        self.assertEqual(len(outliers_extremos), 0)
