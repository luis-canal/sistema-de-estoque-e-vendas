import csv
import os

CAMINHO_CLIENTES = "dados/clientes.csv"
CAMINHO_PRODUTOS = "dados/produtos.csv"
CAMINHO_VENDAS = "dados/vendas.csv"

from modelos.Cliente import Cliente
from modelos.Produto import Produto
from modelos.Venda import Venda


def garantir_arquivo(caminho, cabecalho):
    if not os.path.exists(caminho):
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(cabecalho)

def carregar_clientes(lista_clientes):
    garantir_arquivo(CAMINHO_CLIENTES, ["id", "nome"])

    with open(CAMINHO_CLIENTES, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for linha in reader:
            c = Cliente(int(linha["id"]), linha["nome"])
            lista_clientes.inserir_fim(c)


def carregar_produtos(lista_produtos):
    garantir_arquivo(CAMINHO_PRODUTOS, ["id", "nome", "quantidade", "preco"])

    with open(CAMINHO_PRODUTOS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for linha in reader:
            p = Produto(
                int(linha["id"]),
                linha["nome"],
                int(linha["quantidade"]),
                float(linha["preco"])
            )
            lista_produtos.inserir_fim(p)


def carregar_vendas(fila_vendas, lista_clientes, lista_produtos):
    garantir_arquivo(CAMINHO_VENDAS, ["id", "cliente_id", "produto_id", "quantidade", "total"])

    with open(CAMINHO_VENDAS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for linha in reader:
            cliente = lista_clientes.buscar(int(linha["cliente_id"]))
            produto = lista_produtos.buscar(int(linha["produto_id"]))

            if cliente and produto:
                v = Venda(
                    int(linha["id"]),
                    cliente,
                    produto,
                    int(linha["quantidade"])
                )
                fila_vendas.enfileirar(v)

def salvar_clientes(lista_clientes):
    garantir_arquivo(CAMINHO_CLIENTES, ["id", "nome"])

    with open(CAMINHO_CLIENTES, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nome"])

        atual = lista_clientes.head
        while atual:
            c = atual.valor
            writer.writerow([c.id, c.nome])
            atual = atual.proximo

def salvar_produtos(lista_produtos):
    garantir_arquivo(CAMINHO_PRODUTOS, ["id", "nome", "quantidade", "preco"])

    with open(CAMINHO_PRODUTOS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nome", "quantidade", "preco"])

        atual = lista_produtos.head
        while atual:
            p = atual.valor
            writer.writerow([p.id, p.nome, p.quantidade, p.preco])
            atual = atual.proximo

def salvar_vendas(fila_vendas):
    garantir_arquivo(CAMINHO_VENDAS, ["id", "cliente_id", "produto_id", "quantidade", "total"])

    with open(CAMINHO_VENDAS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "cliente_id", "produto_id", "quantidade", "total"])

        for v in fila_vendas._itens:
            writer.writerow([v.id, v.cliente.id, v.produto.id, v.quantidade, v.valor_total])