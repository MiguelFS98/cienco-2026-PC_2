from pulp import *
x = LpVariable(
"x" ,
lowBound=0
)
modelo = LpProblem( "Exemplo" , LpMaximize)
modelo += x
modelo . solve ()