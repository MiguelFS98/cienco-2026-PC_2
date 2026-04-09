//2-)

#include "funcoes.h"

float CalcularVenda(float preco, float percentual) {
    float lucro = preco * (percentual / 100.0);
    float valorVenda = preco + lucro;
    return valorVenda;
}
