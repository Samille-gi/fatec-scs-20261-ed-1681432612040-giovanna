"""
--------------------------------------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* B1-3                                                                            *
* *
* Autor: 1681432612040 - nome: Giovanna Samille Gonçalves da silva                           *
* Objetivo:  Simular uma Calculadora HP12c (Pilha RPN)                                                                                  *
* data: 31/03/2026                                                                           *
---------------------------------------------------------------------------------------------
"""

class pilha:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Z = 0
        self.T = 0

        self.count = 0

    def visualizar(self):
        print(f"X = {self.X}\nY = {self.Y}\nZ = {self.Z}\nT = {self.T}\n")
    
    def desempilhar(self, resultado):
        self.X = resultado
        self.Y = self.Z
        self.Z = self.T

        if self.count > 1:
            self.count -= 1
    
    def empilhar(self, item):
        if self.count > 4:
            raise OverflowError ("Pilha cheia! O máximo é 4 elementos (X, Y, Z, T)")

        self.T = self.Z
        self.Z = self.Y
        self.Y = self.X
        self.X = float(item)

        self.count += 1

class  hp12c(pilha):
    def __init__(self):
        super().__init__() 

    def empilhar(self, item):
        super().empilhar(float(item))

    def verificar(self, item):
        if item not in ["+", "-", "*", "/"]:
            raise ValueError("Operador inválido!")

        a = self.Y
        b = self.X

        if item == "+":
            resultado = a + b

        elif item == "-":
            resultado = a - b

        elif item == "*":
            resultado = a * b

        elif item == "/":
            resultado = a / b

        self.desempilhar(resultado)
        
class conversao(pilha):
    def __init__(self):
        super().__init__()
        self.pilha = []

    def empilhar(self, item):
        self.pilha.append(item)

    def acrescentar(self, item):
        b = self.pilha.pop()
        a = self.pilha.pop()

        self.pilha.append(f"({a} {item} {b})")
    
minha_pilha = hp12c()
minha_pilha2 = conversao()
rpn = input("Digite a expressão RPN: ")
expressao = rpn.split()

try:
    for item in expressao:
        if item.replace('.', '', 1).isdigit():
            minha_pilha.empilhar(item)
            minha_pilha2.empilhar(item)
        else:
            minha_pilha.verificar(item)
            minha_pilha2.acrescentar(item)
        minha_pilha.visualizar()

except ValueError as e:
    print(f"Erro: {e}")
     
print(*minha_pilha2.pilha)
print(f"O resultado da expressão algébrica é: {minha_pilha.X:.0f}")







