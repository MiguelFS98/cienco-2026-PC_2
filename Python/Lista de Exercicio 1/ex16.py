"""
16) Classificação de triângulo. Leia três valores representando os lados de um triângulo. Verifique:

1) Se é possível formar um triângulo (a soma de dois lados deve ser maior que o terceiro) 

2) Caso seja possível, classifique como:

Equilatero (todos os lados iguais);
Isosceles (dois lados iguais);
Escaleno (todos diferentes).
"""

import os
os.system('cls')

x = float(input("digite o valor de x: "))
y = float(input("digite o valor de y: "))
z = float(input("digite o valor de z: "))

if((x + y > z) and (z + x > y) and (z + y > x)):
    if(x == y == z):
        print("Equilatero")
    elif((x == y) or (x == z)):
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("Não é possivel formar um triângulo")
