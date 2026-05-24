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
        
        cursor.execute("""INSERT INTO usuario (nome, email, senha, setor, cargo, status, data_criacao)
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (nome, email, senha, setor, cargo, status, data_criacao))
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
        cursor.execute("SELECT id_usuario,nome, email,cargo,status FROM usuario WHERE email=? AND senha=?",(email,senha))
        
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

def listar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_usuario, nome, email, cargo, setor, status, data_criacao FROM usuario ORDER BY status, nome")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuario encontrado!")
    else:
        print("\nLISTA DE USUARIOS")
        print("-" * 30)
        for usuario in usuarios:
            print(f"\nID: {usuario[0]}")
            print(f"Nome: {usuario[1]}")
            print(f"Email: {usuario[2]}")
            print(f"Cargo: {usuario[3]}")
            print(f"Setor: {usuario[4]}")
            print(f"Status: {usuario[5]}")
            print(f"Data de Criação: {usuario[6]}")
            print("-" * 30)

    conexao.close()

def buscar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    email = input("Email do usuario:").strip()

    try:
        sql = "SELECT id_usuario, nome,email, setor,cargo,status,data_criacao FROM usuario WHERE email LIKE ?"
        cursor.execute(sql,(f"%{email}%",))
        usuarios=cursor.fetchall()
        
        if not usuarios:
            print("Nenhum usuario encontrado!")
        else:
            print("\n-----USUARIOS ENCONTRADOS-----")
            for usuario in usuarios:
                print(f"\nID Usuario: {usuario[0]}")
                print(f"Nome: {usuario[1]}")
                print(f"Email: {usuario[2]}")
                print(f"Setor: {usuario[3]}")
                print(f"Cargo: {usuario[4]}")
                print(f"Status: {usuario[5]}")         
                print(f"Data de Criação: {usuario[6]}")
                print("-" * 30)

    except Exception as erro:
        print(f"Erro: {erro}")
    
    finally:
        conexao.close()

def atualizar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    id_user = input("ID usuario:").strip()
    if not id_user.isdigit():
        print("ID invalido! Digite um numero.")
        conexao.close()
        return
    id_user = int(id_user)
    
    try:
        sql_consulta = """SELECT nome, email, cargo, setor FROM usuario WHERE id_usuario = ? """

        cursor.execute(sql_consulta,(id_user,))

        consulta=cursor.fetchone()

        if consulta:
            print("-----USUARIO ENCONTRADO-----")
            print(f"ID usuario: {id_user}")
            print(f"Nome: {consulta[0]}")
            print(f"Email: {consulta[1]}")
            print(f"Cargo: {consulta[2]}")
            print(f"Setor: {consulta[3]}")

            print("Se desejar manter alguma informação, é só apertar ENTER.")
            nome =input("NOME: ").upper()
            email =input("EMAIL: ")
            cargo =input("CARGO: ADMIN/USUARIO ").strip().upper()
            setor =input("SETOR: ")

            if nome == "":
                nome = consulta[0]

            if email == "":
                email = consulta[1]

            if cargo == "":
                cargo = consulta[2]
                
            elif cargo not in ["ADMIN", "USUARIO"]:
                    print("Cargo inválido! Somente ADMIN ou USUARIO.")
                    return

            if setor == "":
                setor = consulta[3]

            sql = "UPDATE usuario SET nome = ?, email = ?,cargo =?,setor=? WHERE id_usuario = ?"

            cursor.execute(sql,(nome, email,cargo,setor,id_user,))
            conexao.commit()
            print("Usuario atualizado com sucesso!")
                 
        else:
            print("-----Usuario não encontrado!-----")
    
    except Exception as erro:
        print(f"Erro:{erro}")

    finally:
        conexao.close()
