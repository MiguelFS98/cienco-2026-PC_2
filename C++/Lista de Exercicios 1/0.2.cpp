#include <iostream>

using namespace std;

int main()
{
    int nota;

    cout << "Digite a nota do aluno: ";
    cin >> nota;

    cout << endl;

    if(nota >= 90)
    {
        cout << "Conceito A\n";
    }
    else if(nota >= 70)
    {
        cout << "Conceito B\n";
    }
    else if(nota >= 50)
    {
        cout << "Conceito C\n";
    }
    else
    {
        cout << "Reprovado\n";
    }
    return 0;
}
