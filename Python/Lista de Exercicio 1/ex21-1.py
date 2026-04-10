"""
21.1) Criação dos exercícios

Você deverá elaborar 3 exercícios próprios, sendo:

- 1 exercício utilizando apenas IF;
- 1 exercício utilizando IF e ELSE;
- 1 exercício utilizando IF, ELIF e ELSE.

Cada exercício deve:

Ter um enunciado claro e contextualizado, diferente dos que já foram apresentados e resolvidos;
Fazer sentido no mundo real (exemplo: notas, idade, salário, comissão, valor de venda, custo de km de por litro, custo de viagem, etc.);
Indicar claramente o que deve ser exibido como saída.
"""
# Exercício 1 - IF

import os
os.system('cls')

num1 = float(input("Digite um numero: "))
if(num1 > 0):
    print("Valor informado é maior que zero!!!")

# Exercício 2 - IF e ELSE

import os
os.system('cls')

num1 = float(input("Digite um numero: "))
if(num1 > 0):
    print("Valor informado é maior que zero!!!")
else:
    print("Valor informado é menor ou igual a zero!!!")

# Exercício 3 - IF, ELIF e ELSE

import os
os.system('cls')

num1 = float(input("Digite um numero: "))
if(num1 > 0):
    print("Valor informado é maior que zero!!!")
elif(num1 < 0):
    print("Valor informado é menor que zero!!!")
else:
    print("Valor informado é igual a zero!!!")
    