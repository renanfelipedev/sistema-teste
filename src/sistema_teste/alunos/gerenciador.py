from sistema_teste.alunos.persistencia import (
    alunos_db,
    fila_atendimento,
    historico_secretaria,
    cursos_homologados
)


def adicionar_curso(nome_curso: str) -> bool:
    """Adiciona um novo curso à lista caso não exista."""
    nome_formatado = nome_curso.strip()
    if any(curso_cadastrado.lower() == nome_formatado.lower() for curso_cadastrado in cursos_homologados):
        print(f"[ERRO] O curso '{nome_formatado}' já está cadastrado.")
        return False
    
    cursos_homologados.append(nome_formatado)
    print(f"[SUCESSO] Curso '{nome_formatado}' homologado com sucesso.")
    return True


def cadastrar_solicitacao(matricula: int, nome: str, curso: str) -> bool:
    """Valida o curso, insere no DB, enfileira (FIFO) e empilha no histórico (LIFO)."""
    if matricula in alunos_db:
        print(f"[ERRO] Matrícula {matricula} já cadastrada na base.")
        return False

    curso_homologado = next((curso_cadastrado for curso_cadastrado in cursos_homologados if curso_cadastrado.lower() == curso.strip().lower()), None)
    if not curso_homologado:
        print(f"[ERRO] Curso '{curso}' inválido. Homologados: {cursos_homologados}")
        return False

    # 1. Armazenamento no Dicionário Principal
    alunos_db[matricula] = {
        'matricula': matricula,
        'nome': nome,
        'curso': curso_homologado,
        'status': "Aguardando"
    }

    # 2. Inserção na Fila de Atendimento (FIFO)
    fila_atendimento.append(matricula)

    # 3. Registro na Pilha de Histórico (LIFO com Tupla Imutável)
    historico_secretaria.append(("CADASTRAR", matricula))

    print(f"[SUCESSO] Aluno(a) {nome} (Matrícula: {matricula}) entrou na fila.")
    return True


def chamar_proximo_aluno() -> bool:
    """Atende o primeiro da fila (FIFO), altera o status e registra no histórico."""
    if not fila_atendimento:
        print("[AVISO] Nenhum aluno aguardando na fila de atendimento.")
        return False

    # 1. Remoção do início da fila (FIFO)
    matricula = fila_atendimento.pop(0)

    # 2. Atualização no banco de dados
    alunos_db[matricula]['status'] = "Em Atendimento"

    # 3. Registro na Pilha de Histórico
    historico_secretaria.append(("CHAMAR", matricula))

    aluno = alunos_db[matricula]
    print(f"[GUICHÊ] Chamando matrícula #{matricula} - {aluno['nome']} ({aluno['curso']}).")
    return True


def desfazer_ultima_acao() -> bool:
    """Desfaz a última ação registrada (LIFO) restaurando o estado anterior."""
    if not historico_secretaria:
        print("[AVISO] Histórico vazio. Nenhuma ação para desfazer.")
        return False

    acao, matricula = historico_secretaria.pop()

    if acao == "CHAMAR":
        # Retorna status para 'Aguardando' e reinserção no início da fila
        alunos_db[matricula]['status'] = "Aguardando"
        fila_atendimento.insert(0, matricula)
        print(f"[UNDO] Chamada desfeita: Matrícula #{matricula} retornou ao início da fila como 'Aguardando'.")

    elif acao == "CADASTRAR":
        # Remove da fila de espera e exclui do banco de dados
        if matricula in fila_atendimento:
            fila_atendimento.remove(matricula)
        if matricula in alunos_db:
            del alunos_db[matricula]
        print(f"[UNDO] Cadastro desfeito: Matrícula #{matricula} removida da fila e da base de dados.")

    return True


def exibir_painel() -> None:
    """Exibe o estado completo das estruturas de dados."""
    print("\n" + "=" * 60)
    print("PAINEL DA SECRETARIA ACADÊMICA (EduQueue)")
    print("=" * 60)

    print("\n--- [CURSOS HOMOLOGADOS] ---")
    print(", ".join(cursos_homologados))

    print("\n--- [FILA DE ATENDIMENTO (FIFO)] ---")
    if fila_atendimento:
        for posicao, mat in enumerate(fila_atendimento, start=1):
            dados = alunos_db[mat]
            print(f"  {posicao}º Lugar -> #{mat}: {dados['nome']} ({dados['curso']})")
    else:
        print("  (Fila vazia)")

    print("\n--- [BASE DE DADOS DOS ALUNOS (alunos_db)] ---")
    if alunos_db:
        for mat, dados in alunos_db.items():
            print(f"  Matrícula #{mat}: {dados['nome']} | Curso: {dados['curso']} | Status: [{dados['status']}]")
    else:
        print("  (Nenhum registro)")

    print("\n--- [HISTÓRICO DE OPERAÇÕES (LIFO - Topo no final)] ---")
    if historico_secretaria:
        for item in historico_secretaria:
            print(f"  Evento: {item[0]} -> Matrícula: {item[1]}")
    else:
        print("  (Histórico vazio)")
    print("=" * 60 + "\n")