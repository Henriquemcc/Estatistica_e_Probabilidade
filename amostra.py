import histograma
import tendencia
import variabilidade


def calcular_tudo(amostra: list):
    """
    Calcula tudo de tendência central, variabilidade e histograma e imprime na tela
    :param amostra: Lista contendo os valores da amostra
    """

    # Média
    media = tendencia.calcular_media(amostra)
    print("Média:", media)

    # Mediana
    mediana = tendencia.calcular_mediana(amostra)
    print("Mediana:", mediana)

    # Moda
    moda = tendencia.calcular_moda(amostra)
    print("Moda:", moda)

    # Ponto média
    ponto_medio = tendencia.calcular_ponto_medio(amostra)
    print("Ponto médio:", ponto_medio)

    # Desvio padrão
    desvio_padrao = variabilidade.calcular_desvio_padrao(amostra)
    print("Desvio padrão:", desvio_padrao)

    # Coeficiente de variação
    coeficiente_variacao = variabilidade.calcular_coeficiente_variacao(amostra)
    print("Coeficiente de variação:", str(coeficiente_variacao) + "%")
    if coeficiente_variacao <= 20:
        print("Homogêneo")
    elif coeficiente_variacao > 20:
        print("Heterogêneo")

    # Escore padronizado
    escore_padronizado = variabilidade.calcular_escore_padronizado(amostra)
    print("Escore padronizado:", escore_padronizado)

    # Quartil 1
    quartil_1 = histograma.obter_quartil(amostra, 1)
    print("Quartil 1:", quartil_1)

    # Quartil 2
    quartil_2 = histograma.obter_quartil(amostra, 2)
    print("Quartil 2:", quartil_2)

    # Quartil 3
    quartil_3 = histograma.obter_quartil(amostra, 3)
    print("Quartil 3:", quartil_3)

    # Amplitude interquartil
    amplitude_interquartil = histograma.calcular_amplitude_interquartil(amostra)
    print("Amplitude interquartil (IQR):", amplitude_interquartil)

    # Outliers
    outliers = histograma.obter_outliers(amostra)
    print("Outliers:", outliers)

    # Outliers extremos
    outliers_extremos = histograma.obter_outliers_extremos(amostra)
    print("Outliers extremos:", outliers_extremos)
