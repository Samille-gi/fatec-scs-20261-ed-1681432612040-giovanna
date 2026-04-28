"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B2-2                                                                             *
* *
* Autor: 1681432612040 - nome: Giovanna Samille Gonçalves da silva                             *
* Objetivo: Gerenciar uma fila de impressão, separando documentos de ADM e alunos, com prioridade para ADM.*                                      *
* data: 28/04/2026                                                                           *
---------------------------------------------------------------------------------------------
"""

fila1 = []
fila2 = []
fila_geral = []

def adicionar_fila():
    print("\n--- Adicionar Fila ---")
    nome_arquivo = input("Nome do Arquivo: ")
    total_paginas = input("Quantidade total de páginas: ")
    
    doc = {
        "nome" : nome_arquivo,
        "paginas": total_paginas
    }
    while True:
        tipo = input("Tipo (adm/aluno): ").lower()
        if tipo == "adm":
            fila1.append(doc)
            break
        elif tipo == "aluno":
            fila2.append(doc)
            break
        else:
            print("Tipo inválido")
            
def consumir_fila():
    print("\n--- Consumir Fila ---")
    if fila_geral:
        doc = fila_geral.pop(0)
        print(f"Imprimindo documento 1: {doc['nome']} ({doc['paginas']} páginas)")
    else:
        print("Fila geral vazia.")
        
def listar():
    print("\n--- Listagem das Filas ---")
    print("\n--- Fila ADM ---")
    if not fila1:
        print("Fila de ADM está vazia.")
    else:
        count = 1
        for p in fila1:
            print(f"Documento {count}: {p['nome']} ({p['paginas']} páginas)")
            count +=1
        
    print("\n--- Fila Aluno ---")
    if not fila2:
        print("Fila de Aluno está vazia.")
    else:
        count2 = 1
        for p in fila2:
            print(f"Documento {count2}: {p['nome']} ({p['paginas']} páginas)")
            count2 +=1
    
    print("\n--- Fila Geral ---")
    if not fila_geral:
        print("Fila Geral está vazia.")
    else:
        count3 = 1
        for p in fila_geral:
            print(f"Documento {count3}: {p['nome']} ({p['paginas']} páginas)")
            count3 +=1
        
def reorganizar():
    print("\n--- Reorganizar Filas ---")
    if not fila_geral:
        fila_geral.extend(fila1)
        fila_geral.extend(fila2)
        
        fila1.clear()
        fila2.clear()
        
        print("Filas foram reorganizadas na fila geral")

    else:
        print("A fila geral possui itens")
def mostrar():
    while True:
        print("\n----- Menu -----")
        print("1 - Adicionar Fila")
        print("2 - Consumir Fila")
        print("3 - Listar as três filas")
        print("4 - Reorganizar fila")
        print("5 - Sair")

        opcao = input("Opção desejada: ")
        
        if opcao == "1":
            adicionar_fila()
        elif opcao == "2":
            consumir_fila()
        elif opcao == "3":
            listar()
        elif opcao == "4":
            reorganizar()
        elif opcao == "5":
            break
    
mostrar()
    
