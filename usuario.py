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
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        if cargo not in ["ADMIN", "USUARIO"]:
            print("Cargo invalido! somente ADMIN ou USUARIO")
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

def login ():
    conexao = conectar()
    cursor = conexao.cursor()

    email = input("Digite seu Email:")
    senha =  input("Digite sua senha:")

    try:
        cursor.execute("""
                  SELECT id_usuario,nome, email,cargo,status FROM usuario WHERE email=? AND senha=?
                       """,(email,senha))
        

        usuario = cursor.fetchone()

        if usuario:
            if usuario[4] == "ATIVO":
                print(f"\nBem vindo,{usuario[1]}!")
                print(f"Cargo:{usuario[3]}")
                print(f"Login realizado com sucesso!")

                return{
                "id_usuario":usuario[0],
                    "nome":usuario[1],
                "email":usuario[2],
                "cargo":usuario[3],
                "status":usuario[4],}
            else:
                print("Usuario inativo, procure um Administrador!")
                return None
        else:
                print("Email ou senha errado!")
                return None
        
    except Exception as erro:
        print(f"Erro ao fazer login: {erro}")
        return None


    finally:
        conexao.close()
            

