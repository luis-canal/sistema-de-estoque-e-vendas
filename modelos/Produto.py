class Produto:

    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.id} - {self.nome} | Qtd: {self.quantidade} | R$ {self.preco:.2f}"