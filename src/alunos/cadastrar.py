import csv
from uuid import uuid4
from verifica_arquivo import verifica_arquivo, ARQUIVO

def cadastrar():
    verifica_arquivo()
    nome = input("Informe o nome: ")
    curso = input("Informe o curso: ")
    periodo = int(input("Informe o período: "))

    novo_aluno = {
        'id': str(uuid4())[:8], 
        'nome': nome,
        'curso': curso,
        'periodo': periodo,
        'status': 'Ativo'
    }

    with open(ARQUIVO, 'a', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["id", "nome", "curso", "periodo", "status"])
        escritor.writerow(novo_aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")
