"""
Leia 5 números e mostre a média.
"""

import os
os.system('cls')

lista = []
soma = 0

for i in range(5):
    n = int(input("Digite um Numero: "))
    lista.append(n)
    soma = soma + n
    media = soma / 5

print(media)