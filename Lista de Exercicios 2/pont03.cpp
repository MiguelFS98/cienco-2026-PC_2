//Crie uma variável inteira chamada x com valor 5.//
//Crie um ponteiro apontando para x.//

#include <iostream>

using namespace std;

int main()
{
    int x = 5;
    int *p;

    p = &x;
    
    cout << "valor de x: " << *p << endl;
    cout << "Valor armazenado no ponteiro: " << p << endl;
    cout << "endereco de x: " << &x << endl;
    cout << endl;

    x = 20;

    cout << "Novo valor de x: " << *p << endl;

}