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

    def pausar(self):
        input("\nPressione ENTER para voltar ao menu...")

    def _registrar_operacao(self, tipo, dados):
        self.pilha.push({"tipo": tipo, "dados": dados})

    def _gerar_id_produto(self):
        idAtual = self.proximoIdProduto
        self.proximoIdProduto += 1
        return idAtual

    def cadastrar_produto(self):
        try:
            nome = input("Nome: ")

            if not nome.strip():
                print("Nome do produto não pode ser vazio!")
                self.pausar()
                return

            atual = self.produtos.head
            while atual:
                if atual.valor.nome.lower() == nome.lower():
                    print("Já existe um produto com esse nome!")
                    self.pausar()
                    return
                atual = atual.proximo

            while True:
                try:
                    quantidade = int(input("Quantidade: "))
                    if quantidade > 0:
                        break
                    print("Quantidade deve ser maior que 0.")
                except ValueError:
                    print("Digite um número válido para quantidade!")

            while True:
                try:
                    preco = float(input("Preço: "))
                    if preco > 0:
                        break
                    print("Preço deve ser maior que 0.")
                except ValueError:
                    print("Digite um valor válido para o preço!")

            p = Produto(
                self._gerar_id_produto(),
                nome,
                quantidade,
                preco
            )

            self.produtos.inserir_fim(p)
            self._registrar_operacao("add_prod", p)
            salvar_produtos(self.produtos)

            print(f"Produto '{nome}' cadastrado com sucesso!")
            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def listar_produtos(self):
        self.produtos.imprimir_lado_a_lado()
        self.pausar()

    def buscar_produto(self, id):
        return self.produtos.buscar(id)
    
    def buscar_produto_por_nome(self, nome):
        atual = self.produtos.head

        while atual:
            if atual.valor.nome.lower() == nome.lower():
                return atual.valor
            atual = atual.proximo

        return None

    def pesquisar_produto_nome(self):
        try:
            nome = input("Nome do produto: ")
            produto = self.buscar_produto_por_nome(nome)

            if produto:
                print(f"""
ID: {produto.id}
Nome: {produto.nome}
Quantidade: {produto.quantidade}
Preço: R$ {produto.preco}
                        """)
                self.pausar()
            else:
                print("Produto não encontrado!")
                self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def remover_produto(self):
        try:
            if self.produtos.is_empty():
                print("Nenhum produto cadastrado!")
                self.pausar()
                return

            try:
                id = int(input("ID produto: "))
            except ValueError:
                print("ID inválido! Digite um número.")
                self.pausar()
                return
            removido = self.produtos.remover_por_id(id)

            if removido:
                self._registrar_operacao("remover_prod", removido)
                salvar_produtos(self.produtos)
                print(f"Produto {removido} removido!")
                self.pausar()
            else:
                print("Produto não encontrado!")
                self.pausar()

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
                self.pausar()
                return
            
            # Outro Brique para verificar nome duplicado
            atual = self.clientes.head
            while atual:
                if atual.valor.nome.strip().lower() == nomeCliente.strip().lower():
                    print("Já existe um cliente com esse nome!")
                    self.pausar()
                    return
                atual = atual.proximo

            idCliente = self._gerar_id_cliente()
            c = Cliente(idCliente, nomeCliente)

            self.clientes.inserir_fim(c)
            self._registrar_operacao("add_cli", c)
            salvar_clientes(self.clientes)

            print(f"Cliente cadastrado! ID: {idCliente} | Nome: {nomeCliente}")
            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def listar_clientes(self):
        self.clientes.imprimir_lado_a_lado()
        self.pausar()

    def buscar_cliente(self, id):
        return self.clientes.buscar(id)
    
    def buscar_cliente_por_nome(self, nome):
        atual = self.clientes.head

        while atual:
            if atual.valor.nome.strip().lower() == nome.strip().lower():
                return atual.valor
            atual = atual.proximo

        return None

    def pesquisar_cliente_nome(self):
        try:
            nome = input("Nome do cliente: ")
            cliente = self.buscar_cliente_por_nome(nome)

            if cliente:
                print(f"""
ID: {cliente.id}
Nome: {cliente.nome}
                """)
                self.pausar()
            else:
                print("Cliente não encontrado!")
                self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def remover_cliente(self):
        try:
            if self.clientes.is_empty():
                print("Nenhum cliente cadastrado!")
                self.pausar()
                return

            try:
                id = int(input("ID cliente: "))
            except ValueError:
                print("ID inválido! Digite um número.")
                self.pausar()
                return
            removido = self.clientes.remover_por_id(id)

            if removido:
                self._registrar_operacao("remover_cli", removido)
                salvar_clientes(self.clientes)
                print(f"Cliente {removido} removido com sucesso!")
                self.pausar()
            else:
                print("Cliente não encontrado!")
                self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def _gerar_id_venda(self):
        if self.vendas.is_empty():
            return 1
        return self.vendas._itens[-1].id + 1

    def registrar_venda(self):
        try:
            id = self._gerar_id_venda()
            try:
                id_cliente = int(input("ID cliente: "))
            except ValueError:
                print("ID inválido! Digite um número.")
                self.pausar()
                return
            cliente = self.buscar_cliente(id_cliente)
            try:
                id_produto = int(input("ID produto: "))
            except ValueError:
                print("ID inválido! Digite um número.")
                self.pausar()
                return
            produto = self.buscar_produto(id_produto)
            try:
                qtd = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida!")
                self.pausar()
                return
            if not cliente or not produto:
                print("Cliente ou produto inválido, tente novamente!")
                time.sleep(2)
                return

            if qtd <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                return

            if produto.quantidade < qtd:
                print("Estoque insuficiente, tente novamente!")
                time.sleep(2)
                return

            venda = Venda(id, cliente, produto, qtd)

            produto.quantidade -= qtd
            self.vendas.enfileirar(venda)

            self._registrar_operacao("venda", venda)
            salvar_vendas(self.vendas)
            salvar_produtos(self.produtos)

            print(f"""
Venda realizada com sucesso!
ID: {id}
Cliente: {cliente.nome}
Produto: {produto.nome}
Quantidade: {qtd}
Total: R$ {produto.preco * qtd:.2f}
""")
            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def listar_vendas(self):
        try:
            if self.vendas.is_empty():
                print("Nenhuma venda registrada!")
                self.pausar()
                return

            print("\n===== FILA DE VENDAS =====\n")

            for venda in self.vendas._itens:
                print(f"""
ID: {venda.id}
Cliente: {venda.cliente.nome}
Produto: {venda.produto.nome}
Quantidade: {venda.quantidade}
Total: R$ {venda.produto.preco * venda.quantidade:.2f}
---------------------------
""")
            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def valor_total_vendas(self):
        try:
            if self.vendas.is_empty():
                print("Nenhuma venda registrada!")
                self.pausar()
                return

            total = 0

            for venda in self.vendas._itens:
                total += venda.produto.preco * venda.quantidade

            print(f"\n Valor total de vendas realizadas: R$ {total:.2f}")
            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")
    
    def valor_total_estoque(self):
        try:
            if self.produtos.is_empty():
                print("Nenhum produto cadastrado!")
                self.pausar()
                return

            total = 0
            atual = self.produtos.head

            while atual:
                produto = atual.valor
                total += produto.preco * produto.quantidade
                atual = atual.proximo

            print(f"\n Valor total do estoque: R$ {total:.2f}")
            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")
    
    def clientes_valores_gastos(self):
        try:
            if self.vendas.is_empty():
                print("Nenhuma venda registrada!")
                self.pausar()
                return

            gastos = {}  

            for venda in self.vendas._itens:
                nome = venda.cliente.nome
                total = venda.produto.preco * venda.quantidade

                if nome in gastos:
                    gastos[nome] += total
                else:
                    gastos[nome] = total

            print("\n ===== GASTOS POR CLIENTE =====\n")

            for cliente, valor in sorted(gastos.items(), key=lambda x: x[1], reverse=True):
                print(f"Cliente: {cliente}")
                print(f"Total gasto: R$ {valor:.2f}")
                print("---------------------------")

            self.pausar()

        except Exception as e:
            print(f"Erro: {e}")

    def desfazer(self):
        if self.pilha.is_empty():
            print("Nada para desfazer")
            self.pausar()
            return

        op = self.pilha.pop()

        if op["tipo"] == "add_prod":
            self.produtos.remover_por_id(op["dados"].id)
            print(f"Desfeito: cadastro do produto '{op['dados'].nome}'")

        elif op["tipo"] == "add_cli":
            self.clientes.remover_por_id(op["dados"].id)
            print(f"Desfeito: cadastro do cliente '{op['dados'].nome}'")

        elif op["tipo"] == "venda":
            p = self.buscar_produto(op["dados"].produto.id)
            if p:
                p.quantidade += op["dados"].quantidade
            if not self.vendas.is_empty():
                self.vendas._itens.pop()
            print(f"Desfeito: venda do produto '{op['dados'].produto.nome}' (quantidade: {op['dados'].quantidade})")

        elif op["tipo"] == "remover_prod":
            self.produtos.inserir_fim(op["dados"])
            print(f"Desfeito: remoção do produto '{op['dados'].nome}'")

        elif op["tipo"] == "remover_cli":
            self.clientes.inserir_fim(op["dados"])
            print(f"Desfeito: remoção do cliente '{op['dados'].nome}'")

        self.pausar()
        salvar_clientes(self.clientes)
        salvar_produtos(self.produtos)
        salvar_vendas(self.vendas)