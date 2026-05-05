"""
Leia 5 números e mostre o maior.
"""

import os
os.system('cls')

lista = []

for i in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)

maior = lista[0]

for valor in lista:
    if valor > maior:
        maior = valor
print("O maior Numero é ", maior)