"""
Conte quantos números são positivos em uma lista.
"""

import os
os.system('cls')

lista = [-1, -2, 3, 4, 5]
contador = 0

for valor in lista:
    if valor > 0:
        contador = contador + 1
print("A lista contem", contador, "números positivos")