"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B2-3                                                                             *
* *
* Autor: 1681432612040 - nome: Giovanna Samille Gonçalves da silva                             *
* Objetivo:
* data: 11/05/2026                                                                           *
---------------------------------------------------------------------------------------------
"""
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self, raiz = None):
        self.raiz = raiz
    
    def inserirRaiz (self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.inserir(valor, self.raiz)

    def inserir(self, valor, noAtual):
        if valor > noAtual.valor:
            if noAtual.direita == None:
                noAtual.direita = No(valor)
            else:
                noAtual = noAtual.direita
                self.inserir(valor, noAtual)
        else:
            if noAtual.esquerda == None:
                noAtual.esquerda = No(valor)
            else:
                noAtual = noAtual.esquerda
                self.inserir(valor, noAtual)

    def buscar(self, no, valor):
        if no == None:
            return None

        if no.valor == valor:
            return no

        esq = self.buscar(no.esquerda, valor)
        if esq != None:
            return esq

        return self.buscar(no.direita, valor)

    def analisar_arvore(self, valor_busca):
        print("Raiz:", self.raiz.valor)

        print("Nós internos e folhas:")
        self.imprimir_nos_internos(self.raiz)

        print("Níveis:")
        self.imprimir_niveis()

        no = self.buscar(self.raiz, valor_busca)

        if no == None:
            print("não achou")
            return

        grau = 0
        if no.esquerda != None:
            grau += 1
        if no.direita != None:
            grau += 1

        print("Valor:", no.valor)
        print("Grau:", grau)

        print("Ancestrais:")
        self.imprimir_ancestrais(self.raiz, valor_busca)

        print("Descendentes:")
        self.imprimir_descendentes(no.esquerda)
        self.imprimir_descendentes(no.direita)

        print("Altura:", self.calcular_altura(no))
        print("Profundidade:", self.calcular_profundidade(self.raiz, valor_busca))

    def imprimir_nos_internos(self, noAtual): 
        if noAtual == None:
            return
        
        if noAtual.direita == None and noAtual.esquerda == None:
            self.imprimir_folhas(noAtual.valor)
        else:
            print(f"Nós internos: {noAtual.valor}")
        
        self.imprimir_nos_internos(noAtual.esquerda)
        self.imprimir_nos_internos(noAtual.direita)

    def imprimir_folhas(self, valor):
        print(f"Folhas: {valor}")

    def imprimir_niveis(self):
        fila = [self.raiz]

        while len(fila) > 0:
            noAtual = fila[0]
            fila.pop(0)

            if noAtual != None:
                print(noAtual.valor)

                fila.append(noAtual.esquerda)
                fila.append(noAtual.direita)

    def calcular_altura(self, no):
        if no == None:
            return 0

        esq = self.calcular_altura(no.esquerda)
        dir = self.calcular_altura(no.direita)

        if esq > dir:
            return esq + 1
        else:
            return dir + 1
        
    def calcular_profundidade(self, no, valor, nivel=0):
        if no == None:
            return -1

        if no.valor == valor:
            return nivel

        esq = self.calcular_profundidade(no.esquerda, valor, nivel + 1)
        if esq != -1:
            return esq

        dir = self.calcular_profundidade(no.direita, valor, nivel + 1)
        return dir

    def imprimir_ancestrais(self, no, valor):
        if no == None:
            return False

        if no.valor == valor:
            return True

        if self.imprimir_ancestrais(no.esquerda, valor) == True:
            print(no.valor)
            return True

        if self.imprimir_ancestrais(no.direita, valor) == True:
            print(no.valor)
            return True

        return False

    def imprimir_descendentes(self, no):
        if no == None:
            return

        print(no.valor)

        self.imprimir_descendentes(no.esquerda)
        self.imprimir_descendentes(no.direita)
arvore = ArvoreBST()

