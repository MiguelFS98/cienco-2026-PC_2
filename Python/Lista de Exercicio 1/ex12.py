import os
os.system('cls')

idade = float(input("Digite a sua idade: "))
if(idade <= 12):
    print("Criança")
elif(idade <= 17):
    print("Adolecente")
elif(idade <= 59):
    print("Adulto")
elif(idade >= 60):
    print("Idoso")