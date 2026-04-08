#include <iostream>

using namespace std;

int main()
{
    int soma = 0;
    int matriz[2][3] = {{1, 2, 3}, {4, 5, 6}};

    for(int i = 0; i < 2; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            soma = soma + matriz[i][j];
            cout << matriz[i][j] << " ";
        }
        cout  << endl;
    }
    cout  << endl;
    cout << soma;
    return 0;
}
