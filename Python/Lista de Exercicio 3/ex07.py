matriz = []
soma = 0
for i in range(2):
    linha = []
    for j in range(2):
        n = int(input ())
        linha . append(n)
        soma = soma + n
    matriz . append( linha )
    
print ("Soma:" , soma)