from conexao import conectar
from datetime import datetime

def registrar_movimentacao(id_produto, id_usuario, qtd, tipo_movimentacao, obs):
    conexao = conectar()
    cursor =  conexao.cursor()

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute("""
        INSERT INTO movimentacao (id_produto, id_usuario, data_hora, qtd_movi, tipo_movi, obs) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, (id_produto, id_usuario, data_hora, qtd, tipo_movimentacao, obs))

        conexao.commit()
    except Exception as erro:
        print("Erro ao registrar movimentação: ", erro)

    finally:
        conexao.close()