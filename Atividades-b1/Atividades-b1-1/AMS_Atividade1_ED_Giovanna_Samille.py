# Estrutura Global: Dicionario de Dicionarios

"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B1-1                                                                             *
* *
* Autor: 1681432612040 - nome: Giovanna Samille Gonçalves da silva                             *
* Objetivo: É criar um sistema de catálogo de filmes usando dicionários em Python,           *
permitindo adicionar, buscar, remover e listar filmes.                                       *
* data: 24/02/2026                                                                           *
---------------------------------------------------------------------------------------------
"""

catalogo = {}

def adicionar_filme(): # variáveis id_filme, titulo, diretor

    print("\n--- Adicionar de Filmes ---")

    id_filme = input("Digite o id do filme: ")

    if id_filme in catalogo:
        print ("ID invalido")
    else: 
        titulo = input("Digite o título do filme: ")
        diretor = input("Digite o diretor do filme: ")
        catalogo[id_filme] = {
        "titulo": titulo,
        "diretor": diretor
    }
        print("Filme adicionado")


def buscar_filme(): # variável id_filme

    print("\n--- Consultar Filmes ---")
    id_filme = input("Digite o id para ocorrer a busca do filme: ")
    filme = catalogo.get(id_filme)
    if filme:
        print (filme)
    else: 
        print("Filme não encontrado")

def remover_filme(): # variável id_filme

    print("\n--- Remover Filmes ---")
    id_filme = input("Digite o id para o filme ser removido: ")
    if id_filme in catalogo :
        filme_removido = catalogo.pop(id_filme, None)
        print(f"Filme removido: {filme_removido}")
    else: 
        print("ID não encontrado")


def listar_todos():

    if not catalogo:
        print("\nO catalogo esta vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Titulo: {dados['titulo']} "
                  f"| Diretor: {dados['diretor']}")

# --- Testes de Funcionamento ---

def Menu():
    while True:
        print("\n------------ Menu ------------")
        print("1 - Adicionar filmes")
        print("2 - Buscar filmes")
        print("3 - Remover filmes")
        print("4 - Listar filmes do catalogo")
        print("5 - Sair")
        print("--------------------------------")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            adicionar_filme()
        elif opcao == "2":
            buscar_filme()
        elif opcao == "3":
            remover_filme()
        elif opcao == "4":
            listar_todos()
        elif opcao == "5":
            break
        else:
            print("Opção Inválida")


Menu()