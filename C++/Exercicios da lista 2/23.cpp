#include <iostream>
using namespace std;

int main() {
    int x = 10;          // variável inteira
    int *ptr = &x;       // ponteiro para a variável

    cout << "Endereco da variavel: " << &x << endl;
    cout << "Endereco armazenado no ponteiro: " << ptr << endl;
    cout << "Valor armazenado no ponteiro: " << *ptr << endl;
    cout << "Valor da variavel: " << x << endl;

    return 0;
}