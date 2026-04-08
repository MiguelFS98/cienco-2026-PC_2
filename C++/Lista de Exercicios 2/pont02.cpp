/*Crie uma variável inteira chamada numero com valor 25.
Crie um ponteiro que aponte para essa variável.*/

#include <iostream>

using namespace std;

int main()
{
    int x = 25;
    int *p;

    p = &x;

    cout << "Valor da variavel usando ponteiro: " << *p << endl;

}