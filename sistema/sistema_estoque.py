from modelos.Cliente import Cliente
from modelos.Produto import Produto
from modelos.Venda import Venda

# Listas provisórias
listaClientes = []
listaProdutos = []
listaVendas = []


def cadastrarCliente():
    nome = input("Nome do CLiente: ")
    id = len(listaClientes) + 1

    cliente = Cliente(id, nome)
    listaClientes.append(cliente)

def listarClientes():
    for cliente in listaClientes:
        print(cliente.id, cliente.nome)

def cadastrarProduto():
    nome = input("Nome do Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    id = len(listaProdutos) + 1

    produto = Produto(id, nome, quantidade, preco)
    listaProdutos.append(produto)

def listarProdutos():
    for produto in listaProdutos:
        print(produto.id, produto.nome, produto.quantidade, produto.preco)