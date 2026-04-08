import os
os.system('cls')

compra = float(input("insira o valor da compra: "))
if(compra >= 100):
    print("Desconto Aprovado!")
else:
    print("Desconto Reprovado!")