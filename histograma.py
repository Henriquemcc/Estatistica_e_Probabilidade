def obter_quartil(amostra: list, k: int):
    """
    Calcula o quartil k da amostra
    :param amostra: Lista contendo os valores da amostra
    :param k: Número do quartil a ser calculado (entre 1 e 3)
    :return: Valor do quartil
    """

    # Verificando se o valor passado para o parâmetro quartil é válido.
    if k < 1:
        raise ValueError("O valor k do quartil deve ser maior ou igual 1.")
    if k > 3:
        raise ValueError("O valor k do quartil deve ser menor ou igual 3.")
    if type(k) == float:
        raise ValueError("O valor k do quartil deve ser inteiro")

    # Ordenando a amostra
    amostra_ordenada = sorted(amostra)

    # Calculando a posição do quartil
    posicao_quartil = k * (len(amostra_ordenada) + 1.0) / 4.0

    # Obtendo o quartil para posição inteiras
    if posicao_quartil.is_integer():
        quartil = amostra_ordenada[int(posicao_quartil) - 1] # No python a contagem na lista começa com zero

    # Obtendo o quartil para posição fracionada
    else:
        posicao_quartil_fracionada = posicao_quartil % 1
        if posicao_quartil_fracionada == 0.25:
            quartil = (3 * amostra_ordenada[int(posicao_quartil) - 1] + amostra_ordenada[int(posicao_quartil)]) / 4 # No python a contagem na lista começa com zero
        elif posicao_quartil_fracionada == 0.5:
            quartil = (amostra_ordenada[int(posicao_quartil) - 1] + amostra_ordenada[int(posicao_quartil)]) / 2 # No python a contagem na lista começa com zero
        elif posicao_quartil_fracionada == 0.75:
            quartil = (amostra_ordenada[int(posicao_quartil) - 1] + 3 * amostra_ordenada[int(posicao_quartil)]) / 4 # No python a contagem na lista começa com zero

    return quartil

def calcular_amplitude_interquartil(amostra: list):
    """
    Calcula a amplitude interquartil (IQR)
    :param amostra: Lista contendo os valores da amostra
    :return: Valor da amplitude interquartil
    """
    return obter_quartil(amostra, 3) - obter_quartil(amostra, 1)

def calcular_lower_fence(amostra: list):
    """
    Calcula a lower fence
    :param amostra: Lista contendo os valores da amostra
    :return: Valor da lower fence
    """
    return obter_quartil(amostra, 1) - 1.5 * calcular_amplitude_interquartil(amostra)

def calcular_upper_fence(amostra: list):
    """
    Calcula a upper fence
    :param amostra: Lista contendo os valores da amostra
    :return: Valor da upper fence
    """
    return obter_quartil(amostra, 3) + 1.5 * calcular_amplitude_interquartil(amostra)

def obter_outliers(amostra: list):
    """
    Obtém os outliers da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Lista com os outliers da amostra
    """
    upper_fence = calcular_upper_fence(amostra)
    lower_fence = calcular_lower_fence(amostra)

    outliers = []

    for i in amostra:
        if i > upper_fence or i < lower_fence:
            outliers.append(i)

    return outliers

def calcular_extreme_lower_fence(amostra: list):
    """
    Calcula a extreme lower fence
    :param amostra: Lista contendo os valores da amostra
    :return: Valor da extreme lower fence
    """
    return obter_quartil(amostra, 1) - 3.0 * calcular_amplitude_interquartil(amostra)

def calcular_extreme_upper_fence(amostra: list):
    """
    Calcula a extreme upper fence
    :param amostra: Lista contendo os valores da amostra
    :return: Valor da extreme upper fence
    """
    return obter_quartil(amostra, 3) + 3.0 * calcular_amplitude_interquartil(amostra)

def obter_outliers_extremos(amostra: list):
    """
    Obtém os outliers extremos da amostra
    :param amostra: Lista contendo os valores da amostra
    :return: Lista com os outliers extremos da amostra
    """
    extreme_upper_fence = calcular_extreme_upper_fence(amostra)
    extreme_lower_fence = calcular_extreme_lower_fence(amostra)

    outliers_extremos = []

    for i in amostra:
        if i > extreme_upper_fence or i < extreme_lower_fence:
            outliers_extremos.append(i)

    return outliers_extremos
