import csv
from uuid import uuid4
from os import path

ARQUIVO = 'alunos.csv'

def verifica_arquivo():
    if not path.isfile(ARQUIVO):
        with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
            cabecalho = "id,nome,curso,periodo,status\n"
            arquivo.write(cabecalho)

def cadastrar():
    verifica_arquivo()
    nome = input("Informe o nome: ")
    curso = input("Informe o curso: ")
    periodo = int(input("Informe o período: "))

    novo_aluno = {
        'id': str(uuid4()), 
        'nome': nome,
        'curso': curso,
        'periodo': periodo,
        'status': 'Ativo'
    }

    with open(ARQUIVO, 'a', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["id", "nome", "curso", "periodo", "status"])
        escritor.writerow(novo_aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")

def listar():
    verifica_arquivo()
    print("Lista de discentes cadastrados:")
    with open(ARQUIVO, 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print(f"""
----------------------------------------
Matrícula: {linha['id']}
Nome: {linha['nome']}
Curso: {linha['curso']}
Período: {linha['periodo']}
Status: {linha['status']}
""")

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

    with open(ARQUIVO, 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(alunos)

    print("Aluno excluído com sucesso!")

if __name__ == "__main__":
    print("Módulo de alunos iniciado!")
