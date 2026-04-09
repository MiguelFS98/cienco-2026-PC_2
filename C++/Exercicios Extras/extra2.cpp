/*Atividade extra 02 (Parte I)

Uma pequena escola deseja um programa simples para auxiliar no controle
de notas de uma turma.

O programa deve armazenar as notas de 10 alunos utilizando um vetor.

Cada posição do vetor representa a nota de um aluno.
As notas devem variar de 0 a 10.

O programa deve apresentar o seguinte menu:

1 - Cadastrar notas
2 - Mostrar notas
3 - Calcular média da turma
4 - Mostrar maior e menor nota
5 - Encerrar

Funcionamento:

a) Na opção "Cadastrar notas", o programa deve solicitar ao usuário
a nota de cada um dos 10 alunos e armazenar no vetor.

b) Na opção "Mostrar notas", o programa deve mostrar todas as notas
armazenadas no vetor, indicando também a posição (ou número do aluno).

Exemplo:

Aluno 1: 7.5
Aluno 2: 8.0
Aluno 3: 6.5
...

c) Na opção "Calcular média da turma", o programa deve calcular e
mostrar a média das notas armazenadas.

d) Na opção "Mostrar maior e menor nota", o programa deve percorrer
o vetor e informar qual foi a maior nota e qual foi a menor nota
digitada.

e) O menu deve continuar sendo exibido até que o usuário escolha
encerrar o programa (opção 5).

*/

/*
Essa pequena atividade tem como objetivos importantes treinar conceitos e práticas em:

vetor
laço for
laço while
menu com switch
acumulador (soma)
busca de maior e menor

Ou seja, ele revisa praticamente toda a base de lógica que vocês trabalharam até agora.

*/

#include <iostream>
using namespace std;

int main() {
    float notas[10];
    int opcao;
    bool cadastradas = false;

    do {
        cout << "\n===== MENU =====\n";
        cout << "1 - Cadastrar notas\n";
        cout << "2 - Mostrar notas\n";
        cout << "3 - Calcular media da turma\n";
        cout << "4 - Mostrar maior e menor nota\n";
        cout << "5 - Alunos acima da media\n";
        cout << "6 - Alunos abaixo da media\n";
        cout << "7 - Consultar nota de um aluno\n";
        cout << "8 - Quantidade de aprovados e reprovados\n";
        cout << "9 - Encerrar\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        switch(opcao) {

            case 1: {
                cout << "\nCadastro de notas:\n";
                for(int i = 0; i < 10; i++) {
                    do {
                        cout << "Digite a nota do aluno " << i + 1 << " (0 a 10): ";
                        cin >> notas[i];
                    } while(notas[i] < 0 || notas[i] > 10);
                }
                cadastradas = true;
                break;
            }

            case 2: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    cout << "\nNotas:\n";
                    for(int i = 0; i < 10; i++) {
                        cout << "Aluno " << i + 1 << ": " << notas[i] << endl;
                    }
                }
                break;
            }

            case 3: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    float soma = 0;
                    for(int i = 0; i < 10; i++) {
                        soma += notas[i];
                    }
                    cout << "\nMedia da turma: " << soma / 10 << endl;
                }
                break;
            }

            case 4: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    float maior = notas[0];
                    float menor = notas[0];

                    for(int i = 1; i < 10; i++) {
                        if(notas[i] > maior) maior = notas[i];
                        if(notas[i] < menor) menor = notas[i];
                    }

                    cout << "\nMaior nota: " << maior << endl;
                    cout << "Menor nota: " << menor << endl;
                }
                break;
            }

            case 5: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    float soma = 0, media;
                    for(int i = 0; i < 10; i++) soma += notas[i];
                    media = soma / 10;

                    cout << "\nAlunos acima da media:\n";
                    for(int i = 0; i < 10; i++) {
                        if(notas[i] > media) {
                            cout << "Aluno " << i + 1 << ": " << notas[i] << endl;
                        }
                    }
                }
                break;
            }

            case 6: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    float soma = 0, media;
                    for(int i = 0; i < 10; i++) soma += notas[i];
                    media = soma / 10;

                    cout << "\nAlunos abaixo da media:\n";
                    for(int i = 0; i < 10; i++) {
                        if(notas[i] < media) {
                            cout << "Aluno " << i + 1 << ": " << notas[i] << endl;
                        }
                    }
                }
                break;
            }

            case 7: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    int aluno;
                    cout << "\nDigite o numero do aluno (1 a 10): ";
                    cin >> aluno;

                    if(aluno >= 1 && aluno <= 10) {
                        cout << "Nota do aluno " << aluno << ": " << notas[aluno - 1] << endl;
                    } else {
                        cout << "Numero invalido!\n";
                    }
                }
                break;
            }

            case 8: {
                if(!cadastradas) {
                    cout << "\nCadastre as notas primeiro!\n";
                } else {
                    int aprovados = 0, reprovados = 0;

                    for(int i = 0; i < 10; i++) {
                        if(notas[i] >= 6.0)
                            aprovados++;
                        else
                            reprovados++;
                    }

                    cout << "\nAprovados: " << aprovados << endl;
                    cout << "Reprovados: " << reprovados << endl;
                }
                break;
            }

            case 9:
                cout << "\nEncerrando...\n";
                break;

            default:
                cout << "\nOpcao invalida!\n";
        }

    } while(opcao != 9);

    return 0;
}