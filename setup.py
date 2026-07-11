import sqlite3
from conexao import conectar
from datetime import datetime
import bcrypt


def criar_banco():
    conexao=sqlite3.connect("almoxarifado.db")

    cursor = conexao.cursor()

    #transformar o arquivo sql em variavel
    with open("schema.sql", "r") as arquivo_sql:
        sql = arquivo_sql.read()

    cursor.executescript(sql)

    conexao.commit()

    conexao.close()

def criar_primeiro_adm():
    conexao=conectar()

    cursor = conexao.cursor()
    try:

        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nome = input("Digite o nome do ADMIN ").upper()
        email = input("Digite o Email do ADMIN ").lower()
        
        while True:

            senha = input("Digite a senha do ADMIN ")
            conf_senha = input("Confirme a senha do ADMIN ")

            if senha == conf_senha:
                break
            else:
                print("Senhas não são iguais.")

        senha_hash = bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        
        cursor.execute("""INSERT INTO usuario 
                    (nome, email, senha, setor, cargo, status, data_criacao) 
                    VALUES (?, ?, ?, ?, ?, ?, ?) """, (
                        nome,
                        email,
                        senha_hash,
                        "TI",
                        "ADMIN",
                        "ATIVO",
                        data_criacao
    ))
        conexao.commit()

        print("Administrador criado com sucesso!")

        return True

    except Exception as error:
        print(f"Erro: {error}")
        conexao.rollback()
        return False


    finally:
        conexao.close()


def verificar_adm():
    conexao=conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM usuario WHERE cargo = ?;",("ADMIN",))

        usuario = cursor.fetchone()[0]

        if usuario >= 1 :
            return True
        else:
            return False
        
    except Exception as error:
        print(f"Erro: {error}")
        return False

    finally:
        conexao.close()    

def configurar_sistema():

    criar_banco()

    if verificar_adm():
      print("Admin ja cadastrado, procure um novo admin para fazer o novo cadastro. ")

    else:
        criar_primeiro_adm()
        print("\nConfiguração finalizada!")
        print("Execute agora: python main.py")

if __name__ == "__main__":
    configurar_sistema()

