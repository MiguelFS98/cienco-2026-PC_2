temp = 0
contador = 0
soma = 0
media = 0

maior = None
menor = None

temp = float(input("Digite a temperatura: "))

while temp != 999:
    
    if temp >= 0:
        soma = temp + soma
        contador = contador + 1
        if contador == 1:
            maior = temp
            menor = temp
        else:
            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp
    temp = float(input("Digite a temperatura: "))
    
if contador > 0:
    media = soma / contador
print(contador)
print(soma)
print(media)
print(maior)
print(menor)
