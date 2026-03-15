BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "movimentacao" (
"id_movi" INTEGER NOT NULL,
"id_produto" INTEGER NOT NULL,
"id_usuario" INTEGER NOT NULL,
"data_hora" TEXT NOT NULL,
"qtd_movi" INTEGER,
"obs" TEXT,
"tipo_movi" TEXT,
PRIMARY KEY("id_movi" AUTOINCREMENT),
FOREIGN KEY("id_produto") REFERENCES "produto"("id_produto"),
FOREIGN KEY("id_usuario") REFERENCES "usuario"("id_usuario")
);

CREATE TABLE IF NOT EXISTS "produto" (
"id_produto" INTEGER,
"nome" TEXT NOT NULL,
"qtd" INTEGER NOT NULL,
"descricao" TEXT,
"categoria" TEXT NOT NULL,
"qtd_minima" INTEGER NOT NULL,
"data_cadastro" TEXT NOT NULL,
"status" TEXT NOT NULL,
"local" TEXT NOT NULL,
PRIMARY KEY("id_produto" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "usuario" (
"id_usuario" INTEGER NOT NULL,
"email" TEXT NOT NULL UNIQUE,
"nome" TEXT NOT NULL,
"senha" TEXT NOT NULL,
"setor" TEXT NOT NULL,
"cargo" TEXT NOT NULL,
"status" TEXT NOT NULL,
"data_criacao" TEXT NOT NULL,
PRIMARY KEY("id_usuario" AUTOINCREMENT)
);

COMMIT;
