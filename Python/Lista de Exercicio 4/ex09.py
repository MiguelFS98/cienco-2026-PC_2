import os
os.system('cls')

def tabuada(num):
    print("A tabuada do", num)
    for i in range(11):
        print(num, "x", i, num * i)

tabuada(5)