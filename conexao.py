import sqlite3

def conectar():
    try:
        conexao= sqlite3.connect("almoxarifado.db")
        return conexao
    
    except sqlite3.Error as erro:
        print("Erro ao conectar ao banco",erro)