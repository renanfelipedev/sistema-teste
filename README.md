# Sistema Teste - Gerenciamento de Discentes

Sistema em Python para cadastro, listagem e exclusão de discentes utilizando armazenamento em formato CSV. Organizado seguindo a estrutura padrão de projetos Python (`src-layout`).

---

## 📁 Estrutura de Diretórios

```text
sistema-teste/
├── src/
│   └── sistema_teste/
│       ├── __init__.py            # Pacote Python principal
│       ├── main.py                # Executável com menu interativo em loop
│       ├── __main__.py            # Suporte a execução via `python -m sistema_teste`
│       └── alunos/                # Subpacote referente a Alunos
│           ├── __init__.py        # Interface do subpacote alunos
│           ├── gerenciador.py     # Lógica de negócio e fluxo de entrada/saída
│           └── persistencia.py    # Persistência de dados em arquivo CSV
├── .gitignore                     # Arquivos e diretórios ignorados pelo Git
├── pyproject.toml                 # Configuração do pacote Python (PEP 621)
├── requirements.txt               # Especificação de dependências
├── README.md                      # Documentação do repositório
└── main.py                        # Script de atalho na raiz
```

---

## 🚀 Como Executar

### Opção 1: Execução Direta via Script Principal
```bash
python main.py
```

### Opção 2: Execução como Módulo Python (`src-layout`)
```bash
python -m src.sistema_teste.main
```

### Opção 3: Instalação Editável do Pacote
Você pode instalar o pacote localmente no ambiente em modo editável (`-e`):
```bash
pip install -e .
```
E então executar o comando no terminal:
```bash
sistema-teste
```