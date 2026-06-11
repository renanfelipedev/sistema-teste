import csv
from verifica_arquivo import verifica_arquivo, ARQUIVO

def buscar():
    verifica_arquivo()
    nome = input("Digite um nome (ou parte do nome) do discente que deseja buscar: ").lower()

    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if nome in linha['nome'].lower():
                print(f"""
----------------------------------------
Matrícula: {linha['id']}
Nome: {linha['nome']}
Curso: {linha['curso']}
Período: {linha['periodo']}
Status: {linha['status']}
----------------------------------------
""")

    print("Discente não encontrado!")
