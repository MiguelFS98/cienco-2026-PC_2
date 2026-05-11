matriz = [
[ 5 , 12] ,
[ 20 , 8]
]
contador = 0
for i in range(2):
    for j in range(2):
        if matriz[i][j] > 10:
            contador = contador + 1
print("Maiores que 10:", contador)