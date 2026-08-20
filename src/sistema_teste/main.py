import sys
from sistema_teste.alunos import (
    adicionar_curso,
    cadastrar_solicitacao,
    chamar_proximo_aluno,
    desfazer_ultima_acao,
    exibir_painel,
)


def exibir_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA SECRETARIA (EduQueue)")
    print("=" * 40)
    print("1. Cadastrar solicitação de aluno (Entrar na Fila)")
    print("2. Chamar próximo aluno (Atendimento)")
    print("3. Desfazer última ação (Undo)")
    print("4. Adicionar novo curso ao catálogo")
    print("5. Exibir painel geral")
    print("0. Sair")
    print("=" * 40)


def menu_cadastrar_solicitacao():
    print("\n--- [Novo Atendimento] ---")
    try:
        matricula_str = input("Informe o número de matrícula: ").strip()
        if not matricula_str.isdigit():
            print("[ERRO] A matrícula deve conter apenas números.")
            return
        matricula = int(matricula_str)

        nome = input("Informe o nome do aluno: ").strip()
        if not nome:
            print("[ERRO] O nome não pode ser vazio.")
            return

        curso = input("Informe o curso: ").strip()
        if not curso:
            print("[ERRO] O curso não pode ser vazio.")
            return

        cadastrar_solicitacao(matricula, nome, curso)
    except Exception as e:
        print(f"[ERRO INESPERADO] {e}")


def menu_adicionar_curso():
    print("\n--- [Homologar Curso] ---")
    nome_curso = input("Informe o nome do novo curso: ").strip()
    if not nome_curso:
        print("[ERRO] O nome do curso não pode ser vazio.")
        return
    adicionar_curso(nome_curso)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_cadastrar_solicitacao()
        elif opcao == "2":
            chamar_proximo_aluno()
        elif opcao == "3":
            desfazer_ultima_acao()
        elif opcao == "4":
            menu_adicionar_curso()
        elif opcao == "5":
            exibir_painel()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("[OPÇÃO INVÁLIDA] Digite um número correspondente a uma das opções do menu.")


if __name__ == "__main__":
    main()