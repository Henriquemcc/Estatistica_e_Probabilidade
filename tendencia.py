# Algoritmos de Medidas de Tendência Central
import math


def calcular_media(amostra: list):
    """
    Calcula a média dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Número real com a média dos valores da amostra
    """
    return sum(amostra) / len(amostra)


def calcular_mediana(amostra: list):
    """
    Calcula a mediana dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Número real com a mediana dos valores da amostra
    """
    amostra = amostra.copy()
    amostra.sort()
    if len(amostra) % 2 == 1:
        posicao_mediana = int((len(amostra) + 1) / 2)
        mediana = amostra[posicao_mediana - 1]  # No python a contagem na lista comeca com zero
    else:
        posicao_mediana_esquerda = int(math.floor((len(amostra) + 1) / 2))
        posicao_mediana_direita = int(math.ceil((len(amostra) + 1) / 2))
        mediana = (amostra[posicao_mediana_esquerda - 1] + amostra[posicao_mediana_direita - 1]) / 2
    return mediana


def calcular_frequencia(amostra: list):
    """
    Calcula a frequência de cada valor da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Dicionário contendo os valores da amostra e a frequência deles
    """
    frequencia = {}
    for i in amostra:
        if i in frequencia:
            frequencia[i] += 1
        else:
            frequencia[i] = 1
    return frequencia


def calcular_moda(amostra: list):
    """
    Calcula a moda dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Numero real com a moda dos valores da amostra
    """
    quantidade = 0
    moda = None
    for i, j in calcular_frequencia(amostra).items():
        if j > quantidade:
            quantidade = j
            moda = i
        elif j == quantidade:
            if type(moda) == list:
                moda.append(i)
            else:
                moda = [moda, i]
    return moda


def calcular_ponto_medio(amostra: list):
    """
    Calcula o ponto médio dos valores da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Numero inteiro com o valor do ponto medio dos valores da amostra
    """
    maximo = max(amostra)
    minimo = min(amostra)
    return (maximo + minimo) / 2
