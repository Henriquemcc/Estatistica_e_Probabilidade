import math
import tendencia


def calcular_somatorio(x: list):
    """
    Calcula o somatório dos elementos de uma lista.
    :param x: Lista cujos elementos serão somados.
    :return: Soma de todos os elementos da lista.
    """
    somatorio = 0
    for xi in x:
        somatorio += xi

    return somatorio


def calcular_somatorio_ao_quadrado(x: list):
    """
    Calcula a soma dos elementos de uma lista ao quadrado.
    :param x: Lista cujos elementos serão elevados a dois e depois somados.
    :return: Soma ao quadrado de todos os elementos da lista.
    """
    somatorio_ao_quadrado = 0
    for xi in x:
        somatorio_ao_quadrado += math.pow(xi, 2)

    return somatorio_ao_quadrado


def calcular_sxx_ou_syy(x: list):
    """
    Calcula o Sxx ou Syy de uma lista. Caso a lista seja x será o Sxx, caso a lista seja y será o Syy.
    :param x: Lista a ser calculado o Sxx ou Syy.
    :return: Sxx ou Syy da lista.
    """
    n = len(x)
    somatorio_x_ao_quadrado = calcular_somatorio_ao_quadrado(x)
    somatorio_x = calcular_somatorio(x)

    return n * somatorio_x_ao_quadrado - math.pow(somatorio_x, 2)


def calcular_somatorio_xy(x: list, y: list):
    """
    Calcula o somatório dos elementos xi com os elementos yi. Sendo xi da lista x e yi da lista y.
    :param x: Lista x a ter seus elementos xi multiplicados com yi e somados.
    :param y: Lista y a ter seus elementos yi multiplicados com xi e somados.
    :return: Soma dos elementos xi multiplicados com yi.
    """
    if len(x) != len(y):
        raise "As listas possuem tamanhos diferentes"

    somatorio_xy = 0

    for i in range(len(x)):
        somatorio_xy += x[i] * y[i]

    return somatorio_xy


def calcular_sxy(x: list, y: list):
    """
    Calcula o valor da variável de regressão Sxy.
    :param x: Lista X.
    :param y: Lista Y.
    :return: Valor da variável de regressão Sxy.
    """
    if len(x) != len(y):
        raise "As listas possuem tamanhos diferentes"

    n = len(x)
    somatorio_xy = calcular_somatorio_xy(x, y)
    somatorio_x = calcular_somatorio(x)
    somatorio_y = calcular_somatorio(y)

    return n * somatorio_xy - somatorio_x * somatorio_y


def calcular_correlacao_simples(x: list, y: list):
    """
    Calcula a correlação amostral simples.
    :param x: Lista X.
    :param y: Lista Y
    :return: Correlação amostral simples das listas X e Y.
    """
    if len(x) != len(y):
        raise "As listas possuem tamanhos diferentes"

    sxy = calcular_sxy(x, y)
    sxx = calcular_sxx_ou_syy(x)
    syy = calcular_sxx_ou_syy(y)

    return sxy / math.sqrt(sxx * syy)


def calcular_b_um(x: list, y: list):
    """
    Calcula o valor da variável de regressão 𝛽1.
    :param x: Lista X.
    :param y: Lista Y.
    :return: Valor da variável de regressão 𝛽1.
    """
    if len(x) != len(y):
        raise "As listas possuem tamanhos diferentes"

    sxy = calcular_sxy(x, y)
    sxx = calcular_sxx_ou_syy(x)

    return sxy / sxx


def calcular_b_zero(x: list, y: list):
    """
    Calcula o valor da veriável de regressão 𝛽0.
    :param x: Lista X.
    :param y: Lista Y.
    :return: Valor da variável de regressão 𝛽0.
    """
    if len(x) != len(y):
        raise "As listas possuem tamanhos diferentes"

    media_y = tendencia.calcular_media(y)
    media_x = tendencia.calcular_media(x)
    b_um = calcular_b_um(x, y)

    return media_y - b_um * media_x


def calcular_equacao_da_reta(x: list, y: list):
    """
    Calcula a equação da reta.
    :param x: Lista X.
    :param y: Lista Y.
    :return: String com a equação da reta.
    """
    if len(x) != len(y):
        raise "As listas possuem tamanhos diferentes"

    b_zero = calcular_b_zero(x, y)
    b_um = calcular_b_um(x, y)

    return "y = {} + {}𝑥 + 𝜀".format(b_zero, b_um)
