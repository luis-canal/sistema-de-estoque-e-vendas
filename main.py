from sistema.sistema_estoque import SistemaEstoque
import os

def menu():
    sistema = SistemaEstoque()

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Desfazer operação")
        print("6 - Remover cliente(id)")
        print("7 - Remover produto(id)")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            sistema.cadastrar_cliente()

        elif opcao == "2":
            sistema.listar_clientes()

        elif opcao == "3":
            sistema.cadastrar_produto()

        elif opcao == "4":
            sistema.listar_produtos()

        elif opcao == "5":
            sistema.desfazer()
        
        elif opcao == "6":
            sistema.remover_cliente()

        elif opcao == "7":
            sistema.remover_produto()

        elif opcao == "0":
            break

        else:
            print("Opção inválida")


menu()