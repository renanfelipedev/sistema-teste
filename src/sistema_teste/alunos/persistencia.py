# Estado global das coleções em memória

alunos_db = {}            # Dict: matricula -> {'matricula', 'nome', 'curso', 'status'}
fila_atendimento = []     # List (FIFO): armazena apenas as matrículas
historico_secretaria = [] # List (LIFO): armazena tuplas imutáveis ("ACAO", matricula)
cursos_homologados = [    # List: cursos válidos
    "Engenharia de Software",
    "Ciência da Computação",
    "Sistemas de Informação",
    "Licenciatura em Computação"
]