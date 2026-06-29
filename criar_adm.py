from conexao import conectar
from datetime import datetime
import bcrypt

conexao = conectar()
cursor = conexao.cursor()

data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Senha original
senha = "123"

# Gerando hash
senha_hash = bcrypt.hashpw(
    senha.encode("utf-8"),
    bcrypt.gensalt()
).decode("utf-8")

cursor.execute("""
INSERT INTO usuario
(nome, email, senha, setor, cargo, status, data_criacao)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    "Administrador",
    "admin",
    senha_hash,
    "TI",
    "ADMIN",
    "ATIVO",
    data_criacao
))

conexao.commit()
conexao.close()

print("Admin criado com sucesso!")