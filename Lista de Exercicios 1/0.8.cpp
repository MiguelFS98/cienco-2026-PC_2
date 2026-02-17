#include <iostream>

using namespace std;

int main()
{
    int vetor1[5] = {2, 4, 6, 8, 10};
    int vetor2[5] = {2, 4, 6, 8, 10};
    int vetor3[5];

    for(int i = 0; i < 5; i++)
    {
        vetor3[i] = vetor1[i] + vetor2[i];
        cout << vetor1[i] << " + " << vetor2[i] << " = " << vetor3[i] << endl;
    }
    cout << endl;
    cout << "Vetor 1: ";
         for(int i = 0; i < 5; i++)
    {
        cout  << vetor1[i] << " ";
    }
    cout << endl;
    cout << "Vetor 2: ";
         for(int i = 0; i < 5; i++)
    {
        cout << vetor2[i] << " ";
    }
    cout << endl;
    cout << "Vetor 3: ";
         for(int i = 0; i < 5; i++)
    {
        cout << vetor3[i] << " ";
    }
    cout << endl;
    return 0;
}
