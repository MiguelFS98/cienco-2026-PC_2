#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

// Definição da Struct para o Livro
struct Livro {
    string nome;
    string autor;
    int ano;
    float preco;
    int situacao; // 0 = disponível, 1 = emprestado
};

int main() {
    Livro biblioteca[10];
    int totalLivros = 0;
    int opcao = 0;

    // Configuração para exibir preços com duas casas decimais
    cout << fixed << setprecision(2);

    while (opcao != 10) {
        cout << "\n--- SISTEMA DE BIBLIOTECA ---" << endl;
        cout << "1 - Cadastrar livros" << endl;
        cout << "2 - Mostrar todos os livros" << endl;
        cout << "3 - Emprestar livro" << endl;
        cout << "4 - Devolver livro" << endl;
        cout << "5 - Mostrar livros disponíveis" << endl;
        cout << "6 - Mostrar livros emprestados" << endl;
        cout << "7 - Quantidade de disponíveis/emprestados" << endl;
        cout << "8 - Consultar livro específico" << endl;
        cout << "9 - Mostrar livro mais caro" << endl;
        cout << "10 - Encerrar" << endl;
        cout << "Escolha uma opcao: ";
        cin >> opcao;
        cin.ignore(); // Limpa o buffer do teclado

        switch (opcao) {
            case 1: // Cadastrar
                if (totalLivros < 10) {
                    cout << "\nCadastro do Livro " << totalLivros + 1 << ":" << endl;
                    cout << "Nome: ";
                    getline(cin, biblioteca[totalLivros].nome);
                    cout << "Autor: ";
                    getline(cin, biblioteca[totalLivros].autor);
                    cout << "Ano: ";
                    cin >> biblioteca[totalLivros].ano;
                    cout << "Preco: ";
                    cin >> biblioteca[totalLivros].preco;
                    biblioteca[totalLivros].situacao = 0; // Inicia disponível
                    totalLivros++;
                    cout << "Livro cadastrado com sucesso!" << endl;
                } else {
                    cout << "Biblioteca cheia!" << endl;
                }
                break;

            case 2: // Mostrar todos
                for (int i = 0; i < totalLivros; i++) {
                    cout << "\nLivro " << i + 1 << ":" << endl;
                    cout << "Nome: " << biblioteca[i].nome << endl;
                    cout << "Autor: " << biblioteca[i].autor << endl;
                    cout << "Ano: " << biblioteca[i].ano << endl;
                    cout << "Preco: R$ " << biblioteca[i].preco << endl;
                    cout << "Situacao: " << (biblioteca[i].situacao == 0 ? "Disponivel" : "Emprestado") << endl;
                }
                break;

            case 3: // Emprestar
                int numEmp;
                cout << "Informe o numero do livro para emprestimo (1 a " << totalLivros << "): ";
                cin >> numEmp;
                if (numEmp > 0 && numEmp <= totalLivros) {
                    if (biblioteca[numEmp - 1].situacao == 0) {
                        biblioteca[numEmp - 1].situacao = 1;
                        cout << "Emprestimo realizado!" << endl;
                    } else {
                        cout << "Livro ja esta emprestado." << endl;
                    }
                }
                break;

            case 4: // Devolver
                int numDev;
                cout << "Informe o numero do livro para devolucao: ";
                cin >> numDev;
                if (numDev > 0 && numDev <= totalLivros) {
                    biblioteca[numDev - 1].situacao = 0;
                    cout << "Livro devolvido com sucesso!" << endl;
                }
                break;

            case 5: // Apenas disponíveis
                cout << "\n--- LIVROS DISPONIVEIS ---" << endl;
                for (int i = 0; i < totalLivros; i++) {
                    if (biblioteca[i].situacao == 0) {
                        cout << "- " << biblioteca[i].nome << endl;
                    }
                }
                break;

            case 6: // Apenas emprestados
                cout << "\n--- LIVROS EMPRESTADOS ---" << endl;
                for (int i = 0; i < totalLivros; i++) {
                    if (biblioteca[i].situacao == 1) {
                        cout << "- " << biblioteca[i].nome << endl;
                    }
                }
                break;

            case 7: // Contagem
                int disp = 0, empr = 0;
                for (int i = 0; i < totalLivros; i++) {
                    if (biblioteca[i].situacao == 0) disp++;
                    else empr++;
                }
                cout << "\nDisponiveis: " << disp << "\nEmprestados: " << empr << endl;
                break;

            case 8: // Consultar específico
                int ind;
                cout << "Numero do livro: ";
                cin >> ind;
                if (ind > 0 && ind <= totalLivros) {
                    cout << "Nome: " << biblioteca[ind-1].nome << " | Autor: " << biblioteca[ind-1].autor << endl;
                    cout << "Situacao: " << (biblioteca[ind-1].situacao == 0 ? "Disponivel" : "Emprestado") << endl;
                }
                break;

            case 9: // Mais caro
                if (totalLivros > 0) {
                    int caro = 0;
                    for (int i = 1; i < totalLivros; i++) {
                        if (biblioteca[i].preco > biblioteca[caro].preco) {
                            caro = i;
                        }
                    }
                    cout << "\nLivro mais caro: " << biblioteca[caro].nome << " (R$ " << biblioteca[caro].preco << ")" << endl;
                }
                break;

            case 10:
                cout << "Encerrando sistema..." << endl;
                break;

            default:
                cout << "Opcao invalida!" << endl;
        }
    }

    return 0;
}