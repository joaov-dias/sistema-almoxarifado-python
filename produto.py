from conexao import conectar
from movimentacao import registrar_movimentacao
from logs import registrar_log
from validacoes import ler_campo_obrigatorio, ler_inteiro


def cadastrar_produto(usuario_logado):
   
    with conectar() as conexao:
        cursor = conexao.cursor()
           
        try:
            nome = ler_campo_obrigatorio("Nome: ")
            qtd = ler_inteiro("Quantidade: ")

            descricao = ler_campo_obrigatorio("Descrição: ")
            categoria = ler_campo_obrigatorio("Categoria: ")
            qtd_minima = ler_inteiro("Quantidade mínima: ")
            local = ler_campo_obrigatorio("Local: ")
            
            cursor.execute(""" 
            INSERT INTO produto 
            (nome, qtd, descricao, categoria, qtd_minima, data_cadastro, status, local)
            VALUES (?, ?, ?, ?, ?, datetime('now'), ?, ?)
            """,(nome, qtd, descricao, categoria, qtd_minima, 'Ativo', local))

            conexao.commit()

            print("Produto cadastrado com sucesso!")
            registrar_log(usuario_logado["id_usuario"],"CADASTRAR_PRODUTO",f"Cadastrou o produto {nome} ")

        except Exception as erro:
            print("Produto não cadastrado,", erro)

def listar_produtos ():

    with conectar() as conexao:
        cursor = conexao.cursor()

        try:
            cursor.execute("""SELECT id_produto,nome,qtd,categoria,local FROM produto""")
            produtos = cursor.fetchall()
            
            for produto in produtos:
                print(f"Id: {produto[0]}")
                print(f"Nome: {produto[1]}")
                print(f"Quantidade: {produto[2]}")
                print(f"Categoria: {produto[3]}")
                print(f"Local: {produto[4]}")
                print("-" * 15)
                
        
        except Exception as erro:

            print("Erro ao mostrar produto,", erro)

    
def atualizar_produto(usuario_logado):

    with conectar() as conexao:
        cursor = conexao.cursor()
        try:
            id_produto = ler_campo_obrigatorio("Id Produto:")
            produto = buscar_produto(cursor,id_produto)
            
            if produto is None :
                            print("Nenhum produto encontrado.")
                            return
            
            nome = input(f"Nome ({produto[1]}): ").strip()
            descricao = input(f"Descrição ({produto[3]}): ").strip()
            categoria = input(f"Categoria ({produto[4]}): ").strip()
            qtd_minima = input(f"Quantidade mínima ({produto[5]}): ").strip()
            status = input(f"Status ({produto[7]}): ").upper()
            local = input(f"Local ({produto[8]}): ").strip()

            if nome == "":
                nome = produto[1]
            if descricao == "":
                descricao = produto[3]
            if categoria == "":
                categoria = produto[4]
            if qtd_minima == "":
                qtd_minima = produto[5]
            elif not qtd_minima.isdigit():
                print("Quantidade mínima Inválida.")
                return
            else:
                qtd_minima = int(qtd_minima)
            if status == "":
                status = produto[7]
            if local == "":
                local = produto[8]

            if status not in("ATIVO","INATIVO"):
                print("Status inválido.")
                return
            
            sql = ("""UPDATE produto
                SET nome = ?, descricao = ?, categoria = ?, qtd_minima = ?, "status" = ?, "local" = ? WHERE id_produto = ? """)
            
            cursor.execute(sql,(nome, descricao, categoria, qtd_minima, status, local, id_produto))
            
            conexao.commit()
            registrar_log(usuario_logado["id_usuario"],"ATUALIZAR_PRODUTO",f"Atualizou o produto {nome} ")
            print("Produto atualizado!")
        
        except Exception as erro:
            print("Erro ao atualizar produto,", erro)

