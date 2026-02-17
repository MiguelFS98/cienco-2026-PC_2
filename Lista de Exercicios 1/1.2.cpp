#include <iostream>

using namespace std;

int main()
{
    int impar = 0;
    int par = 0;
    int matriz[2][3] = {{1, 2, 3}, {4, 5, 6}};

    for(int i = 0; i < 2; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cout << matriz[i][j] << " ";

            if(matriz[i][j] % 2 == 0)
            {
                par++;
            }
            else if(matriz[i][j] % 2 == 1)
            {
                impar++;
            }
        }
        cout  << endl;
    }
    cout << "Tem " << par << " numeros pares na matriz.\n";
    cout << "Tem " << impar << " numeros pares na matriz.";
    return 0;
}
