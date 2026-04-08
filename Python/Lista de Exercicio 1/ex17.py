"""
17) Sistema de notas com conceito. Leia a nota de um aluno (0 a 10) e classifique:

>= 9  classificação  "Excelente"; 
>= 7  classificação  "Bom";  
>= 5  classificação  "Regular "; 
  < 5  classificação  "Insuficiente".

Além disso:

Se a nota for menor que 0 ou maior que 10, mostre "Nota invalida".
"""

import os
os.system('cls')

nota = float(input("Digite a nota do aluno: "))
if((nota < 0) or (nota > 10)):
    print("Nota invalida")
elif(nota >= 9):
    print("Excelente")
elif(nota >= 7):
    print("Bom")
elif(nota >= 5):
    print("Regular")
elif(nota < 5):
    print("Insuficiente")