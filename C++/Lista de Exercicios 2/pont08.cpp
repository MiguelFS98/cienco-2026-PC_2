/*
8-)
Crie uma variável inteira chamada numero com valor 100.
Crie um ponteiro apontando para ela.

Mostre:

- endereço guardado no ponteiro
- valor apontado pelo ponteiro
- Lembre-se que:
  p mostra o endereço
  *p mostra o valor no endereço
*/


#include <iostream>

using namespace std;

int main()
{
    int numero = 100;
    int *p;

    p = &numero;
    
    cout << "valor de numero: " << *p << endl;
    cout << "endereco de numero: " << &numero << endl;
    cout << endl;

}