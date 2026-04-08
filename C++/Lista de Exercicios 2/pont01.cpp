/*
1-)
Declare uma variável inteira chamada x e atribua o valor 10 a ela.
Em seguida, declare um ponteiro para inteiro chamado px e faça esse
ponteiro apontar para a variável x.

Mostre na tela:

- o valor da variável x
- o endereço de memória da variável x
- o valor armazenado no ponteiro px (endereço para onde ele aponta)
- o valor apontado pelo ponteiro (*px)
- o endereço de memória do próprio ponteiro px
*/

#include <iostream>
#include <locale>
using namespace std;

int main()
{
    // Declaração da variável inteira com valor 10
    int x = 10;

    // Declaração de um ponteiro para inteiro
    int *px;

    // O ponteiro passa a apontar para a variável x
    px = &x;

    setlocale(LC_ALL, "Portuguese");

    cout << "\nValor da variável x: " << x;
    cout << "\nEndereco da variável x: " << &x;
    cout << "\nValor armazenado no ponteiro (endereco de x): " << px;
    cout << "\nValor apontado pelo ponteiro (*px): " << *px;
    cout << "\nEndereco do proprio ponteiro px: " << &px;
}
