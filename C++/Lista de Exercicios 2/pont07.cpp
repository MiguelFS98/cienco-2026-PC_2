/*
7-)
Crie duas variáveis inteiras:

x = 15
y = 25

Crie dois ponteiros apontando para essas variáveis.
Troque os valores de x e y usando os ponteiros.

Lembre-se que você precisará usar uma variável auxiliar (aux ou temp),
por exemplo para trocar os valores apontados pelos ponteiros.
*/
#include <iostream>

using namespace std;

int main()
{
    int x = 15;
    int y = 25;
    int z;
    int *p1;
    int *p2;

    p1 = &x;
    p2 = &y;

    cout << "Valor apontado pelo ponteiro 1: " << x << endl;
    cout << "Valor apontado pelo ponteiro 2: " << y << endl;

    z = *p1;
    *p1 = *p2;
    *p2 = z;


    cout << "Novo valor apontado pelo ponteiro 1: " << x << endl;
    cout << "Novo valor apontado pelo ponteiro 2: " << y << endl;

}