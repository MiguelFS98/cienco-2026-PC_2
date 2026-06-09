#Sistema de controle de Notas:
"""
Uma escola deseja realizar uma análise simples das notas obtidas pelos
alunos durante o semestre.
Cada aluno realizou:
Prova 1
Prova 2
Prova 3

Utilize uma matriz 5 x 3 para armazenar:
5 alunos
3 notas para cada aluno
As notas devem ser informadas pelo usuário.

Após preencher a matriz, o programa deve calcular:
Média de cada aluno
Média geral da turma
Maior nota da turma
Menor nota da turma

Apresentar:
Notas cadastradas
Média de cada aluno
Média geral
Maior nota encontrada
Menor nota encontrada

Utilizar obrigatoriamente:
Lista de listas (matriz)
for
if
"""
matriz = []
media_alunos = []
soma_turma = 0
maior_nota = None
menor_nota = None

for i in range(5):
    linha = []
    for j in range(3):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

for i in range(5):
    soma_aluno = 0
    for j in range(3):
        soma_aluno += matriz[i][j]
        soma_turma += matriz[i][j]
        if maior_nota is None or matriz[i][j] > maior_nota:
            maior_nota = matriz[i][j]
        if menor_nota is None or matriz[i][j] < menor_nota:
            menor_nota = matriz[i][j]
    media_alunos.append(soma_aluno / 3)

media_turma = soma_turma / 15

print("Notas cadastradas:")
for i in range(5):
    print(matriz[i])    
print("Média de cada aluno:")
for i in range(5):
    print(f"Aluno {i+1}: {media_alunos[i]:.2f}")
print(f"Média geral da turma: {media_turma:.2f}")
print(f"Maior nota encontrada: {maior_nota:.2f}")
print(f"Menor nota encontrada: {menor_nota:.2f}")   

