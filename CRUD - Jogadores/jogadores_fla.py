jogadores = []

def cadastrar_jogador():
    nome = input("Digite o nome do jogador: ")
    nascimento = input("Digite a data de nascimento do jogador: ")
    clube_anterior = input("Digite o nome do clube anterior do jogador: ")
    convocacoes = input("Digite o número de convocações do jogador: ")
    idade = input("Digite a idade do jogador: ")
    contrato = input("Digite a data do contrato do jogador: ")

    jogador = {
        "id": len(jogadores) + 1,
        "nome": nome,
        "nascimento": nascimento,
        "clube_anterior": clube_anterior,
        "convocacoes": convocacoes,
        "idade": idade,
        "contrato": contrato,
    }

    jogadores.append(jogador)
    print("✅ Jogador cadastrado com sucesso!")

def listar_jogadores():
    if len(jogadores) == 0:
        print("Nenhum jogador encontrado!")
        return
    for jogador in jogadores:
        print(f"\n🔴 Nome: {jogador['id']}")
        print(f"Nascimento: {jogador['nascimento']}")
        print(f"clube_anterior = {jogador['clube_anterior']}")
        print(f"convocacoes = {jogador['convocacoes']}")
        print(f"idade = {jogador['idade']}")
        print(f"contrato = {jogador['contrato']}")

def atualizar_jogador():
    listar_jogadores()
    if len(jogadores) == 0:
        return
    id_jogador = int(input("Digite o id do jogador: "))

    jogador = None
    for j in jogadores:
        if j['id'] == id_jogador:
            jogador = j
            break
    if jogador is None:
        print("Nenhum jogador encontrado!")
        return

    print("Deixe em branco para manter o valor atual.")

    nome = input("Digite o nome do jogador: ")
    nascimento = input("Digite o nascimento do jogador: ")
    clube_anterior = input("Digite o nome do clube anterior do jogador: ")
    convocacoes = input("Digite o número de convocações do jogador: ")
    idade = input("Digite a idade do jogador: ")
    contrato = input("Digite a data do contrato do jogador: ")

    if nome: jogador["nome"] = nome
    if nascimento: jogador["nascimento"] = nascimento
    if clube_anterior: jogador["clube_anterior"] = clube_anterior
    if convocacoes: jogador["convocacoes"] = convocacoes
    if idade: jogador["idade"] = idade
    if contrato: jogador["contrato"] = contrato

    print("✅ Jogador atualizado com sucesso!")

def deletar_jogador():
    listar_jogadores()
    if len(jogadores) == 0:
        return
    id_jogador = int(input("Digite o id do jogador: "))

    for j in jogadores:
        if j['id'] == id_jogador:
            jogadores.remove(j)
            print("✅ Jogador deletado com sucesso!")
            return

    print("Nenhum jogador encontrado!")

def menu():
    while True:
        print("\n======LISTA JOGADORES - CR FLAMENGO=====")
        print("[1] Cadastrar jogador")
        print("[2] Listar jogadores")
        print("[3] Atualizar jogador")
        print("[4] Deletar jogador")
        print("0 - Sair")

        opcao = input("Digite sua opcao: ")

        if opcao == "1":
            cadastrar_jogador()
        elif opcao == "2":
            listar_jogadores()
        elif opcao == "3":
            atualizar_jogador()
        elif opcao == "4":
            deletar_jogador()
        elif opcao == "0":
            print("Até mais, Saudações Rubro Negras 🔴⚫!!!")
            break
        else:
            print("Opção inválida, tente novamente")

menu()




