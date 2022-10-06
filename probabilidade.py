import math


def funcao_variavel_aleatoria_distribuicao_binomial(n, p, x):
    return math.comb(n, x) * math.pow(p, x) * math.pow((1 - p), (n - x))


def funcao_variavel_aleatoria_distribuicao_hipergeometrica(N, A, n, x):
    return math.comb(A, x) * math.comb(N - A, n - x) / math.comb(N, n)
