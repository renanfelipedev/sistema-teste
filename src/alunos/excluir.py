import csv
from verifica_arquivo import verifica_arquivo, ARQUIVO

def excluir():
    verifica_arquivo()
    matricula = input("Informe a Matrícula (ID) do aluno a ser excluído: ").strip()

    alunos = []
    encontrado = False

    with open(ARQUIVO, 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        campo_nomes = leitor.fieldnames
        for linha in leitor:
            if linha['id'] == matricula:
                encontrado = True
            else:
                alunos.append(linha)

    if not encontrado:
        print("Aluno não encontrado!")
        return

    with open('alunos.csv', 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(alunos)

    print("Aluno excluído com sucesso!")
