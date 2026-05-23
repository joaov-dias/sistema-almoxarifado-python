from conexao import conectar
from datetime import datetime

def registrar_movimentacao(cursor,id_produto, id_usuario, qtd, tipo_movimentacao, obs):

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute("""
        INSERT INTO movimentacao (id_produto, id_usuario, data_hora, qtd_movi, tipo_movi, obs) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, (id_produto, id_usuario, data_hora, qtd, tipo_movimentacao, obs))

    except Exception as erro:
        print("Erro ao registrar movimentação: ", erro)


def listar_movimentacoes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT 
        produto.nome,
        movimentacao.id_usuario,
        movimentacao.tipo_movi,
        movimentacao.qtd_movi,
        movimentacao.data_hora
        FROM movimentacao
        JOIN produto 
        ON 
        movimentacao.id_produto = produto.id_produto
        ORDER BY movimentacao.data_hora DESC
        """)

        movimentacoes = cursor.fetchall()
        

        for movi in movimentacoes:      
            print(f"Produto: {movi[0]}")
            print(f"Usuário: {movi[1]}")
            print(f"Tipo de movimentação: {movi[2]}")
            print(f"Quantidade movimentada: {movi[3]}")
            print(f"Data e hora: {movi[4]}")
            print("-" * 20)

    except Exception as erro:
        print("Erro ao listar movimentações: ", erro)

    
