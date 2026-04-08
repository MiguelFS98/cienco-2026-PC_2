#include <iostream>
#include <locale>

using namespace std;

void x(int n)
{
    if(n == 0)
    {
        cout << " ";
    }
    else
    {
        cout << "X";
    }
    
    
}

int main()
{
    int vaga[10] = {0};
    int escolha;
    int status = 0;
    int estacionar;
    int retirar;
    int livres = 10;
    int estacionado = 0;
    int indice;

    setlocale(LC_ALL, "Portuguese");

    do
    {
        

        cout << "1 - Mostrar Vagas" << endl;
        cout << "2 - Estacionar Veículo" << endl;
        cout << "3 - Retirar Veículo" << endl;
        cout << "4 - Encerrar" << endl;

        cout << "escolha uma opção: ";
        cin >> escolha;

        switch (escolha)
        {
        case 1:
            for(int i = 0; i < 10; i++)
            {
                cout << "["; x(vaga[i]); cout << "]" << " ";
            }
            cout << endl;
            cout << endl;
        break;
        case 2:

            cout << "Escolha a vaga em que deseja estacionar: ";
            cin >> estacionar;
            cout << endl;

            indice = estacionar - 1;

            for(int i = 0; i < 10; i++)
            {
                int indice = estacionar - 1;
            
                if (indice < 0 || indice > 9)
                {
                    cout << "Vaga inválida!" << endl;
                }        
                else if (vaga[indice] == 0) 
                {
                    vaga[indice] = 1; 
                    estacionado++;
                    livres--;
                    cout << "Veículo estacionado na vaga " << estacionar << endl;
                }
                else if (vaga[indice - 1] == 1)
                {
                    status = 1;
                }
            }

                if (status == 1)
            {
                cout << "A vaga escolhida já está ocupada!!" << endl;
            }
                cout << endl;
        break;
        case 3:
             cout << "Escolha a vaga em que deseja retirar o Veiculo: ";
             cin >> retirar;

             for(int i = 0; i < 10; i++)
            {
                if(vaga[retirar-1] == 1)
                {
                    retirar = retirar - 1;
                    vaga[retirar]--;
                    livres++;
                    estacionado--;
                
                }
            else if (vaga[retirar-1] <= 0)
            {
                status = 1;
            }

            }

            if (status == 1)
            {
                cout << "A vaga escolhida ja esta livre!!" << endl;
            }

        
        
            cout << endl;
        break;

        case 4:

        cout << "------Estatisticas------" << endl;
        cout << "Vagas Livres: " << livres << endl;
        cout << "Vagas Ocupadas: " << estacionado << endl;
        cout << endl;
        cout << endl;
        cout << "Programa Finalizado!!" << endl;
        }
        
    }
    while (escolha <= 4);
    
}
