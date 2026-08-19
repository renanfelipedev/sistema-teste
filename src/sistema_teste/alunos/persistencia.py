import csv
from os import path

ARQUIVO = 'alunos.csv'

def verifica_arquivo(file_path=ARQUIVO):
    if not path.isfile(file_path):
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            cabecalho = "id,nome,curso,periodo,status\n"
            arquivo.write(cabecalho)

def ler_alunos(file_path=ARQUIVO):
    verifica_arquivo(file_path)
    with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor), leitor.fieldnames

def salvar_aluno(novo_aluno, file_path=ARQUIVO):
    verifica_arquivo(file_path)
    with open(file_path, 'a', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["id", "nome", "curso", "periodo", "status"])
        escritor.writerow(novo_aluno)

def reescrever_alunos(alunos, campo_nomes, file_path=ARQUIVO):
    with open(file_path, 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(alunos)
