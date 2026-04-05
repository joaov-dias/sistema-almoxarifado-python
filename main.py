from produto import listar_produtos, atualizar_produto, deletar_produto, cadastrar_produto, buscar_por_nome,estoque_minimo,entrada_estoque,saida_estoque


def mostrar_menu():
    print("\n===== MENU ALMOXARIFADO =====")
    print("1 - Listar produtos")
    print("2 - Atualizar produto")
    print("3 - Cadastrar produto")
    print("4 - Deletar produto")
    print("5 - Buscar por nome")
    print("6 - Estoque mínimo")
    print("7 - Entrada estoque")
    print("8 - Saida Estoque")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        # LISTAR PRODUTOS
        if opcao == "1":
            print("LISTAR PRODUTOS")
            listar_produtos()

        # ATUALIZAR PRODUTO
        elif opcao == "2":
            print("ATUALIZAR PRODUTO")
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
            print("CADASTRAR PRODUTO")
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
            print("DELETAR PRODUTO")
            while True:
                try:
                    id_produto = int(input("Id do produto: "))
                    break
                except ValueError:
                    print("Digite um número válido")

            deletar_produto(id_produto)

        # BUSCAR POR NOME
        elif opcao == "5":
            print("BUSCAR POR NOME")
            nome= input("Nome do produto:")
            buscar_por_nome(nome)

        # ESTOQUE MÍNIMO
        elif opcao == "6":
            print("ESTOQUE MÍNIMO")
            estoque_minimo()

        #ENTRADA DE PRODUTOS
        elif opcao == "7":
            print("ENTRADA DE PRODUTO")
            id_produto = input("ID do produto: ")
            qtd = int(input("Quantidade de entrada de produto: "))
            entrada_estoque(id_produto,qtd)
       
        # SAIR DE PRODUTOS
        elif opcao == "8":
            print("SAÍDA DE PRODUTO")
            id_produto = input("ID do produto: ")
            qtd = int(input("Quantidade de saída de produto: "))
            saida_estoque(id_produto,qtd)


        elif opcao == "0":
            print("Saindo...")
            break
        
        # OPÇÃO INVÁLIDA
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()