import os
os.system('cls')

soma = 0
contador = 0
media = 0
n = float(input("Digite um numero(-1 Finaliza o Programa) "))
while n != -1:
    soma = soma + n
    contador = contador + 1
    n = float(input("Digite um numero(-1 Finaliza o Programa) "))
    media = soma / contador
print(media)