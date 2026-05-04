def mostrarIdade():
    print("Idade", '=', Idade)

Idade = int(input("Digite a Idade: "))
contador = 0
while Idade > 0:
    mostrarIdade()
    if Idade >= 18:
        contador = contador + 1
    Idade = int(input("Digite a Idade: "))
print(contador)