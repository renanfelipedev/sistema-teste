from os import path

ARQUIVO = 'alunos.csv'

def verifica_arquivo():
    if not path.isfile(ARQUIVO):
        with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
            cabecalho = "id,nome,curso,periodo,status\n"
            arquivo.write(cabecalho)
