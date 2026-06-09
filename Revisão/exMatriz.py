
#Criando uma Matriz:
"""
matriz = [
[ 10, 20, 30],
[ 40, 50, 60]
]

print(matriz)
#Matriz 2 x 3
#2 linhas
#3 colunas
"""
"""
#Acessando posições da Matriz:

matriz = [
[10, 20, 30],
[40, 50, 60]
]

print(matriz[0][1])
print(matriz[1][2])

#Saída:
#20
#60
"""
"""
#Percorrendo uma Matriz:

for i in range(2):
    for j in range(3):
    print(matriz[ i ][ j ])
#Utilizamos dois laços:
#um para as linhas
#um para as colunas
"""
"""
#Exibindo a Matriz em Formato Matricial:

matriz = [
[10, 20, 30],
[40, 50, 60]
]

for i in range(2):
    for j in range(3):
        print(matriz[ i ][ j ] ,
            end=" ")
    print()

#Saída:
#102030
#405060
"""
"""
#Preenchimento interativo de matriz
matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input())
        linha.append( valor )
    matriz.append( linha )
"""