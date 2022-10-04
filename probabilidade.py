import math


def funcao_de_probabilidade_binomial(k: float, n: int, p: float):
    return math.comb(n, k) * math.pow(p, k) * math.pow((1 - p), (n - k))
