from sistema.sistema_estoque import SistemaEstoque

def menu():
    sistema = SistemaEstoque()

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Desfazer operação")
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
            sistema.desfazer_ultima_operacao()

        elif opcao == "0":
            break

        else:
            print("Opção inválida")


menu()