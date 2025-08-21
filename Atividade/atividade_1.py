#lisata de nomes

def menu():
    print("\n--- MENU ---")
    print("1 - Adicionar nome")
    print("2 - Pesquisar nome")
    print("3 - Alterar nome")
    print("4 - Excluir nome")
    print("5 - Mostrar lista")
    print("0 - Sair")

lista = []
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        lista.append(nome)
        print("Nome adicionado!")

    elif opcao == "2":
        nome = input("Digite o nome a pesquisar: ")
        if nome in lista:
            print(f"{nome} está na lista.")
        else:
            print(f"{nome} não foi encontrado.")

    elif opcao == "3":
        antigo = input("Digite o nome que deseja alterar: ")
        if antigo in lista:
            novo = input("Digite o novo nome: ")
            lista[lista.index(antigo)] = novo
            print("Nome alterado com sucesso!")
        else:
            print("Nome não encontrado.")

    elif opcao == "4":
        nome = input("Digite o nome a excluir: ")
        if nome in lista:
            lista.remove(nome)
            print("Nome excluído!")
        else:
            print("Nome não encontrado.")

    elif opcao == "5":
        print("Lista atual:", lista)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
