import alunos

def show_menu():
    print("""
    1 - Cadastrar discente
    2 - Listar discentes
    3 - Excluir discente
    """)

if __name__ == "__main__":
    show_menu()

    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        alunos.cadastrar()
    elif opcao == 2:
        alunos.listar()
    elif opcao == 3:
        alunos.excluir()
    else:
        print("Opção inválida")

