#include <iostream>
#include <locale>

using namespace std;

int main()
{
    int vetor[5] = {10, 20, 30, 40, 50};
    int maior;
    int menor;

    setlocale(LC_ALL, "Portuguese");

    maior = vetor[0];
    menor = vetor[0];
    for(int i = 0; i < 5; i++)
    {
        if(vetor[i] > maior)
        {
            maior = vetor[i];
        }
        else if(vetor[i] < menor)
        {
            menor = vetor[i];
        }
        cout << vetor[i] << " ";
    }
    cout << endl;
    cout << "O menor numero é " << menor << endl;
    cout << "O maior numero é " << maior << endl;
    return 0;
}
