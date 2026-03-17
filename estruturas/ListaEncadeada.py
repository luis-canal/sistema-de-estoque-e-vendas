from Nodo import Nodo

class LSE:

    def __init__(self):
        self.head = None
        self.tail = None
        self.quantidade_itens = 0

    def is_empty(self):
        return self.quantidade_itens == 0 or self.head == None

    def inserir_inicio(self, dado_a_ser_inserido):
        self.quantidade_itens += 1

        if self.is_empty():
            nodo = Nodo(dado_a_ser_inserido)
            self.head = nodo
            self.tail = nodo
            return
        
        head_armazenado = self.head
        self.head = Nodo(dado_a_ser_inserido)
        self.head.proximo = head_armazenado

    def inserir_fim(self, dado_a_ser_inserido):
        self.quantidade_itens += 1

        if self.is_empty():
            nodo = Nodo(dado_a_ser_inserido)
            self.head = nodo
            self.tail = nodo
            return

        tail_armazenado = self.tail
        nodo = Nodo(dado_a_ser_inserido)
        tail_armazenado.proximo = nodo
        self.tail = nodo

    def remover_inicio(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        self.quantidade_itens -= 1

        if self.head == self.tail:
            dado_removido = self.tail
            self.head = None
            self.tail = None
            return dado_removido
        
        dado_removido = self.head
        self.head = dado_removido.proximo
        dado_removido.proximo = None

        return dado_removido
        
    def remover_fim(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        self.quantidade_itens -= 1

        if self.head == self.tail:
            dado_removido = self.tail
            self.head = None
            self.tail = None
            return dado_removido
        
        dado_removido = None
        atual = self.head

        while atual != None:
            if (atual.proximo != None and atual.proximo == self.tail):
                dado_removido = self.tail
                self.tail = atual
                atual.proximo = None
                return dado_removido
            
            atual = atual.proximo

    def imprimir_lista_completa(self):
        atual = self.head
        while atual != None:
            print(atual)
            atual = atual.proximo

    def imprimir_lado_a_lado(self):
        saida = ""
        atual = self.head

        while atual != None:
            if atual == self.head:
                saida += '[' + str(atual) + ']'
            else:
                saida += '=>' + '[' + str(atual) + ']'

            atual = atual.proximo
            
        print(saida)
