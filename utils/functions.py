import numpy as np

def rastrigin(x):
    """
    Função de Rasterigin para otimização.
    x: array ou lista de variáveis (ax: [x1, x2, x3, ...])
    Retorna o valor da função (enquanto menor, melhor para minimização)
    """
    A = 10
    x = np.array(x)
    n = len(x)
    value = A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))
    return value,