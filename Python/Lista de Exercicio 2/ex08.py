import os
os.system('cls')

n = int(input("Digite um numero(-1 Finaliza o Programa) "))
menor = n
while n >= 0:
    if n < menor:
        menor = n
    n = int(input("Digite um numero(-1 Finaliza o Programa) "))
print(menor)