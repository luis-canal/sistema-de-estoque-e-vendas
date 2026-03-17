from sistema.sistema_estoque import *

def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrarCliente()

        elif opcao == "2":
            listarClientes()

        elif opcao == "3":
            cadastrarProduto()

        elif opcao == "4":
            listarProdutos()

        elif opcao == "0":
            break

        else:
            print("Opção inválida")
            return False
        
menu()