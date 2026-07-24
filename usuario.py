from conexao import conectar
from datetime import datetime
import bcrypt
from logs import registrar_log
from validacoes import ler_campo_obrigatorio, verificar_permissao,ler_inteiro,ler_cargo,ler_status

def cadastrar_usuario(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    nome = ler_campo_obrigatorio("Nome:")
    email = ler_campo_obrigatorio("Email:")
    senha = ler_campo_obrigatorio("Senha:")
    setor = ler_campo_obrigatorio("Setor:")
    cargo = ler_cargo("Cargo: (ADMIN ou USUARIO)")
    status = "ATIVO"
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    senha_hash = bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    try:
        cursor.execute("""INSERT INTO usuario (nome, email, senha, setor, cargo, status, data_criacao)
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (nome, email, senha_hash, setor, cargo, status, data_criacao))
        conexao.commit()

        print("Usuario cadastrado com sucesso!")
        registrar_log(usuario_logado["id_usuario"],"CADASTRAR_USUARIO",f"Cadastrou o usuario {nome}")

    except Exception as erro:
        print(f"Erro ao cadastrar usuario: {erro}")
    
    finally:
        conexao.close()

def login ():
    conexao = conectar()
    cursor = conexao.cursor()
    email = ler_campo_obrigatorio("Email:")
    senha =  ler_campo_obrigatorio("Senha:")
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
                    registrar_log(id_usuario,"LOGIN","Login realizado com sucesso")

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
        print("\nLISTA DE USUÁRIOS")
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

    email = ler_campo_obrigatorio("Email do usuario a ser buscado:")

    try:
        sql = "SELECT id_usuario, nome,email, setor,cargo,status,data_criacao FROM usuario WHERE email LIKE ?"
        cursor.execute(sql,(f"%{email}%",))
        usuarios=cursor.fetchall()
        
        if not usuarios:
            print("Nenhum usuario encontrado!")
        else:
            print("\n-----USUÁRIOS ENCONTRADOS-----")
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
        print(f"Erro ao buscar usuario: {erro}")
    
    finally:
        conexao.close()

def atualizar_usuario(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    id_user = ler_inteiro("ID usuário:")
    
    try:
        sql_consulta = "SELECT nome, email, cargo, setor FROM usuario WHERE id_usuario = ?"

        cursor.execute(sql_consulta,(id_user,))

        consulta=cursor.fetchone()

        if consulta:
            print("-----USUÁRIO ENCONTRADO-----")
            print(f"ID usuario: {id_user}")
            print(f"Nome: {consulta[0]}")
            print(f"Email: {consulta[1]}")
            print(f"Cargo: {consulta[2]}")
            print(f"Setor: {consulta[3]}")
            
            print("Se desejar manter alguma informação, é só apertar ENTER.")
            nome =input("NOME: ")
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
            registrar_log(usuario_logado["id_usuario"],"ATUALIZAR_USUARIO", f"Atualizou o usuario {nome}  (ID {id_user})")
                 
        else:
            print("-----Usuario não encontrado!-----")
    
    except Exception as erro:
        print(f"Erro ao atualizar usuario: {erro}")

    finally:
        conexao.close()

def alterar_status_usuario(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    id_user = ler_inteiro("Id usuário:")
    
    
    try:
        cursor.execute("SELECT nome, email, setor, cargo, status, data_criacao FROM usuario WHERE id_usuario = ?",(id_user,))
        consulta = cursor.fetchone()

        if consulta:
            print("-----USUÁRIO ENCONTRADO-----")
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
            
            novo_status=ler_status("Novo status (ATIVO/INATIVO): ")

            
            cursor.execute("UPDATE usuario SET status = ? WHERE id_usuario = ?",(novo_status,id_user,))  
            conexao.commit()
            print(f"Status alterado para {novo_status}, com sucesso!")
            registrar_log(usuario_logado["id_usuario"],"ALTERAR_STATUS_USUARIO",f"Usuario {consulta[0]}, ID:{id_user} para STATUS: {novo_status}" )

        else:
            print("-----Usuario NÃO encontrado!-----")

    except Exception as erro:
        print(f"Erro alterar status do usuario: {erro}")
    
    finally:
        conexao.close()

def alterar_senha(usuario_logado):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT senha FROM usuario WHERE id_usuario = ?",(usuario_logado["id_usuario"],))
    
        senha_hash = cursor.fetchone()[0]

        senha_antiga = ler_campo_obrigatorio("Senha antiga:")

        senha_correta = bcrypt.checkpw(senha_antiga.encode("utf-8"), senha_hash.encode("utf-8"))

        if not senha_correta:
            print("Senha incorreta.")
            return
        
        while True:
            nova_senha = ler_campo_obrigatorio("Digite a nova Senha: ")

            confirmar_senha = ler_campo_obrigatorio("Digite novamente a NOVA senha: ")

            if nova_senha == confirmar_senha:
                break
            else:
                print("As senhas não coincidem.")

        novo_hash = bcrypt.hashpw(nova_senha.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

        cursor.execute("UPDATE usuario SET senha= ? WHERE id_usuario = ?",(novo_hash,usuario_logado["id_usuario"],))
        conexao.commit()

        print("Senha alterada com sucesso!")
        registrar_log (usuario_logado["id_usuario"],"ALTERAR_SENHA", f"Alteração da senha do usuário ID {usuario_logado['id_usuario']}.")

          


    except Exception as erro:
        print(f"Erro em alterar senha: {erro}")

    finally:
        conexao.close()
    





