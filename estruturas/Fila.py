class Fila:

    def __init__(self):
        self._itens = []

    def enfileirar(self, item):
        self._itens.append(item)

    def desinfileirar(self):
        if self.is_empty():
            print("A fila está vazia")
            return
        
        return self._itens.pop(0)

    def proximo_a_sair_da_fila(self):
        return self._itens[0]
    
    def is_empty(self):
        return len(self._itens) == 0
    
    def __len__(self):
        return len(self._itens)

    def __str__(self):
        return str(self._itens)
