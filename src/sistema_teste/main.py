import sys
from pathlib import Path

# Garante que o diretório 'src' esteja no sys.path mesmo ao executar este arquivo diretamente
src_path = Path(__file__).resolve().parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from sistema_teste.alunos import cadastrar, listar, excluir

def show_menu():
    print("""
    ==============================
    1 - Cadastrar discente
    2 - Listar discentes
    3 - Excluir discente
    4 - Sair
    ==============================
    """)

def main():
    while True:
        show_menu()
        try:
            opcao = int(input("Informe a opção desejada: "))
        except ValueError:
            print("Opção inválida! Digite um número inteiro.")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nSaindo do sistema...")
            break

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Escolha uma opção de 1 a 4.")

if __name__ == "__main__":
    main()
