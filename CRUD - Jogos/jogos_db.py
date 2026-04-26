import sqlite3

def conectar():
    conn = sqlite3.connect('jogos.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            adversario TEXT,
            placar TEXT,
            competicao TEXT,
            local TEXT
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_jogo():
    conn = conectar()
    cursor = conn.cursor()

    data = input("Data do jogo (ex: 23/04/2026): ")
    adversario = input("Adversário: ")
    placar = input("Placar (ex: 3x1): ")
    competicao = input("Competição: ")
    local = input("Local (casa/fora): ")

    cursor.execute("""
        INSERT INTO jogos (data, adversario, placar, competicao, local)
        VALUES (?, ?, ?, ?, ?)
    """, (data, adversario, placar, competicao, local))

    conn.commit()
    conn.close()
    print("✅ Jogo cadastrado com sucesso!")

def listar_jogos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()
    conn.close()

    if len(jogos) == 0:
        print("Nenhum jogo cadastrado ainda.")
        return

    for jogo in jogos:
        print(f"\n🔴 Jogo #{jogo[0]}")
        print(f"   Data: {jogo[1]}")
        print(f"   Adversário: {jogo[2]}")
        print(f"   Placar: {jogo[3]}")
        print(f"   Competição: {jogo[4]}")
        print(f"   Local: {jogo[5]}")

def atualizar_jogo():
    listar_jogos()
    id_jogo = int(input("\nDigite o ID do jogo que deseja atualizar: "))

    data = input("Nova data (deixe em branco para manter): ")
    adversario = input("Novo adversário (deixe em branco para manter): ")
    placar = input("Novo placar (deixe em branco para manter): ")
    competicao = input("Nova competição (deixe em branco para manter): ")
    local = input("Novo local (deixe em branco para manter): ")

    conn = conectar()
    cursor = conn.cursor()

    if data: cursor.execute("UPDATE jogos SET data = ? WHERE id = ?", (data, id_jogo))
    if adversario: cursor.execute("UPDATE jogos SET adversario = ? WHERE id = ?", (adversario, id_jogo))
    if placar: cursor.execute("UPDATE jogos SET placar = ? WHERE id = ?", (placar, id_jogo))
    if competicao: cursor.execute("UPDATE jogos SET competicao = ? WHERE id = ?", (competicao, id_jogo))
    if local: cursor.execute("UPDATE jogos SET local = ? WHERE id = ?", (local, id_jogo))

    conn.commit()
    conn.close()
    print("✅ Jogo atualizado com sucesso!")

def deletar_jogo():
    listar_jogos()
    id_jogo = int(input("\nDigite o ID do jogo que deseja deletar: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jogos WHERE id = ?", (id_jogo,))
    conn.commit()
    conn.close()
    print("✅ Jogo deletado com sucesso!")

def menu():
    criar_tabela()
    while True:
        print("\n===== FLA CRUD =====")
        print("1 - Cadastrar jogo")
        print("2 - Listar jogos")
        print("3 - Atualizar jogo")
        print("4 - Deletar jogo")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_jogo()
        elif opcao == "2":
            listar_jogos()
        elif opcao == "3":
            atualizar_jogo()
        elif opcao == "4":
            deletar_jogo()
        elif opcao == "0":
            print("Até mais! Mengão! 🔴⚫")
            break
        else:
            print("Opção inválida.")

menu()