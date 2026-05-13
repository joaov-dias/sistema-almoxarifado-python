from conexao import conectar
from movimentacao import registrar_movimentacao

def cadastrar_produto(nome, qtd, descricao, categoria, qtd_minima, local):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(""" 
        INSERT INTO produto 
        (nome, qtd, descricao, categoria, qtd_minima, data_cadastro, status, local)
        VALUES (?, ?, ?, ?, ?, datetime('now'), ?, ?)
        """,(nome, qtd, descricao, categoria, qtd_minima, 'Ativo', local))

        conexao.commit()
    
        print("Produto cadastrado com sucesso!")

    except Exception as erro:
        print("Produto não cadastrado,", erro)
        
    conexao.close()

def listar_produtos ():

    conexao = conectar()
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

    conexao.close()

def atualizar_produto(id_produto, nome, descricao, categoria, qtd_minima, status, local):

    conexao = conectar()

    cursor = conexao.cursor()


    cursor.execute("SELECT * FROM produto WHERE id_produto = ?",(id_produto,))
    
    produto = cursor.fetchone()

    if produto is None :
        print("Produto não encontrado.")
        conexao.close()

        return
    
    sql = ("""UPDATE produto
           SET nome = ?, descricao = ?, categoria = ?, qtd_minima = ?, "status" = ?, "local" = ? WHERE id_produto = ? """)
    
    cursor.execute(sql,(nome, descricao, categoria, qtd_minima, status, local, id_produto))
    print("Produto atualizado!")

    conexao.commit()
    conexao.close()

def deletar_produto(id_produto):
    conexao =conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produto WHERE id_produto = ?", (id_produto,))

    produto =  cursor.fetchone()

    if produto is None :
        print("Produto não encontrado")
        conexao.close()
        return

    sql = ("DELETE FROM produto WHERE id_produto = ?")

    cursor.execute(sql,(id_produto,))

    print(f'Produto {produto[0]} - {produto[1]}, {produto[3]} deletado com sucesso!')

    conexao.commit()

    conexao.close()

def buscar_por_nome(nome):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """SELECT * FROM produto WHERE nome LIKE ?"""
        
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
                Local: {produto[8]}
                Status: {produto[7]}
                -------------------------
                """)
    else:
            print("Produto não encontrado!")

    conexao.close()

def estoque_minimo():
    conexao = conectar()
     
    cursor = conexao.cursor()

    sql= """
    SELECT id_produto, nome, qtd, qtd_minima FROM produto
    WHERE qtd <= qtd_minima
    """
    cursor.execute(sql)

    produtos = cursor.fetchall()

    conexao.close()

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

def entrada_estoque(id_produto, qtd,id_usuario, obs):
    conexao =  conectar()

    cursor = conexao.cursor()

    if qtd <= 0:
        print("Quantidade Invalida! Deve ser Superior a zero")
        conexao.close()
        return
    
    cursor.execute("SELECT * FROM produto WHERE id_produto = ?",(id_produto,))

    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado!")
        conexao.close()
        return

    nova_quantidade = produto[2] + qtd

    cursor.execute("update produto set qtd = ? where id_produto = ?",(nova_quantidade, id_produto))    
    

    registrar_movimentacao(cursor,id_produto, id_usuario, qtd, "entrada", obs)

    print(f"Entrada de {qtd} unidades do produto {produto[1]} registrada com sucesso!")
    
    conexao.commit()
    
    conexao.close()

def saida_estoque(id_produto, qtd, id_usuario, obs):
    conexao = conectar()

    cursor = conexao.cursor()
    if qtd <= 0:
        print("\n\nQuantidade invalida! Deve ser maio que Zero!")
        conexao.close()
        return

    cursor.execute("SELECT * FROM produto WHERE id_produto = ?", (id_produto,))
    

    produto =  cursor.fetchone()

    if produto is None:
        print("Prouduto não encontrado!")
        conexao.close()
        return

    cursor.execute("UPDATE produto SET qtd = qtd - ? WHERE id_produto = ? AND qtd >= ?", (qtd, id_produto, qtd))

    if cursor.rowcount == 0:
        print("Quantidade insuficiente para saída de estoque!")
        conexao.close()
        return
    
    print(f"Saída de {qtd} unidades do produto {produto[1]} realizada com sucesso!")

    registrar_movimentacao(cursor,id_produto, id_usuario, qtd, "saida", obs)
    print(f"Saída de {qtd} unidades do produto {produto[1]} registrada com sucesso!")

    conexao.commit()
    conexao.close()
