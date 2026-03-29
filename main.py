from produto import listar_produtos, atualizar_produto, deletar_produto, cadastrar_produto, buscar_por_nome,estoque_minimo


def mostrar_menu():
    print("\n===== MENU ALMOXARIFADO =====")
    print("1 - Listar produtos")
    print("2 - Atualizar produto")
    print("3 - Cadastrar produto")
    print("4 - Deletar produto")
    print("5 - Buscar por nome")
    print("6 - Estoque mínimo")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        # LISTAR PRODUTOS
        if opcao == "1":
            listar_produtos()

        # ATUALIZAR PRODUTO
        elif opcao == "2":

            while True:
                try:
                    id_produto = int(input("Id do produto: "))
                    break
                except ValueError:
                    print("Digite um número válido")

            nome = input("Nome: ")
            descricao = input("Descrição: ")
            categoria = input("Categoria: ")

            while True:
                try:
                    qtd_minima = int(input("Quantidade mínima: "))
                    break
                except ValueError:
                    print("Digite um número válido")

            status = input("Status: ")
            local = input("Local: ")

            atualizar_produto(id_produto, nome, descricao, categoria, qtd_minima, status, local)

        # CADASTRAR PRODUTO
        elif opcao == "3":

            nome = input("Nome: ")

            while True:
                try:
                    qtd = int(input("Quantidade: "))
                    break
                except ValueError:
                    print("Digite um número válido")

            descricao = input("Descrição: ")
            categoria = input("Categoria: ")

            while True:
                try:
                    qtd_minima = int(input("Quantidade mínima: "))
                    break
                except ValueError:
                    print("Digite um número válido")

            
            local = input("Local: ")

            cadastrar_produto(nome, qtd, descricao, categoria, qtd_minima, local)

        # DELETAR PRODUTO
        elif opcao == "4":

            while True:
                try:
                    id_produto = int(input("Id do produto: "))
                    break
                except ValueError:
                    print("Digite um número válido")

            deletar_produto(id_produto)

        # BUSCAR POR NOME
        elif opcao == "5":

            nome= input("Nome do produto:")
            buscar_por_nome(nome)

        # ESTOQUE MÍNIMO
        elif opcao == "6":
            estoque_minimo()
        # SAIR
        elif opcao == "0":
            print("Saindo...")
            break

        # OPÇÃO INVÁLIDA
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()