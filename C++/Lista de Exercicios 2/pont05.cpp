/*Crie uma variável inteira chamada numero com valor 50.
Crie um ponteiro para essa variável.

Mostre:
- valor da variável
- endereço da variável
- valor apontado pelo ponteiro
*/

#include <iostream>

using namespace std;

int main()
{
    int numero = 50;
    int *p;

    p = &numero;

    cout << "Valor da variavel: " << numero << endl;
    cout << "endereco: " << &numero << endl;
    cout << "Valor apontado pelo ponteiro: " << *p << endl;

}