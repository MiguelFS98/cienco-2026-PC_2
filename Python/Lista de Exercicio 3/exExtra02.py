"""
__________________________________________________________
Curso: Ciência da Computação
Disciplina: Programação de Computadores II
Assunto: Revisão de conceitos – estruturas de decisão e repetição
Tarefa: Sistema de Controle de Vendas (evolução do sistema) em Python – Versão 2
Data: 04/05/2026 (atividade a ser realizada em sala/aula)
__________________________________________________________

VERSÃO 2 – Sistema de Controle de Vendas (evolução do sistema)

Na atividade anterior, você desenvolveu um sistema básico para controle de vendas. 

Agora é hora de evoluir esse sistema, deixando ele um pouco mais completo e mais próximo de uma situação real.

A partir do que já foi feito na versão 1, você deverá acrescentar novas funcionalidades ao programa.

----------------------------------------------------------

CLASSIFICAÇÃO DAS VENDAS

Para cada valor de venda informado, o sistema deve classificar automaticamente:

- Até R$ 100 = venda pequena; 
- De R$ 101 até R$ 500 = venda média; 
- Acima de R$ 500 = venda grande.  

----------------------------------------------------------

CONTROLE POR CATEGORIA

Além de classificar, o sistema deve contabilizar:
- Quantas vendas pequenas foram realizadas;
- Quantas vendas médias foram realizadas;  
- Quantas vendas grandes foram realizadas. 

----------------------------------------------------------

TOTALIZAÇÃO POR CATEGORIA

O sistema também deve acumular o valor total vendido em cada categoria:
- Total vendido em vendas pequenas;
- Total vendido em vendas médias; 
- Total vendido em vendas grandes. 

----------------------------------------------------------

ANÁLISE PERCENTUAL

Com base no valor total geral de vendas (já calculado na versão 1), o sistema deve informar:
- Qual o percentual que as vendas pequenas representam; 
- Qual o percentual que as vendas médias representam;  
- Qual o percentual que as vendas grandes representam. 

Os percentuais devem considerar o valor total vendido e, juntos, devem representar aproximadamente 100%.

----------------------------------------------------------

SAÍDA FINAL

Além das informações já exibidas na versão 1, o programa deve apresentar:
- Quantidade de vendas por categoria;  
- Total vendido por categoria;  
- Percentual de participação de cada categoria no total geral.  

----------------------------------------------------------

OBSERVAÇÕES IMPORTANTES

- Utilize apenas os conceitos já estudados em aula  (if, elif, else, while, for);
- NÃO utilizar listas, funções ou qualquer recurso mais avançado;
- Organize bem as variáveis e o fluxo do programa;
- Pense antes de sair codificando, ou seja, a lógica é o mais importante aqui.

----------------------------------------------------------
"""

import os
os.system('cls')

somaVendas = 0
qntVendas = 0
mediaVendas = 0

valorVendas = float(input("Digite o valor da venda(digitando 0 ira finalizar o programa!!) "))
menor = valorVendas
maior = valorVendas
qntVendasPequenas = 0
qntVendasMedias = 0
qntVendasGrandes = 0
totalVendasPequenas = 0
totalVendasMedias = 0
totalVendasGrandes = 0

while valorVendas != 0:
    if valorVendas < menor:
        menor = valorVendas
    elif valorVendas > maior:
        maior = valorVendas
    somaVendas = somaVendas + valorVendas
    qntVendas = qntVendas + 1
    if valorVendas <= 100:
        qntVendasPequenas = qntVendasPequenas + 1
        totalVendasPequenas = totalVendasPequenas + valorVendas
    elif valorVendas <= 500:
        qntVendasMedias = qntVendasMedias + 1
        totalVendasMedias = totalVendasMedias + valorVendas
    else:
        qntVendasGrandes = qntVendasGrandes + 1
        totalVendasGrandes = totalVendasGrandes + valorVendas
    valorVendas = float(input("Digite o valor da venda(digitando 0 ira finalizar o programa!!) "))
    mediaVendas = somaVendas / qntVendas

percentualPequenas = (totalVendasPequenas / somaVendas) * 100
percentualMedias = (totalVendasMedias / somaVendas) * 100
percentualGrandes = (totalVendasGrandes / somaVendas) * 100
print("Total vendido:", somaVendas)
print("Quantidade de vendas:", qntVendas)
print("Média das vendas:", mediaVendas)
print("Maior venda:", maior)
print("Menor venda:", menor)
print("Quantidade de vendas pequenas:", qntVendasPequenas)
print("Quantidade de vendas médias:", qntVendasMedias)
print("Quantidade de vendas grandes:", qntVendasGrandes)
print("Total vendido em vendas pequenas:", totalVendasPequenas)
print("Total vendido em vendas médias:", totalVendasMedias)
print("Total vendido em vendas grandes:", totalVendasGrandes)
print("Percentual de vendas pequenas:", percentualPequenas, "%")
print("Percentual de vendas médias:", percentualMedias, "%")
print("Percentual de vendas grandes:", percentualGrandes, "%")
