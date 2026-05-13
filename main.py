from produto import listar_produtos, atualizar_produto, deletar_produto, cadastrar_produto, buscar_por_nome,estoque_minimo,entrada_estoque,saida_estoque
from  movimentacao import listar_movimentacoes  
from usuario import cadastrar_usuario

def mostrar_menu():
    print("\n"+"*" * 5 + "MENU AlMOXARIFADO"+ "*" * 5)
   

   
    print("1 - Listar produtos")
    print("2 - Buscar Produto")
    print("3 - Entrada estoque")
    print("4 - Saída estoque")
    print("5 - Movimentações")
    print("6 - Cadastrar produto")
    print("7 - Atualizar produto")
    print("8 - Deletar produto")
    print("9 - Estoque mínimo")
    print("10 - Cadastrar usuário")

    print("[SAIR]")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        # 1 - LISTAR PRODUTOS
        if opcao == "1":
            print("\nLISTAR PRODUTOS")
            print("-" * 35)
            listar_produtos()

        # 2 - BUSCAR PRODUTO
        elif opcao == "2":
            print("\nBUSCAR PRODUTO")
            print("-" * 35)
            nome = input("Nome do produto: ")
            buscar_por_nome(nome)

        # 3 - ENTRADA ESTOQUE
        elif opcao == "3":
            print("\nENTRADA DE ESTOQUE")
            print("-" * 35)

            id_produto = input("ID do produto: ")
            qtd = int(input("Quantidade de entrada: "))
            user = input("Usuário: ")
            obs = input("Observação: ")

            entrada_estoque(id_produto, qtd, user, obs)

        # 4 - SAÍDA ESTOQUE
        elif opcao == "4":
            print("\nSAÍDA DE ESTOQUE")
            print("-" * 35)

            id_produto = input("ID do produto: ")
            qtd = int(input("Quantidade de saída: "))
            user = input("Usuário: ")
            obs = input("Observação: ")

            saida_estoque(id_produto, qtd, user, obs)

        # 5 - HISTÓRICO
        elif opcao == "5":
            print("\nHISTÓRICO DE MOVIMENTAÇÕES")
            print("-" * 35)
            listar_movimentacoes()

        # 6 - CADASTRAR PRODUTO
        elif opcao == "6":
            print("\nCADASTRAR PRODUTO")
            print("-" * 35)

            nome = input("Nome: ")
            qtd = int(input("Quantidade: "))
            descricao = input("Descrição: ")
            categoria = input("Categoria: ")
            qtd_minima = int(input("Quantidade mínima: "))
            local = input("Local: ")

            cadastrar_produto(nome, qtd, descricao, categoria, qtd_minima, local)

        # 7 - ATUALIZAR PRODUTO
        elif opcao == "7":
            print("\nATUALIZAR PRODUTO")
            print("-" * 35)

            id_produto = int(input("ID do produto: "))
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            categoria = input("Categoria: ")
            qtd_minima = int(input("Quantidade mínima: "))
            status = input("Status: ")
            local = input("Local: ")

            atualizar_produto(id_produto,nome,descricao,categoria,qtd_minima,status,local)

        # 8 - DELETAR PRODUTO
        elif opcao == "8":
            print("\nDELETAR PRODUTO")
            print("-" * 35)

            id_produto = int(input("ID do produto: "))
            deletar_produto(id_produto)

        # 9 - ESTOQUE MÍNIMO
        elif opcao == "9":
            print("\nESTOQUE MÍNIMO")
            print("-" * 35)
            estoque_minimo()

        # 10 - CADASTRAR USUÁRIO
        elif opcao == "10":
            print("\nCADASTRAR USUÁRIO")
            print("-" * 35)
            cadastrar_usuario()

        # 0 - SAIR
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()