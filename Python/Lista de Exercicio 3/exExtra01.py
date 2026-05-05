"""
__________________________________________________________
Curso: Ciência da Computação
Disciplina: Programação de Computadores II
Assunto: Revisão de conceitos e práticas estrutura de decisão e repetição
Tarefa: Sistema de Controle de Vendas (básico) em Python - Versão 1
Data: 04/05/2026 (atividade a ser realizada em sala/aula)
__________________________________________________________

VERSÃO 1 - Sistema de Controle de Vendas (básico) em Python

Uma pequena loja está começando a informatizar o controle de suas vendas diárias. Para isso,
 você deverá desenvolver um programa em Python que permita registrar várias vendas realizadas ao longo do dia.

O programa deve funcionar da seguinte forma:

- O usuário deve informar o valor de uma venda
- O programa deve continuar solicitando valores até que seja digitado 0, indicando o encerramento

Durante o processamento, o sistema deve:

Somar o valor total vendido
Contar quantas vendas foram realizadas
Identificar o maior valor de venda
Identificar o menor valor de venda

Ao final, o programa deve mostrar:

- Total vendido;
- Quantidade de vendas;
- Média das vendas;
- Maior venda;
- Menor venda.

Regras importantes:

- A primeira venda válida deve ser usada como base para maior e menor;
- Não utilizar listas;
- Utilizar estrutura de repetição (while);
- Utilizar estruturas de decisão (if / elif / else).
"""

import os
os.system('cls')

somaVendas = 0
qntVendas = 0
mediaVendas = 0
valorVendas = float(input("Digite o valor da venda(digitando 0 ira finalizar o programa!!) "))
menor = valorVendas
maior = valorVendas
while valorVendas != 0:
    if valorVendas < menor:
        menor = valorVendas
    elif valorVendas > maior:
        maior = valorVendas
    somaVendas = somaVendas + valorVendas
    qntVendas = qntVendas + 1
    valorVendas = float(input("Digite o valor da venda(digitando 0 ira finalizar o programa!!) "))
    mediaVendas = somaVendas / qntVendas
print(somaVendas)
print(qntVendas)
print(mediaVendas)
print(maior)
print(menor)