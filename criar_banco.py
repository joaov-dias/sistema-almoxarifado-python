import sqlite3

#Conectar ou criar banco "almoxarifado.db"
conexao=sqlite3.connect("almoxarifado.db")

cursor = conexao.cursor()

#abrir o arquivo, ler e tranformar em variavel o arquivo sql (schema.sql)
with open("schema.sql", "r") as arquivo_sql:
    sql = arquivo_sql.read()

#executar o script sql
cursor.executescript(sql)

conexao.commit()

conexao.close()
