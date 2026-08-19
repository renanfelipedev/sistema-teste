from uuid import uuid4
from .persistencia import (
    ARQUIVO,
    verifica_arquivo,
    ler_alunos,
    salvar_aluno,
    reescrever_alunos
)

def cadastrar(file_path=ARQUIVO):
    verifica_arquivo(file_path)
    nome = input("Informe o nome: ")
    curso = input("Informe o curso: ")
    try:
        periodo = int(input("Informe o período: "))
    except ValueError:
        print("Período inválido! Deve ser um número inteiro.")
        return

    novo_aluno = {
        'id': str(uuid4()), 
        'nome': nome,
        'curso': curso,
        'periodo': periodo,
        'status': 'Ativo'
    }

    salvar_aluno(novo_aluno, file_path)
    print(f"Aluno {nome} cadastrado com sucesso!")

def listar(file_path=ARQUIVO):
    verifica_arquivo(file_path)
    print("Lista de discentes cadastrados:")
    alunos, _ = ler_alunos(file_path)
    if not alunos:
        print("Nenhum aluno encontrado.")
        return
    for linha in alunos:
        print(f"""
----------------------------------------
Matrícula: {linha['id']}
Nome: {linha['nome']}
Curso: {linha['curso']}
Período: {linha['periodo']}
Status: {linha['status']}
""")

def excluir(file_path=ARQUIVO):
    verifica_arquivo(file_path)
    matricula = input("Informe a Matrícula (ID) do aluno a ser excluído: ").strip()

    alunos_existentes, campo_nomes = ler_alunos(file_path)
    alunos_restantes = []
    encontrado = False

    for linha in alunos_existentes:
        if linha['id'] == matricula:
            encontrado = True
        else:
            alunos_restantes.append(linha)

    if not encontrado:
        print("Aluno não encontrado!")
        return

    reescrever_alunos(alunos_restantes, campo_nomes, file_path)
    print("Aluno excluído com sucesso!")
