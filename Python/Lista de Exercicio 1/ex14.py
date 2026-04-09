import os
os.system('cls')

valor = int(input("Digite o valor do produto: "))
if(valor >= 100):
    print("Produto Caro")
elif(valor >= 50):
    print("Produto intermediario")
else:
    print("Produto barato")