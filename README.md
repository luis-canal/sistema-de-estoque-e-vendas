# Sistema de Controle de Estoque e Vendas

## Disciplina

**Organização e Abstração na Programação**

---

**Estrutura de Dados com Python**

---

## Integrantes

* Guilherme Menzen
* Guilherme Vassoler Daros
* Eduardo Pagliarini Herter
* Kaiki André Pauletto
* Luis Eduardo Brescansin Canal
* Luis Vieira

---

## Descrição do Sistema

Este projeto consiste em um sistema de controle de estoque e vendas desenvolvido em Python, com foco na aplicação prática de estruturas de dados.

O sistema permite:

* Cadastro, listagem, busca e remoção de **produtos**
* Cadastro, listagem, busca e remoção de **clientes**
* Registro e controle de **vendas**
* Cálculo de:

  * Valor total das vendas
  * Valor total do estoque
  * Ranking de clientes por valor gasto
* Funcionalidade de **desfazer operações (undo)** utilizando pilha

O objetivo principal é simular um sistema real de gerenciamento, aplicando conceitos fundamentais de programação e organização de dados.

---

## Estruturas de Dados Utilizadas

O sistema foi desenvolvido utilizando estruturas de dados implementadas manualmente, sem uso de bibliotecas prontas:

### Lista Encadeada Simples (LSE)

Utilizada para armazenar:

* Produtos
* Clientes

Permite:

* Inserção dinâmica
* Remoção por ID
* Percorrimento eficiente dos dados

---

### Fila (Queue)

Utilizada para armazenar:

* Vendas

Segue o princípio **FIFO (First In, First Out)**:

* A primeira venda registrada é a primeira a ser processada

---

### Pilha (Stack)

Utilizada para:

* Controle de operações realizadas no sistema

Permite a funcionalidade de:

* **Desfazer ações (Undo)**

Segue o princípio **LIFO (Last In, First Out)**:

* A última operação realizada é a primeira a ser desfeita

---

## Persistência de Dados

O sistema utiliza persistência automática em arquivos `.csv`, garantindo que os dados não sejam perdidos ao encerrar a execução.

Arquivos utilizados:

* `clientes.csv`
* `produtos.csv`
* `vendas.csv`

### Funcionamento:

* Ao iniciar o sistema:

  * Os dados são carregados automaticamente dos arquivos
* Ao realizar alterações:

  * Os dados são salvos automaticamente

Isso garante:

* Continuidade dos dados
* Simulação de um sistema real

---

## Instruções de Execução

### Pré-requisitos:

* Python 3 instalado

---

### Passos:

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd nome-do-projeto
```

3. Execute o sistema:

```bash
python main.py
```

---

### Estrutura básica do projeto:

```bash
/main.py
/estruturas
    ListaEncadeada.py
    Pilha.py
    Fila.py
/modelos
    Cliente.py
    Produto.py
    Venda.py
/sistema
    sistema_estoque.py
    persistencia.py
/dados
    clientes.csv
    produtos.csv
    vendas.csv
```