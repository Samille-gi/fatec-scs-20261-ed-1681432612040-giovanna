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
        self.pilha = []

    def esta_vazia(self):
        return len(self.pilha) == 0
    
    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("Atenção: Operação Inválida!")
        return self.pilha.pop()
    
    def empilhar(self, item):
        self.pilha.append(item)

class  hp12c(pilha):
    def __init__(self):
        super().__init__() 

    def empilhar(self, item):
        super().empilhar(float(item))

    def verificar(self, item):
        b = self.desempilhar()
        a = self.desempilhar()

        if item == "+":
            resultado = a + b

        elif item == "-":
            resultado = a - b

        elif item == "*":
            resultado = a * b

        elif item == "/":
            resultado = a / b

        self.empilhar(resultado)
        
class conversao(pilha):
    def __init__(self):
        super().__init__() 

    def acrescente(self, item):
        b = self.desempilhar()
        a = self.desempilhar()

        self.empilhar(f"({a} {item} {b})")
    
minha_pilha = hp12c()
minha_pilha2 = conversao()
rpn = input("Digite a expressão RPN: ")
expressao = rpn.split()

for item in expressao:
    if item.isdigit():
        minha_pilha.empilhar(item)
        minha_pilha2.empilhar(item)
    else:
        minha_pilha.verificar(item)
        minha_pilha2.acrescente(item)
    print(*minha_pilha.pilha)
        
print(*minha_pilha2.pilha)

print(f"O resultado da expressão algébrica é: {minha_pilha.pilha[0]:.0f}")







