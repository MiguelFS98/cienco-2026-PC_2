matriz = [
[ 5 , 12] ,
[ 20 , 8]
]
maior = matriz [0][0]
for i in range(2):
    for j in range(2):
        if matriz [ i ][ j ] > maior:
            maior = matriz [ i ][ j ]
print ("Maior valor :" , maior)