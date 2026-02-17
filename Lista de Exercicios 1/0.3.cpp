#include <iostream>
#include <locale>

using namespace std;

int main()
{
    int escolha;

    setlocale(LC_ALL, "Portuguese");

    cout << "1 - Suporte Técnico" << endl;
    cout << "2 - Financeiro" << endl;
    cout << "3 - Comercial" << endl;
    cout << "Selecione o serviço desejado: ";
    cin >> escolha;

    cout << endl;

    if(escolha < 1 || escolha > 3)
    {
        cout << "Opção Inválida\n";
    }
    return 0;
}
