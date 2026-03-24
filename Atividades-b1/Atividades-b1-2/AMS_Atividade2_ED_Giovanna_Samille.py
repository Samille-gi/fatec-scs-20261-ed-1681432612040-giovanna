
"""
--------------------------------------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Exemplo de Manipulação de Lista ligada                                                                             *
* *
* Autor: 1681432612040 - nome: Giovanna Samille Gonçalves da silva                                 *
* Objetivo: Mostrar manipulação de lista ligada em python                                                                                  *
* data: 09/03/2026                                                                           *
---------------------------------------------------------------------------------------------
"""

# Banco de dados em memoria (Dicionario)
# Nó: {"valor": dado, "proximo": None}

produtos = {}
def valorExite(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual ["valor"] == valorEntrada:
            return True
        atual = atual ["proximo"]
    return False

# funcao de Inclusao
def inserirInicio(listaEntrada):
    print("\n ---- Inserir um valor no início ----")
    valor = input("Digite o valor: ")
    if (valorExite(listaEntrada, valor)):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": listaEntrada}
    return novoNo
    
    
    
# funcao de Inclusao no Fim
def inserirFim(listaEntrada):
    print("\n ---- Inserir um valor no final ----")
    valor = input("Digite o valor: ")

    if (valorExite(listaEntrada, valor)):
        print("Codigo de produto Duplicado")
        return listaEntrada
    
    atual = listaEntrada
    while atual is not None:
        if atual["proximo"] == None:
            novoNo = {"valor": valor, "proximo": None}
            atual["proximo"] = novoNo
            return listaEntrada
        atual = atual["proximo"]
    


# funcao de Inclusao no Meio
def inserirMeio(listaEntrada):
    print("\n ---- Inserir um valor após o outro----")
    valor_base = input("Número de base para o valor ser adicionado depois: ")
    
    if not (valorExite(listaEntrada, valor_base)):
        print("Valor invalido")
        return listaEntrada
    
    valor = input("Digite o valor: ")

    if (valorExite(listaEntrada, valor)):
        print("Codigo de produto Duplicado")
        return listaEntrada
    
    atual = listaEntrada
    while atual is not None:
        if atual["valor"] == valor_base:
            novoNo = {"valor": valor, "proximo": atual["proximo"]}
            atual["proximo"] = novoNo
            return listaEntrada
        atual = atual["proximo"]

# funcao de Lista
def listar(listaRecebida):
    print("\n ---- Exibir Lista ----")
    if listaRecebida is None:
        print("Lista vazia")
        return
    listaAtual = listaRecebida
    while listaAtual is not None:
        print (listaAtual["valor"], end="->" )
        listaAtual = listaAtual["proximo"]

# funcao de consulta
def buscar(listaRecebida):
    print("\n ---- Buscar nó ----")
    argumentoPesquisa = input("informe o argumento de pesquisa:")

    listaAtual = listaRecebida
    posicao = 1

    while listaAtual is not None:
        if listaAtual["valor"]==argumentoPesquisa:
            break
        listaAtual = listaAtual["proximo"]
        posicao +=1
        
    if listaAtual is None:
        print("Valor não encontrado")
    else:
        print(f"valor encontrado na posição {posicao}")

# funcao de Exclusao
def remover(listaEntrada):
    print("\n ---- Remover nó ----")
    valor = input("Digite o valor: ")

    if (valorExite(listaEntrada, valor)):
        atual = listaEntrada
        while atual is not None:
            if atual["proximo"]["valor"] == valor:
             # verifica se o próximo é o valor procurado
                atual["proximo"] = atual["proximo"]["proximo"]
                return listaEntrada
            atual = atual["proximo"] 

    else:
        print("Valor não existe")

# Exemplo de Menu de Interacao
def menu():
    lista = None
    while True:
        print("\n ---- Menu ----")
        print("1- Inserir no Início \n2- inserir no Fim \n3- Inserir no meio \n4- listar \n5- remover\n6- Buscar \n0- Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista = inserirInicio(lista)

        elif opcao == '2':
            lista = inserirFim(lista)
        elif opcao == '3':
            lista = inserirMeio(lista)
        elif opcao == '4':
            listar(lista)
        elif opcao == '5':
            lista = remover(lista)
        elif opcao == '6':
            buscar(lista)
        elif opcao == '0':
            print ("Obrigado por usar o sistema")
            break
        else:
            print ("**Opcao invalida**")

print ("**Bem-vindo ao programa**")
menu()