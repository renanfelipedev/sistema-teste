import alunos

def show_menu():
    print("""
    [C]adastrar discente
    [B]uscar discente
    [L]istar discentes
    [E]xcluir discente

    [S]air
    """)

if __name__ == "__main__":
    while True:
        show_menu()

        opcao = input("Informe a opção desejada: ").lower()

        match opcao:
            case 'c':
                alunos.cadastrar()
            case 'b':
                alunos.buscar()
            case 'l':
                alunos.listar()
            case 'e':
                alunos.excluir()
            case 's':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")