def deletar_produto(usuario_logado):
    with conectar() as conexao:
        cursor = conexao.cursor()

        try:
            id_produto = ler_inteiro("ID do produto: ")

            produto = buscar_produto(cursor,id_produto)

            if produto is None :
                print("Produto não encontrado")
                return

            sql = ("DELETE FROM produto WHERE id_produto = ?")

            cursor.execute(sql,(id_produto,))

            print(f'Produto {produto[0]} - {produto[1]}, {produto[3]} deletado com sucesso!')
            registrar_log(usuario_logado["id_usuario"],"DELETAR_PRODUTO",f"Deletou o produto {produto[1]}(ID: {id_produto}) ")

            conexao.commit()
        except Exception as erro:
            print("Erro ao deletar produto,", erro)

def buscar_por_nome():
    with conectar() as conexao:
        cursor = conexao.cursor()

        try:
            nome = ler_campo_obrigatorio("Nome do produto: ")

            sql = "SELECT id_produto,nome,qtd,descricao,categoria,local,status FROM produto WHERE nome LIKE ?"
                
            cursor.execute(sql,(f"%{nome}%",))

            produtos =  cursor.fetchall()

            if produtos:

                print("\nProdutos encontrados:\n")
                for produto in produtos:
                    print(f"""
                        ID: {produto[0]}
                        Nome: {produto[1]}
                        Quantidade: {produto[2]}
                        Descrição: {produto[3]}
                        Categoria: {produto[4]}
                        Local: {produto[5]}
                        Status: {produto[6]}
                        -------------------------
                        """)
            else:
                    print("Produto não encontrado!")
        
        except Exception as erro:
            print("Erro ao buscar produto,", erro)

def estoque_minimo():
        with conectar() as conexao:
            cursor = conexao.cursor()

            sql= """
            SELECT id_produto, nome, qtd, qtd_minima FROM produto
            WHERE qtd <= qtd_minima
            """
            cursor.execute(sql)

            produtos = cursor.fetchall()

            if not produtos:
                print("Nenhum produto com baixo estoque!")
                return
            print("Produtos com baixo estoque:\n")
            print("-" * 15 )

            for produto in produtos:
                print(f"Id: {produto[0]}")
                print(f"Nome: {produto[1]}")
                print(f"Quantidade: {produto[2]}")
                print(f"Minimo: {produto[3]}")
                print("-" * 15)

def entrada_estoque(user):
    with conectar() as conexao:
        cursor = conexao.cursor()
        try:
            id_produto = ler_inteiro("ID do produto: ")
            qtd = ler_inteiro("Quantidade de entrada: ")
            id_usuario = user
            obs = ler_campo_obrigatorio("Observação: ")

            produto = buscar_produto(cursor,id_produto)

            if produto is None:
                print("Produto não encontrado!")
                return

            nova_quantidade = produto[2] + qtd

            cursor.execute("UPDATE produto SET qtd = ? WHERE id_produto = ?",(nova_quantidade, id_produto))    
            
            registrar_movimentacao(cursor,id_produto, id_usuario, qtd, "entrada", obs)

            print(f"Entrada de {qtd} unidades do produto {produto[1]} registrada com sucesso!")
            
            conexao.commit()

        except Exception as erro:
            print("Erro ao realizar entrada de estoque,", erro)


def saida_estoque(user):
    with conectar() as conexao:
        cursor = conexao.cursor()

        try:
            id_produto = ler_inteiro("ID do produto: ")
            qtd = ler_inteiro("Quantidade de saída: ")
            obs = ler_campo_obrigatorio("Observação: ")

            produto =  buscar_produto(cursor,id_produto)

            if produto is None:
                print("Produto não encontrado!")
                return

            cursor.execute("UPDATE produto SET qtd = qtd - ? WHERE id_produto = ? AND qtd >= ?", (qtd, id_produto, qtd))

            if cursor.rowcount == 0:
                print("Quantidade insuficiente para saída de estoque!")
                return
            
            print(f"Saída de {qtd} unidades do produto {produto[1]} realizada com sucesso!")

            registrar_movimentacao(cursor,id_produto, user, qtd, "saida", obs)
            print(f"Saída de {qtd} unidades do produto {produto[1]} registrada com sucesso!")

            conexao.commit()
            
        except Exception as erro:
            print("Erro ao realizar saída de estoque,", erro)

def buscar_produto(cursor,id_produto):
    cursor.execute("SELECT * FROM produto WHERE id_produto = ?",(id_produto,))

    return cursor.fetchone