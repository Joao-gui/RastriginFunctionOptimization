"""
Arquivo de configuração do projeto de otimização (DEAP + Rastrigin)
"""

# ====== PARÂMETROS DO AG ======
POP_SIZE = 5         # Tamanho da população
N_GER = 100          # Número de gerações
PROB_CX = 0.7        # Probabilidade de cruzamento
PROB_MT = 0.2        # Probabilidade de mutação
SEED = 42            # Semente aleatória (para reprodutibilidade)
TRIALS = 20          # Número de rodadas do algoritmo

# ======= PARÂMETROS DO PROBLEMA ========
IND_SIZE = 5        # Dimensão de indivíduo (número de variáveis)
BOUND_LOW = -5.12   # Limite inferior
BOUND_UP = 5.12     # LImite superios

# ======= PARÂMETROS μ e λ ========
MU = 50             # Numero de pais
_LAMBDA = 100       # Numero de filhos