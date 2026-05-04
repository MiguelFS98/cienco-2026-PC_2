soma = 0
i = 1

while i <= 10:
    num = float(input(f"Digite o número {i}: "))
    soma += num
    i += 1

media = soma / 10

print("Média:", media)