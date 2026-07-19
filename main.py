from produto import listar_produtos, atualizar_produto, deletar_produto, cadastrar_produto, buscar_por_nome,estoque_minimo,entrada_estoque,saida_estoque
from  movimentacao import listar_movimentacoes  
from usuario import cadastrar_usuario,login,listar_usuario,buscar_usuario,atualizar_usuario,alterar_status_usuario, alterar_senha,verificar_permissao
from datetime import datetime
from relatorio import menu_relatorio

def mostrar_menu(nome, cargo):
    print("\n"+"-" * 5 + "MENU AlMOXARIFADO"+ "-" * 5)

    print(f"Usuario logado: {nome}!")
    print(f"Cargo: {cargo}")
    print(f"Data de acesso: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    print("-" * 40)

    print("1 - Listar produtos")
    print("2 - Buscar Produto")
    print("3 - Entrada estoque")
    print("4 - Saída estoque")
    print("5 - Alterar senha usuário")

    
    if cargo == "ADMIN":
        print("-" * 3 + "ADMINISTRADOR" + "-" * 3)
        print("6 - Cadastrar produto")
        print("7 - Atualizar produto")
        print("8 - Deletar produto")
        print("9 - Cadastrar usuário")
        print("10 - Listar usuários")
        print("11 - Buscar usuario por email")
        print("12 - Atualizar usuario")
        print("13 - Alterar status usuario")
        print("14 - Relatorios")

    print("0 - Sair")

def mostrar_titulo(titulo):
    print(f"\n{titulo}")
    print("-" * 35)

def main():
    usuario_logado = login()
    if not usuario_logado:
        print("Falha no login! Encerrando o sistema...")
        return
    

    while True:
        mostrar_menu(usuario_logado["nome"], usuario_logado["cargo"])
        opcao = input("Escolha uma opção: ")

        #MENU COMUM INDEPENDENTE DO CARGO
        # 1 - LISTAR PRODUTOS
        if opcao == "1":
            mostrar_titulo("LISTAR PRODUTOS")
            listar_produtos()

        # 2 - BUSCAR PRODUTO
        elif opcao == "2":
            mostrar_titulo("BUSCAR PRODUTO")
            buscar_por_nome()

        # 3 - ENTRADA ESTOQUE
        elif opcao == "3":
            mostrar_titulo("ENTRADA DE ESTOQUE")
            entrada_estoque(usuario_logado["id_usuario"])

        # 4 - SAÍDA ESTOQUE
        elif opcao == "4":
            mostrar_titulo("SAÍDA DE ESTOQUE")
            saida_estoque(usuario_logado["id_usuario"])


        #5- ALTERAR SENHA USUÁRIO
        elif opcao == "5":
            mostrar_titulo("ALTERAR SENHA USUÁRIO")
            alterar_senha(usuario_logado)

        #MENU RESTRITO PARA ADMINISTRADOR
        # 6 - CADASTRAR PRODUTO
        elif opcao == "6":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            mostrar_titulo("CADASTRAR PRODUTO")
            cadastrar_produto(usuario_logado)

        # 7 - ATUALIZAR PRODUTO
        elif opcao == "7":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            mostrar_titulo("ATUALIZAR PRODUTO")
            atualizar_produto(usuario_logado)

        # 8 - DELETAR PRODUTO
        elif opcao == "8":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            mostrar_titulo("DELETAR PRODUTO")
            deletar_produto(usuario_logado)

        
        # 9 - CADASTRAR USUÁRIO
        elif opcao == "9":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            mostrar_titulo("CADASTRAR USUÁRIO")
            cadastrar_usuario(usuario_logado)

        # 10 - LISTAR USUÁRIOS
        elif opcao == "10":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            listar_usuario()

        # 11 - BUSCAR USUARIOS POR EMAIL
        elif opcao == "11":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            buscar_usuario()

        #12 - ATUALIZAR USUARIO
        elif opcao == "12":  
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            atualizar_usuario(usuario_logado)

        #13 - ALTERAR STATUS USUÁRIO
        elif opcao == "13":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            alterar_status_usuario(usuario_logado)

        #14 - MENU RELATORIO
        elif opcao == "14":
            if not verificar_permissao(usuario_logado,["ADMIN"]):
                continue
            menu_relatorio()

        # 0 - SAIR
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")
            
if __name__ == "__main__":
    main()