from conexao import conectar
from datetime import datetime
import bcrypt

def cadastrar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ").strip()
    setor = input("Digite o setor do usuário: ")
    cargo = input("Digite o cargo do usuário: (ADMIN ou USUARIO)").upper()
    status = "ATIVO"
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    senha_hash = bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    try:
        if cargo not in ["ADMIN", "USUARIO"]:
            print("Cargo invalido! somente ADMIN ou USUARIO")
            return
        
        cursor.execute("""INSERT INTO usuario (nome, email, senha, setor, cargo, status, data_criacao)
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (nome, email, senha_hash, setor, cargo, status, data_criacao))
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
        cursor.execute("SELECT id_usuario,nome, email,cargo,status,senha FROM usuario WHERE email=?",(email,))
        
        usuario = cursor.fetchone()

        if usuario:
            id_usuario, nome, email, cargo, status, senha_hash = usuario

            senha_valida = bcrypt.checkpw(
                senha.encode("utf-8"),
                senha_hash.encode("utf-8")
            )

            if senha_valida:
                if usuario[4] == "ATIVO":
                    print(f"\nBem vindo,{nome}!")
                    print(f"Cargo:{cargo}")
                    print(f"Login realizado com sucesso!")

                    return{
                    "id_usuario":id_usuario,
                        "nome":nome,
                    "email":email,
                    "cargo":cargo,
                    "status":status,}
                else:
                    print("Usuario inativo, procure um Administrador!")
                    return None
            else:
                print("Email ou senha inválidos.")
                return None
        else:
                print("Email ou senha inválidos.")
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

def atualizar_usuario(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    id_user = input("ID usuário:").strip()
    if not id_user.isdigit(): #Se não for numero
        print("ID invalido! Digite um numero.")
        conexao.close()
        return
    id_user = int(id_user)
    
    try:
        sql_consulta = "SELECT nome, email, cargo, setor FROM usuario WHERE id_usuario = ?"

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
                            
            if cargo not in ["ADMIN", "USUARIO"]:
                    print("Cargo inválido! Somente ADMIN ou USUARIO.")
                    return
            
            if usuario_logado["id_usuario"] == id_user and cargo != consulta[2]:
                print("Não é permitido alterar seu próprio cargo.")
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

def alterar_status_usuario(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    id_user = input("Id usuário:").strip()
    
    if not id_user.isdigit():
        print("Digite apenas o NUMERO do ID do usuario.")
        conexao.close()
        return
    
    id_user = int(id_user)    
    
    try:
        cursor.execute("SELECT nome, email, setor, cargo, status, data_criacao FROM usuario WHERE id_usuario = ?",(id_user,))
        consulta = cursor.fetchone()

        if consulta:
            print("-----USUARIO ENCONTRADO-----")
            print(f"ID usuario: {id_user}")
            print(f"Nome: {consulta[0]}")
            print(f"Email: {consulta[1]}")
            print(f"Setor: {consulta[2]}")
            print(f"Cargo: {consulta[3]}")
            print(f"Status: {consulta[4]}")
            print(f"Data Criação: {consulta[5]}")

            if usuario_logado["id_usuario"] == id_user:
                print("Não é permitido alterar seu próprio status.")
                return
            
            novo_status=input("Novo status (ATIVO/INATIVO): ").strip().upper()

            if novo_status not in ["ATIVO", "INATIVO"]:
                print("Status inválido, Somente ATIVO ou INATIVO.")
                return
            
            cursor.execute("UPDATE usuario SET status = ? WHERE id_usuario = ?",(novo_status,id_user,))  
            conexao.commit()
            print(f"Status alterado para {novo_status}, com sucesso!")

        else:
            print("-----Usuario NÃO encontrado!-----")

    except Exception as erro:
        print(f"Erro:{erro}")
    
    finally:
        conexao.close()

def alterar_senha(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT senha FROM usuario WHERE id_usuario = ?",(usuario_logado["id_usuario"],))
    
        senha_hash = cursor.fetchone()[0]

        senha_antiga = input("Senha antiga:").strip()

        senha_correta = bcrypt.checkpw(senha_antiga.encode("utf-8"), senha_hash.encode("utf-8"))

        if not senha_correta:
            print("Senha incorreta.")
            return
        
        while True:
            nova_senha = input("Digite a nova Senha: ").strip()

            confirmar_senha =input("Digite novamente a NOVA senha: ").strip()

            if nova_senha == confirmar_senha:
                break
            else:
                print("As senhas não coincidem.")

        novo_hash = bcrypt.hashpw(nova_senha.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

        cursor.execute("UPDATE usuario SET senha= ? WHERE id_usuario = ?",(novo_hash,usuario_logado["id_usuario"],))
        conexao.commit()

        print("Senha alterada com sucesso!")

          


    except Exception as erro:
        print(f"Erro: {erro}")

    finally:
        conexao.close()
    




