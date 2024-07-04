# Aqui a  biblioteca é definida como um dicionário global
biblioteca = {}

def validar_titulo(titulo):
    # Nesta parte valida-se  se o título do livro é uma string não vazia.
    if not titulo or not titulo.strip():
        print("Título inválido.Digite um título válido.")
        return False
    return True

def validar_campo(campo):
    # Valida se o campo de atualização é válido.
    campos_validos = ("autor", "ano_publicacao", "disponivel")
    if campo not in campos_validos:
        print(f"Campo inválido: {campo}. Digite um campo válido entre {campos_validos}.")
        return False
    return True

def menu_principal():
    # Nesta função apresenta o menu principal e o mesmo interage com o usuário.
    while True:
        print("""
              ○Gerenciamento de Biblioteca○

              1. Adicionar livro
              2. Atualizar livro
              3. Remover livro
              4. Consultar disponibilidade
              5. Sair e fechar o menu

              ☞ Digite sua opção: """)

        opcao = input()

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            atualizar_livro()
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            consultar_disponibilidade()
        elif opcao == "5":
            print("Obrigado por usar nosso Gerenciamento de Biblioteca ;) ")
            break
        else:
            print("Opção inválida.Digite um numeral entre 1 e 5.")

def adicionar_livro():
    # Adicionar um novo livro na biblioteca.
    while True:
        titulo = input("Digite aqui o título do livro: ")
        if validar_titulo(titulo):
            break

    autor = input("Digite aqui o autor do livro: ")
    ano_publicacao = input("Se possível,digite o ano de publicação: ")

    novo_livro = {
        "autor": autor,
        "ano_publicacao": ano_publicacao,
        "disponivel": True
    }

    biblioteca[titulo] = novo_livro
    print(f"O livro '{titulo}' foi adicionado com sucesso! :) ")

def atualizar_livro():
    # Atualizar as informações de um livro existente.
    while True:
        titulo = input("Digite aqui o título do livro: ")
        if validar_titulo(titulo) and titulo in biblioteca:
            break
        else:
            print(" O livro solicitado não foi  encontrado.Digite um título existente.")

    while True:
        campo = input("Digite o campo que deseja ser atualizado (autor, ano de publicação, disponivel ): ")
        if validar_campo(campo):
            break

    novo_valor = input(f"Digite aqui o novo valor para {campo}: ")

    # Converte 'disponivel' para boolean se for o campo atualizado
    if campo == "disponivel":
        novo_valor = novo_valor.lower() in ["sim", "true", "1"]

    biblioteca[titulo][campo] = novo_valor
    print(f"O campo '{campo}' do livro '{titulo}' foi atualizado com sucesso! :)")

def remover_livro():
    # Função para remover um livro da biblioteca.
    while True:
        titulo = input("Digite aqui o título do livro: ")
        if validar_titulo(titulo) and titulo in biblioteca:
            break
        else:
            print("O livro solicitado não foi encontrado.Digite um título existente.")

    del biblioteca[titulo]
    print(f"O livro '{titulo}' foi removido com sucesso!")

def consultar_disponibilidade():
    # Consultar a disponibilidade de um livro.
    while True:
        titulo = input("Digite aqui o título do livro: ")
        if validar_titulo(titulo) and titulo in biblioteca:
            break
        else:
            print("O livro solicitado não foi encontrado.Digite um título existente.")

    livro = biblioteca[titulo]
    disponivel = livro["disponivel"]

    if disponivel:
        print(f"O livro '{titulo}' está disponível para empréstimo.")
    else:
        print(f"O livro '{titulo}' está emprestado.")

# Inicia o menu principal
menu_principal()