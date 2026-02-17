#include <iostream>

using namespace std;

void calcularAbastecimento(float litros, float preco)
{
    float total = (litros * preco);
    cout << "O valor total a pagar e: R$ " << total << endl;
}

int main()
{
    calcularAbastecimento(5, 6.31);
}
