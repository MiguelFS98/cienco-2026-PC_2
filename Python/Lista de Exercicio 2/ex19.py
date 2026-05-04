i = 1

maior = float(input(f"Digite o número {i}: "))
i += 1

while i <= 5:
    num = float(input(f"Digite o número {i}: "))
    
    if num > maior:
        maior = num
    
    i += 1

print("Maior número:", maior)