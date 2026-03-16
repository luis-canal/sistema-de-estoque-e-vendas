class Fila:

    def __init__(self):
        self._itens = []

    def enfileirar(self, item):
        self._itens.append(item) # sempre vai adicionar no final da lista

    def desinfileirar(self):
        if self.is_empty(): # a verdade para desinfileirar, é que precisar ter algum dado na fila
            print("A fila está vazia")
            return
