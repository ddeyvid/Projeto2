#kaua
#adrian
#lucas#qualquer coisa


import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print(media_salarial)

def grupo():
    funcionarios_acima = 0
media = np.mean(salarios)
funcionarios_acima = np.sum(salarios > media)
print(f"A média salarial é: {media:.2f}")
print(f"O número de funcionários com salário acima da média é: {funcionarios_acima}")

grupo()