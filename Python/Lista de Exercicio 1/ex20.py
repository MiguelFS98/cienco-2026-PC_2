"""

20) Sistema de acesso. Leia:

- Nome do usuário
- Senha

Considere:
Usuário: admin  
Senha: 1234  

Regras:

- Se usuário e senha estiverem corretos, mostrar mensagem: "Acesso permitido";
- Se apenas usuário estiver correto, mostrar mensagem: "Senha incorreta";
- Caso contrário, mostrar: "Usuario invalido".

"""

import os
os.system('cls')

nomeUsuario = input("Digite seu nome de usuário: ")
senhaUsuario = input("Digite sua senha: ")

if (nomeUsuario == "admin" and senhaUsuario == "1234"):
    print("Acesso permitido!!!")
elif(nomeUsuario != "admin" and senhaUsuario == "1234"):
    print("Usuario invalido!!!")
elif(nomeUsuario == "admin" and senhaUsuario != "1234"):
    print("Senha invalida!!!")
elif(nomeUsuario != "admin" and senhaUsuario != "1234"):
    print("Usuario e Senha invalidos!!!")
else:
    print("!!!ERRO!!!")