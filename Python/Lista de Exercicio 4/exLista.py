"""
__________________________________________________________

Curso: Ciência da Computação
Disciplina: Programação de Computadores II
Assunto: Procedimentos e Funções em Python
Tarefa: Sistema de Controle de Notas
Data:  11/05/2026
__________________________________________________________

Sistema de Controle de Notas em Python

Uma escola deseja começar a informatizar parte do controle das notas dos alunos. 

Para isso, você deverá desenvolver um programa em Python utilizando os conceitos de procedimentos e funções trabalhados em aula. 

O objetivo desta atividade é justamente praticar a organização do programa em módulos menores, tornando o código mais organizado, reutilizável e fácil de entender.

__________________________________________________________

O programa deverá funcionar da seguinte forma:
__________________________________________________________

O usuário deverá informar várias notas.

O programa continuará executando até que seja digitado o valor -1, indicando o encerramento da entrada de dados.

Durante o processamento, o sistema deverá:

- Somar as notas;
- Contar quantas notas foram informadas;
- Identificar a maior nota;
- Identificar a menor nota;
- Classificar cada nota informada.

__________________________________________________________

Classificação das notas
__________________________________________________________

Nota menor que 4 = aluno em situação crítica;
Nota 4 até 6.99 = aluno em recuperação;
Nota maior ou igual a 7 = aluno aprovado.

O programa deverá contar:

Quantos alunos ficaram em situação crítica;
Quantos ficaram em recuperação;
Quantos foram aprovados.

__________________________________________________________

IMPORTANTE
__________________________________________________________

Esta atividade DEVE utilizar procedimentos e funções.

O objetivo NÃO é fazer tudo diretamente no programa principal.

Você deverá organizar o código utilizando chamadas de funções e procedimentos.

__________________________________________________________

O programa deverá possuir:
__________________________________________________________

1) Um procedimento para mostrar o menu/título do sistema;

2) Uma função para calcular a média das notas;

3) Uma função para classificar uma nota;

4) Um procedimento para mostrar os resultados finais.

__________________________________________________________

Fluxo esperado do programa
__________________________________________________________

O programa principal deverá:

- Chamar o procedimento de apresentação;
- Ler as notas;
- Chamar a função de classificação;
- Atualizar os contadores;
- Chamar a função que calcula a média;
- Chamar o procedimento responsável por mostrar os resultados finais.

__________________________________________________________

Ao final, mostrar:
__________________________________________________________

- Quantidade de notas informadas;
- Média das notas;
- Maior nota;
- Menor nota;
- Quantidade de alunos aprovados;
- Quantidade em recuperação;
- Quantidade em situação crítica.

__________________________________________________________

Regras importantes
__________________________________________________________

- O valor -1 serve apenas para encerrar;
- O valor -1 NÃO deve participar dos cálculos;
- Não utilizar listas;
- Utilizar while;
- Utilizar if / elif / else;
- Utilizar obrigatoriamente procedimentos e funções.

__________________________________________________________

ESTRUTURA ESPERADA (exemplo)
__________________________________________________________

def mostrar_titulo():
    ...

def calcular_media(total, quantidade):
    ...

def classificar_nota(nota):
    ...

def mostrar_resultados(...):
    ...

# programa principal
mostrar_titulo()

while ...:
    ...

media = calcular_media(...)

mostrar_resultados(...)

__________________________________________________________
"""

import os
os.system('cls')

def mostrar_titulo():
    print("Sistema de Controle de Notas")
    print("---------------------------")

def calcular_media(total, quantidade):
    if quantidade > 0:
        return total / quantidade
    else:
        return 0

def classificar_nota(nota):
    if nota < 4:
        return "Crítica"
    elif 4 <= nota < 7:
        return "Recuperação"
    else:
        return "Aprovado"
    
def mostrar_resultados(quantidade, media, maior, menor, aprovados, recuperacao, critica):
    print("\nResultados Finais:")
    print(f"Quantidade de notas informadas: {quantidade}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Quantidade de alunos aprovados: {aprovados}")
    print(f"Quantidade em recuperação: {recuperacao}")
    print(f"Quantidade em situação crítica: {critica}")

# programa principal
mostrar_titulo()

total_notas = 0
quantidade_notas = 0
maior_nota = float('-inf')
menor_nota = float('inf')
aprovados = 0
recuperacao = 0
critica = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    elif 0 <= nota <= 10:
        total_notas += nota
        quantidade_notas += 1
        maior_nota = max(maior_nota, nota)
        menor_nota = min(menor_nota, nota)
        
        classificacao = classificar_nota(nota)
        if classificacao == "Aprovado":
            aprovados += 1
        elif classificacao == "Recuperação":
            recuperacao += 1
        else:
            critica += 1
    else:
        print("Nota inválida. Digite um valor entre 0 e 10.")

media = calcular_media(total_notas, quantidade_notas)

mostrar_resultados(quantidade_notas, media, maior_nota, menor_nota, aprovados, recuperacao, critica)