"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B2-3                                                                             *
* *
* Autor: 1681432612040 - nome: Giovanna Samille Gonçalves da silva                             *
* Objetivo: Implementar e analisar uma Árvore Binária de Busca (BST) em Python.*                                      *
* data: 19/05/2026                                                                           *
---------------------------------------------------------------------------------------------
"""

class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def analisar_arvore(self, valor_busca):
        print("Raiz:", self.raiz.valor)

        print("\nNós internos:")
        self.imprimir_nos_internos(self.raiz)

        print("\nFolhas:")
        self.imprimir_folhas(self.raiz)

        print("\nNíveis:")
        self.imprimir_niveis()

        print("\nAltura da árvore:", self.calcular_altura(self.raiz))

        print("Profundidade:", self.calcular_profundidade(self.raiz, valor_busca))

        print("\nAncestrais:")
        self.imprimir_ancestrais(self.raiz, valor_busca)

        print("\nDescendentes:")
        no = self.buscar(self.raiz, valor_busca)
        self.imprimir_descendentes(no)

    def imprimir_nos_internos(self, no):
        if no == None:
            return

        if no.esq != None or no.dir != None:
            print(no.valor)

        self.imprimir_nos_internos(no.esq)
        self.imprimir_nos_internos(no.dir)

    def imprimir_folhas(self, no):
        if no == None:
            return

        if no.esq == None and no.dir == None:
            print(no.valor)

        self.imprimir_folhas(no.esq)
        self.imprimir_folhas(no.dir)

    def imprimir_niveis(self):
        if self.raiz == None:
            return

        fila = [self.raiz]

        while len(fila) > 0:
            no = fila.pop(0)

            print(no.valor)

            if no.esq != None:
                fila.append(no.esq)

            if no.dir != None:
                fila.append(no.dir)

    def calcular_altura(self, no):
        if no == None:
            return 0

        esq = self.calcular_altura(no.esq)
        dir = self.calcular_altura(no.dir)

        if esq > dir:
            return esq + 1
        else:
            return dir + 1

    def calcular_profundidade(self, no, valor_busca, nivel=0):
        if no == None:
            return -1

        if no.valor == valor_busca:
            return nivel

        esq = self.calcular_profundidade(no.esq, valor_busca, nivel + 1)

        if esq != -1:
            return esq

        return self.calcular_profundidade(no.dir, valor_busca, nivel + 1)

    def imprimir_ancestrais(self, no, valor_busca):
        if no == None:
            return False

        if no.valor == valor_busca:
            return True

        if self.imprimir_ancestrais(no.esq, valor_busca):
            print(no.valor)
            return True

        if self.imprimir_ancestrais(no.dir, valor_busca):
            print(no.valor)
            return True

        return False

    def imprimir_descendentes(self, no):
        if no == None:
            return

        print(no.valor)

        self.imprimir_descendentes(no.esq)
        self.imprimir_descendentes(no.dir)

    def buscar(self, no, valor_busca):
        if no == None:
            return None

        if no.valor == valor_busca:
            return no

        esq = self.buscar(no.esq, valor_busca)

        if esq != None:
            return esq

        return self.buscar(no.dir, valor_busca)