import os
os.system('cls')

saldo = float(input("Digite seu saldo em conta: "))
if(saldo >= 1000):
    print("Cliente VIP")
else:
    print("Cliente Padrão")