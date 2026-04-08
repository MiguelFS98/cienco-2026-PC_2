/*Crie duas variáveis inteiras:

a = 10
b = 30

Crie dois ponteiros que apontem para essas variáveis.
Mostre o valor das duas variáveis usando os ponteiros.
Atente-se para que cada ponteiro aponta para uma variável diferente.
*/

#include <iostream>

using namespace std;

int main()
{
    int x = 10;
    int y = 30;    
    int *p1;
    int *p2;

    p1 = &x;
    p2 = &y;

    cout << "Valor apontado pelo ponteiro 1: " << *p1 << endl;
    cout << "Valor apontado pelo ponteiro 2: " << *p2 << endl;
