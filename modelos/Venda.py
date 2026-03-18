from modelos.Produto import Produto

class Venda:

    def __init__(self, id, cliente, produto, quantidade):
        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = produto.preco * quantidade