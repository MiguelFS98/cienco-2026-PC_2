import os
os.system('cls')

temp = float(input("Digite a Temperatura atual: "))
if(temp >= 30):
    print("Muito quente")
elif(temp >= 20):
    print("Agradavel")
elif(temp >= 10):
    print("Frio")
#elif(temp < 10):
else:
    print("Muito frio")