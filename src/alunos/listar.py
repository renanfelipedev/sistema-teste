import csv
from verifica_arquivo import verifica_arquivo, ARQUIVO

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
