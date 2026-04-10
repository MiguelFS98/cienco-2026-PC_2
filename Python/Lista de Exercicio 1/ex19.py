"""

19) Calculadora simples. Leia dois números e uma operação (+, -, *, /).

Realize o cálculo conforme a operação informada.

Regras a serem consideradas:

- Se for divisão, verificar se o divisor é zero;
- Se a operação for inválida, mostrar mensagem de erro.

"""

import os
os.system('cls')

num1 = float(input("Digite o primeiro numero: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo numero: "))

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Divisor é zero.")
else:
    print("Erro: Operação inválida.")