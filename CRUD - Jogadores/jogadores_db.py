import sqlite3

def conectar():
    conn =sqlite3.connect("jogadores.db")
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nome TEXT,
           nascimento TEXT,
           clube_anterior TEXT,
           convocacoes TEXT,
           idade TEXT,
           contrato TEXT
           
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_jogador():
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Digite o nome do jogador: ")
    nascimento = input("Digite o nascimento do jogador: ")
    clube_anterior = input("Digite o clube_anterior do jogador: ")
    convocacoes = input("Digite a convocacoes: ")
    idade = input("Digite a idade: ")
    contrato = input("Digite a data do fim do contrato: ")

    cursor.execute("""
        INSERT INTO jogadores (nome, nascimento, clube_anterior, convocacoes, idade, contrato)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, nascimento, clube_anterior, convocacoes, idade, contrato))

    conn.commit()
    conn.close()
    print("✅ Jogador cadastrado com sucesso!")

def listar_jogadores():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jogadores")
    jogadores = cursor.fetchall()
    conn.close()

    if len(jogadores) == 0:
      print("Nenhum jogador encontrado!")
      return

    for jogador in jogadores:
        print(f"\n🔴 ID:{jogador[0]}")
        print(f"Nome: {jogador[1]}")
        print(f"Nascimento: {jogador[2]}")
        print(f"Clube anterior: {jogador[3]}")
        print(f"Convocações: {jogador[4]}")
        print(f"Idade: {jogador[5]}")
        print(f"Contrato: {jogador[6]}")

def atualizar_jogador():
    listar_jogadores()
    id_jogador = int(input("Digite o id do jogador que deseja editar: "))

    nome = input("Digite o nome do jogador (deixe em branco para manter o atual) ")
    nascimento = input("Digite a nova data de nascimento (deixe em branco para manter o atual) ")
    clube_anterior = input("Digite o clube anterior do jogador (deixe em branco para manter o atual) ")
    convocacoes = input("Digite o número de convocacoes (deixe em branco para manter o atual) ")
    idade = input("Digite a idade do jogador (deixe em branco para manter o atual) ")
    contrato = input("Digite a data do contrato do jogador (deixe em branco para manter o atual) ")

    conn = conectar()
    cursor = conn.cursor()

    if nome: cursor.execute("UPDATE jogadores SET nome = ? WHERE id = ?", (nome, id_jogador))
    if nascimento: cursor.execute("UPDATE jogadores SET nascimento = ? WHERE id = ?", (nascimento, id_jogador))
    if clube_anterior: cursor.execute("UPDATE jogadores SET clube_anterior = ? WHERE id = ?", (clube_anterior, id_jogador))
    if convocacoes: cursor.execute("UPDATE jogadores SET convocacoes = ? WHERE id = ?", (convocacoes, id_jogador))
    if idade: cursor.execute("UPDATE jogadores SET idade = ? WHERE id = ?", (idade, id_jogador))
    if contrato: cursor.execute("UPDATE  jogadores SET idade = ? WHERE id = ?", (contrato, id_jogador))

    conn.commit()
    conn.close()
    print("✅ Perfil do jogador atualziado com sucesso!")

def deletar_jogador():
    listar_jogadores()
    id_jogadores = input("Digite o id do jogador que deseja deletar: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jogadores WHERE id = ?", (id_jogadores,))
    conn.commit()
    conn.close()
    print("✅ Jogador deletado com sucesso!")

def menu():
    criar_tabela()
    while True:
        print("\n====== Elenco CR Flamengo =====")
        print("1 - Cadastrar jogador")
        print("2 - Listar jogadores")
        print("3 - Atualizar jogador")
        print("4 - Deletar jogador")
        print("5 - Sair")

        opcao = input("Selecione: ")

        if opcao == "1":
            cadastrar_jogador()
        elif opcao == "2":
            listar_jogadores()
        elif opcao == "3":
            atualizar_jogador()
        elif opcao == "4":
            deletar_jogador()
        elif opcao == "5":
            print("🔴⚫Obrigado e saudações Rubro Negras!!🔴⚫")
            break
        else:
            print("Opção inválida, tente novamente!")

menu()

