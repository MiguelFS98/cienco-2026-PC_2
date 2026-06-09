"""
Acessando os elementos da Lista:

notas = [7, 8, 6, 9, 10]
print(notas[0])
print(notas[3])

Saída: 7
       9
"""
"""
Percorrendo a Lista:

notas = [7, 8, 6, 9, 10]
for i in range(len(notas)):
    print( notas [ i ])

Saída: 7
       8
       6
       9
       10
"""

#Preenchimento interativo da Lista:

numeros = []
for i in range(5):
    valor = int(input ())
    numeros.append(valor)
