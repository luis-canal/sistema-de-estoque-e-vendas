from estruturas.ListaEncadeada import LSE
from estruturas.Pilha import Pilha
from estruturas.Fila import Fila

from modelos.Cliente import Cliente
from modelos.Produto import Produto
from modelos.Venda import Venda

from sistema.persistencia import *

import time


class SistemaEstoque:

    def __init__(self):
        self.produtos = LSE()
        self.clientes = LSE()
        self.vendas = Fila()
        self.pilha = Pilha()  

        self.proximoIDCliente = 1
        self.proximoIdProduto = 1

        carregar_clientes(self.clientes)
        carregar_produtos(self.produtos)
        carregar_vendas(self.vendas, self.clientes, self.produtos)

        atual = self.clientes.head
        while atual:
            self.proximoIDCliente = max(self.proximoIDCliente, atual.valor.id + 1)
            atual = atual.proximo

        atual = self.produtos.head
        while atual:
            self.proximoIdProduto = max(self.proximoIdProduto, atual.valor.id + 1)
            atual = atual.proximo

    def _registrar_operacao(self, tipo, dados):
        self.pilha.push({"tipo": tipo, "dados": dados})

    def _gerar_id_produto(self):
        idAtual = self.proximoIdProduto
        self.proximoIdProduto += 1
        return idAtual

    def cadastrar_produto(self):
        try:
            nome = input("Nome: ")

            #Brique pra impedir cadastro de nome duplicado
            atual = self.produtos.head
            while atual:
                if atual.valor.nome.lower() == nome.lower():
                    print("Já existe um produto com esse nome!")
                    time.sleep(2)
                    return
                atual = atual.proximo

            quantidade = int(input("Quantidade: "))
            while quantidade <= 0:
                print("Quantidade inválida! Deve ser maior que 0.")
                time.sleep(2)
                quantidade = int(input("Quantidade: "))

            preco = float(input("Preço: "))
            while preco <= 0:
                print("Preço inválido! Deve ser maior que 0.")
                time.sleep(2)
                preco = float(input("Preço: "))

            p = Produto(
                self._gerar_id_produto(),
                nome,
                quantidade,
                preco
            )

            self.produtos.inserir_fim(p)
            self._registrar_operacao("add_prod", p)
            salvar_produtos(self.produtos)

            print(f"Produto {nome} cadastrado com sucesso!")
            time.sleep(2)

        except Exception as e:
            print(f"Erro: {e}")

    def listar_produtos(self):
        self.produtos.imprimir_lado_a_lado()
        time.sleep(2)

    def buscar_produto(self, id):
        return self.produtos.buscar(id)

    def remover_produto(self):
        try:
            if self.produtos.is_empty():
                print("Nenhum produto cadastrado!")
                time.sleep(2)
                return

            id = int(input("ID do produto: "))
            removido = self.produtos.remover_por_id(id)

            if removido:
                salvar_produtos(self.produtos)
                print(f"Produto {removido} removido!")
                time.sleep(2)
            else:
                print("Produto não encontrado!")
                time.sleep(2)

        except Exception as e:
            print(f"Erro: {e}")

    def _gerar_id_cliente(self):
        idAtual = self.proximoIDCliente
        self.proximoIDCliente += 1
        return idAtual

    def cadastrar_cliente(self):
        try:
            nomeCliente = input("Nome: ")

            if len(nomeCliente.strip()) < 3:
                print("Nome inválido! Insira um nome com pelo menos 3 caracteres.")
                time.sleep(2)
                return

            idCliente = self._gerar_id_cliente()
            c = Cliente(idCliente, nomeCliente)

            self.clientes.inserir_fim(c)
            self._registrar_operacao("add_cli", c)
            salvar_clientes(self.clientes)

            print(f"Cliente cadastrado! ID: {idCliente} | Nome: {nomeCliente}")
            time.sleep(2)

        except Exception as e:
            print(f"Erro: {e}")

    def listar_clientes(self):
        self.clientes.imprimir_lado_a_lado()
        time.sleep(2)

    def buscar_cliente(self, id):
        return self.clientes.buscar(id)

    def remover_cliente(self):
        try:
            if self.clientes.is_empty():
                print("Nenhum cliente cadastrado!")
                time.sleep(2)
                return

            id = int(input("ID do cliente: "))
            removido = self.clientes.remover_por_id(id)

            if removido:
                salvar_clientes(self.clientes)
                print(f"Cliente {removido} removido com sucesso!")
                time.sleep(2)
            else:
                print("Cliente não encontrado!")
                time.sleep(2)

        except Exception as e:
            print(f"Erro: {e}")

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
            salvar_vendas(self.vendas)
            salvar_produtos(self.produtos)

            print("Venda realizada")

        except Exception as e:
            print(f"Erro: {e}")

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
            if not self.vendas.is_empty():
                self.vendas._itens.pop()

        print("Desfeito")
        time.sleep(2)
        salvar_clientes(self.clientes)
        salvar_produtos(self.produtos)
        salvar_vendas(self.vendas)