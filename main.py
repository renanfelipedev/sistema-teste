import sys
from pathlib import Path

# Adiciona o diretório 'src' e a raiz ao sys.path para permitir importações
root_path = Path(__file__).parent
src_path = root_path / "src"

if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

try:
    from sistema_teste.main import main
except ImportError:
    from src.sistema_teste.main import main

if __name__ == "__main__":
    main()
