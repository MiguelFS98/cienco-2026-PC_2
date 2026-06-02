"""
-------------------------------------------------------------------------------------
Curso: Ciência da Computação
Disciplina: Programação de Computadores II
Assunto: Estruturas básicas de programação em linguagem Python
Data: 01/06/2026
Data da devolução: 01/06/2026
-------------------------------------------------------------------------------------

1-) Desenvolva o enunciado e a resolução de um problema a ser resolvido computacionamente utilizando a linguagem de programação Python para cada uma das estruturas a seguir:


1.1) Estrutura de decisão if / elif / else


1.2.) Estrutura de repetição for


1.3) Estrutura de repetição while


1.4) Vetor (lista)


1.5) Matriz (lista de lista)


1.6) Procedimento sem retorno


1.7) Procedimento com retorno


1.8) Função sem retorno


1.9) Função com retorno

-------------------------------------------------------------------------------------
"""

# 1.1) Estrutura de decisão if / elif / else

#Escreva um programa que solicite ao usuário um número inteiro e determine se ele é positivo, negativo ou zero.

"""
numero = int(input("Digite um número inteiro: "))


if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
"""
    
# 1.2.) Estrutura de repetição for

#Escreva um programa que imprima os números de 1 a 10 usando um loop for.

"""
for i in range(1, 11):
    print(i)
"""

# 1.3) Estrutura de repetição while

#Escreva um programa que solicite ao usuário um número inteiro e imprima a contagem regressiva até zero usando um loop while.

"""
numero = int(input("Digite um número inteiro: "))

while numero >= 0:
    print(numero)
    numero -= 1
"""

# 1.4) Vetor (lista)

#Escreva um programa que solicite ao usuário 5 números inteiros, armazene-os em uma lista e imprima a soma dos números.

"""
numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
soma = sum(numeros)
print("A soma dos números é:", soma)
"""

# 1.5) Matriz (lista de lista)

#Escreva um programa que crie uma matriz 3x3, preencha-a com números inteiros e imprima a matriz.

"""
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite um número inteiro para a posição [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)
print("Matriz 3x3:")
for linha in matriz:
    print(linha)
"""

# 1.6) Procedimento sem retorno

#Escreva um procedimento que receba um número inteiro e imprima se ele é par ou ímpar.

"""
def verificar_paridade(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
numero = int(input("Digite um número inteiro: "))
verificar_paridade(numero)
"""

# 1.7) Procedimento com retorno

#Escreva um procedimento que receba um número inteiro e retorne o dobro desse número.

"""
def calcular_dobro(numero):
    return numero * 2
numero = int(input("Digite um número inteiro: "))
dobro = calcular_dobro(numero)
print("O dobro do número é:", dobro)
"""

# 1.8) Função sem retorno

#Escreva uma função que receba um número inteiro e imprima a tabuada desse número.

"""
def imprimir_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Digite um número inteiro: "))
imprimir_tabuada(numero)
"""

# 1.9) Função com retorno

#Escreva uma função que receba um número inteiro e retorne a soma dos números de 1 até esse número.

"""
def calcular_soma(numero):
    return sum(range(1, numero + 1))
numero = int(input("Digite um número inteiro: "))
soma = calcular_soma(numero)
print("A soma dos números de 1 até", numero, "é:", soma)
"""