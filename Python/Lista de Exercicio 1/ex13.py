import os
os.system('cls')

numero = int(input("Digite um numero: "))
if(numero == 0):
    print("Zero")
elif(numero > 0):
    print("Positivo")
else:
    print("Negativo")