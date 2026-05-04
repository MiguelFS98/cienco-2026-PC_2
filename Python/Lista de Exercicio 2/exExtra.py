"""
Leia números até que o usuário digite 0. No final, mostre a soma de todos os números digitados.



soma = 0

num = float(input("Digite um número (0 para parar): "))

while num != 0:
    soma += num
    num = float(input("Digite um número (0 para parar): "))

print("Soma total:", soma)

"""
"""

Leia um número inteiro positivo e mostre quantos dígitos ele possui.





num = int(input("Digite um número inteiro positivo: "))

contador = 0

while num > 0:
    num //= 10
    contador += 1

print("Quantidade de dígitos:", contador)

"""
"""

Leia um número e mostre se ele é primo ou não.



num = int(input("Digite um número: "))

i = 2
primo = True

while i < num:
    if num % i == 0:
        primo = False
        break
    i += 1

if primo and num > 1:
    print("É primo")
else:
    print("Não é primo")

"""
"""

Mostre a soma dos números pares de 1 até 100.




menor = float(input("Digite o número 1: "))

for i in range(2, 6):
    num = float(input(f"Digite o número {i}: "))
    
    if num < menor:
        menor = num

print("Menor número:", menor)

"""
"""

Mostre os números de 1 a 20 e indique se são pares ou ímpares.



for i in range(1, 21):
    if i % 2 == 0:
        print(i, "- par")
    else:
        print(i, "- ímpar")

"""