BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS movimentacao (
    id_movi INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    data_hora DATETIME NOT NULL,
    qtd_movi INTEGER NOT NULL,
    tipo_movi TEXT NOT NULL CHECK(tipo_movi IN ('entrada', 'saida')),
    obs TEXT,

    FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    qtd INTEGER NOT NULL,
    descricao TEXT,
    categoria TEXT NOT NULL,
    qtd_minima INTEGER NOT NULL,
    data_cadastro TEXT NOT NULL,
    status TEXT NOT NULL,
    local TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    setor TEXT NOT NULL,
    cargo TEXT NOT NULL,
    status TEXT NOT NULL,
    data_criacao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS logs (
    id_log INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    acao TEXT NOT NULL,
    descricao TEXT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

COMMIT;