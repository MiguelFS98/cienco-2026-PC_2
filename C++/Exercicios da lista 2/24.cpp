#include <iostream>
using namespace std;

struct Produto {
    string nome;
    float preco;
    int quantidade;
};

int main() {
    Produto produtos[3];

    for (int i = 0; i < 3; i++) {
        cout << "Digite o nome do produto: ";
        cin >> produtos[i].nome;
        cout << "Digite o preco: ";
        cin >> produtos[i].preco;
        cout << "Digite a quantidade: ";
        cin >> produtos[i].quantidade;
        cout << endl;
    }

    cout << "\nProdutos cadastrados:\n";
    for (int i = 0; i < 3; i++) {
        cout << "Nome: " << produtos[i].nome << endl;
        cout << "Preco: " << produtos[i].preco << endl;
        cout << "Quantidade: " << produtos[i].quantidade << endl;
        cout << "-------------------\n";
    }

    return 0;
}