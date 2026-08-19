import sys
from pathlib import Path

src_path = Path(__file__).resolve().parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from sistema_teste.main import main

if __name__ == "__main__":
    sys.exit(main())
