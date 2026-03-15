from conexao import conectar

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
        cursor.execute("""SELECT id_produto,nome,categoria,local FROM produto""")

       
        produtos = cursor.fetchall()

        for produto in produtos:
            print(produto)
    
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