from conexao import conectar

def registrar_log(id_usuario,acao,descricao):
    conexao = conectar()

    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO logs (id_usuario,acao,descricao) VALUES (?,?,?) ",(id_usuario, acao, descricao))
        conexao.commit()
    
    except Exception as erro:
        print(f"Erro: {erro}")
    
    finally:
        conexao.close