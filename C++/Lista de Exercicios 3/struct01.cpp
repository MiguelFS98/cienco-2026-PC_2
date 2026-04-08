#include <iostream>

using namespace std;

struct Pessoa
{
    string nome;
    int idade;
};


int main()
{
    Pessoa pessoa;

    cout << "Digite o nome da Pessoa: ";
    cin >> pessoa.nome;
    cout << endl;
    cout << "Digite a idade da Pessoa: ";
    cin >> pessoa.idade;

    cout << "O nome da Pessoa e " << pessoa.nome << endl;
    cout << "A idade da Pessoa e " << pessoa.idade << endl;

    return 0;
}