"""
Leia 5 valores e armazene em uma lista.
Mostre a soma.
"""

import os
os.system('cls')

lista = []
soma = 0

for i in range(5):
    n = int(input())
    lista.append(n)
    soma = soma + n
print(soma)
