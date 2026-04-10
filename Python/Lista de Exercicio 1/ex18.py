"""

18) Cálculo de imposto. Leia o salário de um funcionário e calcule o imposto de acordo com as regras a seguir:

Até 2000 é isento;  
Até 4000 aliquota de 10%;  
Acima de 4000 aliquota de 20%.

Se programa deve Mostrar:

O salário informado;
O valor do imposto;
O salário líquido.

"""

import os
os.system('cls')

salario = float(input("Digite seu salario: "))
if(salario <= 2000):
    print("\nVocê está Isento")
elif(salario <= 4000):
    print("\nAplicando Aliquota de 10%")
    print("\nSalario base: ",salario)
    salarioLiquido = salario + (salario * 0.1)
    alicota = salarioLiquido - salario
    print("Valor a adicionar: ", alicota)
    print("Salario Total: ",salarioLiquido)
elif(salario > 4000):
    print("\nAplicando Aliquota de 20%")
    print("\nSalario base: ",salario)
    salarioLiquido = salario + (salario * 0.2)
    alicota = salarioLiquido - salario
    print("Valor a adicionar: ", alicota)
    print("Salario Total: ",salarioLiquido)
else:
    print("!!!ERRO!!!ERRO!!!")