class Venda:

    def __init__(self, id, cliente, produto, quantidade):
        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = produto.preco * quantidade

    def __str__(self):
        return f"Venda {self.id} | Cliente: {self.cliente.nome} | Produto: {self.produto.nome} | Qtd: {self.quantidade} | Total: {self.valor_total}"