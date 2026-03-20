from sistema.sistema_estoque import SistemaEstoque
import os, time

def menu():
    sistema = SistemaEstoque()

    while True:
# ===== MENU ESTOQUE =====
# 1 - Cadastrar cliente (certo)
# 2 - Listar clientes (certo)
# 3 - Cadastrar produto (certo)
# 4 - Listar produtos (certo)
# remover cliente NOVO
# remover produto NOVO
# 5 - Pesquisar produto 
# 6 - Realizar venda
# 7 - Ver fila de vendas
# 8 - Desfazer última operação (certo)
# 9 - Exibir valor total do estoque
# 10 - Exibir valor total de vendas
# 11 - Exibir clientes e valores gastos
# 12 - Sair (certo)
# ========================
        print("\n===== MENU ESTOQUE =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Desfazer última operação")
        print("6 - Remover cliente(id)")
        print("7 - Remover produto(id)")
        print("0 - Sair")
        print("========================")

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
            print("Saindo...")
            time.sleep(2)
            break

        else:
            print("Opção inválida, tente novamente")


menu()