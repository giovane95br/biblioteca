livraria = []

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input(f"Digite o Nome do autor de ({titulo}): ")
    copias = int(input("Digite a quantidade de cópias disponíveis: "))
    livraria.append({"titulo": titulo, "autor": autor, "copias": copias})
    print(f"\nLivro '{titulo}' adicionado com sucesso!\n")

def listar_livros():
    if livraria:
        for livro in livraria:
            print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Cópias: {livro['copias']}\n")
    else:
        print("\nNenhum livro disponível!\n")

def pegar_emprestado():
    titulo = input("\nDigite o título do livro que deseja pegar emprestado: ")
    for livro in livraria:
        if livro['titulo'].lower() == titulo.lower():
            if livro['copias'] > 0:
                livro['copias'] -= 1
                print(f"\nVocê pegou o livro ({livro['titulo']}) emprestado!") 
                print(f"Cópias restantes de {titulo}: {livro['copias']}\n")
                return
            else:
                print("\nNão há cópias disponíveis!")
                return
    print("\nLivro não encontrado!")

def devolver_livro():
    titulo = input("\nQual livro você gostaria de devolver: ")
    for livro in livraria:
        if livro['titulo'].lower() == titulo.lower():
            livro['copias'] += 1
            print(f"\nVocê devolveu o livro '{livro['titulo']}'! Cópias restantes: {livro['copias']}\n")
            return
    print("\nLivro não encontrado!")

def biblioteca():
    while True:
        print("[1] Adicionar Livros")
        print("[2] Listar Livros")
        print("[3] Pegar Emprestado")
        print("[4] Devolver Livro")
        print("[5] Sair\n")
        
        opcao = input("O que deseja fazer: ")
        if opcao == '1': adicionar_livro()
        elif opcao == '2': listar_livros()
        elif opcao == '3': pegar_emprestado()
        elif opcao == '4': devolver_livro()
        elif opcao == '5': 
            print("\nAté a proxima!")
            break
        else: print("\nOpção inválida!")

# Inicia o programa
biblioteca()
