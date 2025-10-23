"""
Arquivo de configuração do projeto de otimização (DEAP + Rastrigin)
"""

# ====== PARÂMETROS DO AG ======
POP_SIZE = 100        # Tamanho da população
N_GER = 250           # Número de gerações
PROB_CX = 0.8         # Probabilidade de cruzamento
PROB_MT = 0.1         # Probabilidade de mutação
SEED = 42             # Semente aleatória (para reprodutibilidade)
TRIALS = 30           # Número de rodadas do algoritmo

# ======= PARÂMETROS DO PROBLEMA ========
IND_SIZE = 10         # Dimensão de indivíduo (número de variáveis)
BOUND_LOW = -5.12     # Limite inferior
BOUND_UP = 5.12       # LImite superios

# ======= PARÂMETROS μ e λ ========
MU = 150              # Numero de pais
_LAMBDA = 200         # Numero de filhos