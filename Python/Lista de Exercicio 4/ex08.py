import os
os.system('cls')

def validar(num):
    if num < 0:
        print(num, "é Negativo!!!")
    elif num == 0:
        print("Zero é Zero")
    else:
        print(num, "é Positivo!!!")

validar(-1)