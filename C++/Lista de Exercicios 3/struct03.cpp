#include <iostream>

using namespace std;

struct Carro
{
    string marca;
    string modelo;
    int ano;
};


int main()
{
    Carro c1;

    cout << "Digite a marca do carro: ";
    cin >> c1.marca;
    cout << endl;
    cout << "Digite o Nome do modelo: ";
    cin >> c1.modelo;
    cout << "Digite o Ano de lancamento do carro: ";
    cin >> c1.ano;

    cout << "A marca do carro e " << c1.marca << endl;
    cout << "O modelo do carro e " << c1.modelo << endl;
    cout << "O Ano de Lancamento foi " << c1.ano << endl;

    return 0;
}