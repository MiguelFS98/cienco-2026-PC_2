//3-)

#include <iostream>
#include "funcoes.h"

using namespace std;

int main() {
    float preco, percentual, resultado;

    cout << "Digite o preco do produto: ";
    cin >> preco;

    cout << "Digite o percentual de lucro (%): ";
    cin >> percentual;

    resultado = CalcularVenda(preco, percentual);

    cout << "Valor de venda: " << resultado << endl;

    return 0;
}