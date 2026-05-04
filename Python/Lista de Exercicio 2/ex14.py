soma = 0
i = 1

while i <= 5:
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota
    i += 1

media = soma / 5

print("Média:", media)