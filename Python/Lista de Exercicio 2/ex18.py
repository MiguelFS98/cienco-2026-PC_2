contador = 0
i = 1

while i <= 10:
    num = float(input(f"Digite o número {i}: "))
    
    if num > 0:
        contador += 1
    
    i += 1

print("Quantidade de números positivos:", contador)