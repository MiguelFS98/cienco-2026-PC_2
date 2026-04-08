/*
Crie uma variável inteira chamada idade com valor 18.
Crie um ponteiro apontando para essa variável.

Altere o valor da idade para 21 usando o ponteiro.
*/
#include <iostream>

using namespace std;

int main()
{
    int Idade = 18;
    int *p;

    p = &Idade;
    
    cout << "valor de Idade: " << *p << endl;
    cout << "Valor armazenado no ponteiro: " << p << endl;
    cout << "endereco de Idade: " << &Idade << endl;
    cout << endl;

    *p = 21;


    cout << "Novo valor de Idade: " << Idade << endl;
}