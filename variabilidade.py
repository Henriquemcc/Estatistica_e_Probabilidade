# Algoritmos de Medidas de Variabilidade
import math

import tendencia


def calcular_desvio(amostra: list):
    """
    Calcula o desvio de cada valor da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Lista contendo a tupla com o valor da amostra e o desvio dele
    """
    media = tendencia.calcular_media(amostra)
    desvio = []
    for i in amostra:
        desvio.append((i, i - media))
    return desvio


def calcular_desvio_padrao(amostra: list):
    """
    Calcula o desvio padrao dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Número real com o valor do desvio padrão dos valores da amostra
    """
    desvio = calcular_desvio(amostra)
    desvio_padrao = 0
    quantidade_amostra = 0
    for i in desvio:
        desvio_padrao += math.pow(i[1], 2)
        quantidade_amostra += 1
    desvio_padrao /= (quantidade_amostra - 1)
    desvio_padrao = math.sqrt(desvio_padrao)
    return desvio_padrao


def calcular_coeficiente_variacao(amostra: list, exibir_em_porcentagem: bool = True):
    """
    Calcula o coeficiente de variação dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :param exibir_em_porcentagem: Valor booleano indicando se o coeficiente de variação deve ser multiplicado por 100
    para que possa ser mostrado em porcentagem
    :return: Número real com o coeficiente de variação dos valores da amostra
    """
    coeficiente_variacao = calcular_desvio_padrao(amostra) / tendencia.calcular_media(amostra)
    if exibir_em_porcentagem:
        coeficiente_variacao *= 100
    return coeficiente_variacao


def calcular_escore_padronizado(amostra: list):
    """
    Calcula o escore padronizado dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Lista contendo a tupla com o valor da amostra e o escore padronizado dele
    """
    desvio = calcular_desvio(amostra)
    desvio_padrao = calcular_desvio_padrao(amostra)
    escore_padronizado = []
    for i in desvio:
        escore_padronizado.append((i[0], i[1] / desvio_padrao))
    return escore_padronizado
