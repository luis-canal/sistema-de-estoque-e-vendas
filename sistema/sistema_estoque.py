from estruturas.ListaEncadeada import LSE
from estruturas.Pilha import Pilha
from estruturas.Fila import Fila

from modelos.Cliente import Cliente
from modelos.Produto import Produto
from modelos.Venda import Venda


class SistemaEstoque:

    def __init__(self):
        self.produtos = LSE()
        self.clientes = LSE()
        self.vendas = Fila()
        self.pilha = Pilha()  
        self.proximoIDCliente = 1

    def _registrar_operacao(self, tipo, dados):
        self.pilha.push({"tipo": tipo, "dados": dados})

    def cadastrar_produto(self):
        try:
            p = Produto(
                int(input("ID: ")),
                input("Nome: "),
                int(input("Quantidade: ")),
                float(input("Preço: "))
            )

            self.produtos.inserir_fim(p)
            self._registrar_operacao("add_prod", p)

            print("Produto cadastrado")

        except:
            print("Erro")

    def listar_produtos(self):
        self.produtos.imprimir_lado_a_lado()

    def buscar_produto(self, id):
        return self.produtos.buscar(id)
    
    def _gerar_id_cliente(self):
        idAtual = self.proximoIDCliente
        self.proximoIDCliente += 1
        return idAtual

    def cadastrar_cliente(self):
        try:
            nomeCliente = input("Nome: ")
            idCliente = self._gerar_id_cliente()

            if len(nomeCliente.strip()) < 3:
                print("Nome inválido! Insira um nome com pelo menos 3 caracteres.")
                return

            c = Cliente(idCliente, nomeCliente)

            self.clientes.inserir_fim(c)
            self._registrar_operacao("add_cli", c)

            print(f"Cliente cadastrado! ID: {idCliente} | Nome: {nomeCliente}")

        except:
            print("Erro")

    def listar_clientes(self):
        self.clientes.imprimir_lado_a_lado()

    def buscar_cliente(self, id):
        return self.clientes.buscar(id)

    def registrar_venda(self):
        try:
            id = int(input("ID venda: "))
            cliente = self.buscar_cliente(int(input("ID cliente: ")))
            produto = self.buscar_produto(int(input("ID produto: ")))
            qtd = int(input("Quantidade: "))

            if not cliente or not produto:
                print("Cliente ou produto inválido")
                return

            if produto.quantidade < qtd:
                print("Estoque insuficiente")
                return

            venda = Venda(id, cliente, produto, qtd)

            produto.quantidade -= qtd
            self.vendas.enfileirar(venda)

            self._registrar_operacao("venda", venda)

            print("Venda realizada")

        except:
            print("Erro")

    def desfazer(self):
        if self.pilha.is_empty():
            print("Nada para desfazer")
            return

        op = self.pilha.pop()

        if op["tipo"] == "add_prod":
            self.produtos.remover_por_id(op["dados"].id)

        elif op["tipo"] == "add_cli":
            self.clientes.remover_por_id(op["dados"].id)

        elif op["tipo"] == "venda":
            p = self.buscar_produto(op["dados"].produto.id)
            if p:
                p.quantidade += op["dados"].quantidade

        print("Desfeito")