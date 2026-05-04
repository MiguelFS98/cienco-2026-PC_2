import os
os.system('cls')

n = int(input("Digite um numero(-1 Finaliza o Programa) "))
maior = n
while n != -1:
    if n > maior:
        maior = n
    n = int(input("Digite um numero(-1 Finaliza o Programa) "))
print(maior)