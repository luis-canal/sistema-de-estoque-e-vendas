from sistema.sistema_estoque import SistemaEstoque
import os, time

def menu():
    sistema = SistemaEstoque()

    while True:
# ===== MENU ESTOQUE =====

# *** fazer um negocio para só sair da fila de vendas, cliente e prodtos ao apertar alguma tecla

# 1 - Cadastrar cliente (certo)
# 2 - Listar clientes (certo)
# 3 - Cadastrar produto (certo)
# 4 - Listar produtos (certo)
# remover cliente NOVO (certo)
# remover produto NOVO (certo)
# 5 - Pesquisar produto (certo)
# pesquisar cliente NOVO (certo)
# 6 - Realizar venda (certo)
# 7 - Ver fila de vendas (certo)
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
        print("8 - Pesquisar produto")
        print("9 - Pesquisar Cliente")
        print("10 - Realizar venda")
        print("11 - Listar vendas")
        print("12 - Exibir valor total de estoque")
        print("13 - Exibir valor total de vendas")
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

        elif opcao == "8":
            sistema.pesquisar_produto_nome()

        elif opcao == "9":
            sistema.pesquisar_cliente_nome()
        
        elif opcao == "10":
            sistema.registrar_venda()
        
        elif opcao == "11":
            sistema.listar_vendas()
        
        elif opcao == "12":
            sistema.valor_total_estoque()
        
        elif opcao == "13":
            sistema.valor_total_vendas()

        elif opcao == "0":
            print("Saindo...")
            time.sleep(2)
            os.system("cls")
            break

        else:
            print("Opção inválida, tente novamente")
            time.sleep(2)
            os.system("cls")

menu()