from conexao import conectar
from datetime import datetime

def cadastrar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    setor = input("Digite o setor do usuário: ")
    cargo = input("Digite o cargo do usuário: (ADMIN ou USUARIO)").upper()
    status = "ATIVO"
    data_criacao = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    try:
        if cargo not in ["ADMIN", "USUARIO"]:
            print("Cargo invalido! somente ADMIN ou USUARIO")
            conexao.close()
            return
        
        cursor.execute("""
    INSERT INTO usuario
    (nome, email, senha, setor, cargo, status, data_criacao)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", (nome, email, senha, setor, cargo, status, data_criacao))
        conexao.commit()

        print("Usuario cadastrado com sucesso!")

    except Exception as erro:
        print(f"Erro ao cadastrar usuario:{erro}")
    
    finally:
        conexao.close()