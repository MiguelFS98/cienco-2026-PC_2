n = int(input("Digite um número inteiro positivo: "))

fatorial = 1
i = 1

while i <= n:
    fatorial *= i
    i += 1

print("Fatorial:", fatorial)