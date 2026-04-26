import json
import os

ARQUIVO = "jogos.json"

def carregar_jogos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_jogos():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(jogos, f, ensure_ascii=False, indent=4)
jogos = carregar_jogos()

def cadastrar_jogo():
    data = input("Data do jogo (ex: 23/04/2026): ")
    adversario = input("Adversário: ")
    placar = input("Placar (ex: 3x1): ")
    competicao = input("Competição: ")
    local = input("Local (casa/fora): ")

    jogo = {
        "id": len(jogos) + 1,
        "data": data,
        "adversario": adversario,
        "placar": placar,
        "competicao": competicao,
        "local": local
    }

    jogos.append(jogo)
    print("✅ Jogo cadastrado com sucesso!")
    salvar_jogos()

def listar_jogos():
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado ainda.")
        return
    for jogo in jogos:
        print(f"\n🔴 Jogo #{jogo['id']}")
        print(f"   Data: {jogo['data']}")
        print(f"   Adversário: {jogo['adversario']}")
        print(f"   Placar: {jogo['placar']}")
        print(f"   Competição: {jogo['competicao']}")
        print(f"   Local: {jogo['local']}")


def atualizar_jogo():
    listar_jogos()
    if len(jogos) == 0:
        return
    id_jogo = int(input("\nDigite o ID do jogo que deseja atualizar: "))

    jogo = None
    for j in jogos:
        if j["id"] == id_jogo:
            jogo = j
            break

    if jogo is None:
        print("Jogo não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")

    data = input(f"Data ({jogo['data']}): ")
    adversario = input(f"Adversário ({jogo['adversario']}): ")
    placar = input(f"Placar ({jogo['placar']}): ")
    competicao = input(f"Competição ({jogo['competicao']}): ")
    local = input(f"Local ({jogo['local']}): ")

    if data: jogo["data"] = data
    if adversario: jogo["adversario"] = adversario
    if placar: jogo["placar"] = placar
    if competicao: jogo["competicao"] = competicao
    if local: jogo["local"] = local

    print("✅ Jogo atualizado com sucesso!")
    salvar_jogos()


def deletar_jogo():
    listar_jogos()
    if len(jogos) == 0:
        return
    id_jogo = int(input("\nDigite o ID do jogo que deseja deletar: "))

    for j in jogos:
        if j["id"] == id_jogo:
            jogos.remove(j)
            print("✅ Jogo deletado com sucesso!")
            salvar_jogos()
            return

    print("Jogo não encontrado.")

def menu():
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