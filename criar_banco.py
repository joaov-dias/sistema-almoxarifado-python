import sqlite3

conexao=sqlite3.connect("almoxarifado.db")

cursor = conexao.cursor()

#transformar o arquivo sql em variavel
with open("schema.sql", "r") as arquivo_sql:
    sql = arquivo_sql.read()

cursor.executescript(sql)

conexao.commit()

conexao.close()
