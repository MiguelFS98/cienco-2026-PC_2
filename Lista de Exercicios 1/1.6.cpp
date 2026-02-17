#include <iostream>
using namespace std;

float calcularAbastecimento(float litros, float preco)
{
    float total = litros * preco;
    return total;
}

int main()
{
    cout << "Valor total: R$ " << calcularAbastecimento(5, 6.31) << endl;
    return 0;
}
