#include <iostream>

using namespace std;

struct Livro
{
    string titulo;
    string autor;
    int ano;
};


int main()
{
    Livro l1;

    cout << "Digite o titulo do livro: ";
    cin >> l1.titulo;
    cout << endl;
    cout << "Digite o Nome do autor: ";
    cin >> l1.autor;
    cout << "Digite o Ano de lancamento do livro: ";
    cin >> l1.ano;

    cout << "O Titulo do Livro e " << l1.titulo << endl;
    cout << "O Livro foi escrito por " << l1.autor << endl;
    cout << "O Ano de Lancamento foi " << l1.ano << endl;

    return 0;
}