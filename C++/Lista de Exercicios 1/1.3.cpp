#include <iostream>
#include <locale>

using namespace std;

void somarNumeros()
{
    int numero1 = 14;
    int numero2 = 14;
    int soma;

    soma = numero1 + numero2;
    cout << soma;
}

int main()
{
    setlocale(LC_ALL, "Portuguese");
    cout << "A soma dos numero declarados é ";
    somarNumeros();
    return 0;
}
