# BANCO DE DADOS

# Sistema de Controle de Almoxarifado

Versão: **1.0**

---

# 1. Visão Geral

O sistema utiliza o **SQLite** como banco de dados relacional para armazenar todas as informações da aplicação.

O banco é criado automaticamente pelo arquivo `setup.py`, que executa o script `schema.sql` durante a configuração inicial do sistema.

As principais entidades do banco são:

* Usuários
* Produtos
* Movimentações
* Logs

---

# 2. Tabela: usuario

Responsável pelo armazenamento dos usuários do sistema.

| Campo        | Tipo    | Descrição                              |
| ------------ | ------- | -------------------------------------- |
| id_usuario   | INTEGER | Chave primária (autoincremento)        |
| email        | TEXT    | E-mail do usuário (único)              |
| nome         | TEXT    | Nome do usuário                        |
| senha        | TEXT    | Senha criptografada com bcrypt         |
| setor        | TEXT    | Setor ao qual o usuário pertence       |
| cargo        | TEXT    | Perfil de acesso (ADMIN ou USUARIO)    |
| status       | TEXT    | Situação do usuário (ATIVO ou INATIVO) |
| data_criacao | TEXT    | Data de criação do cadastro            |

---

# 3. Tabela: produto

Responsável pelo cadastro dos produtos.

| Campo         | Tipo    | Descrição                        |
| ------------- | ------- | -------------------------------- |
| id_produto    | INTEGER | Chave primária (autoincremento)  |
| nome          | TEXT    | Nome do produto                  |
| qtd           | INTEGER | Quantidade disponível em estoque |
| descricao     | TEXT    | Descrição do produto             |
| categoria     | TEXT    | Categoria do produto             |
| qtd_minima    | INTEGER | Quantidade mínima permitida      |
| data_cadastro | TEXT    | Data de cadastro                 |
| status        | TEXT    | Situação do produto              |
| local         | TEXT    | Local de armazenamento           |

---

# 4. Tabela: movimentacao

Responsável pelo histórico de movimentações do estoque.

Cada registro representa uma entrada ou saída de produtos.

| Campo      | Tipo     | Descrição                               |
| ---------- | -------- | --------------------------------------- |
| id_movi    | INTEGER  | Chave primária (autoincremento)         |
| id_produto | INTEGER  | Produto movimentado                     |
| id_usuario | INTEGER  | Usuário responsável pela movimentação   |
| data_hora  | DATETIME | Data e hora da operação                 |
| qtd_movi   | INTEGER  | Quantidade movimentada                  |
| tipo_movi  | TEXT     | Tipo da movimentação (entrada ou saída) |
| obs        | TEXT     | Observações da movimentação             |

---

# 5. Tabela: logs

Responsável pelo registro das ações realizadas pelos usuários no sistema.

Esses registros auxiliam na auditoria e rastreabilidade das operações.

| Campo      | Tipo     | Descrição                       |
| ---------- | -------- | ------------------------------- |
| id_log     | INTEGER  | Chave primária (autoincremento) |
| id_usuario | INTEGER  | Usuário responsável pela ação   |
| acao       | TEXT     | Tipo da ação executada          |
| descricao  | TEXT     | Descrição da operação           |
| data_hora  | DATETIME | Data e hora do registro         |

---

# 6. Relacionamentos

O banco possui os seguintes relacionamentos:

* Um **usuário** pode realizar várias **movimentações**.
* Um **produto** pode possuir várias **movimentações**.
* Um **usuário** pode gerar vários **logs**.

Representação simplificada:

```text
usuario (1)
   │
   ├──────────────┐
   │              │
   ▼              ▼
movimentacao     logs
      ▲
      │
produto (1)
```

---

# 7. Integridade dos dados

O banco utiliza mecanismos para garantir a consistência das informações:

* Chaves primárias com autoincremento.
* Chaves estrangeiras entre as tabelas relacionadas.
* Restrição `UNIQUE` para o e-mail dos usuários.
* Restrição `NOT NULL` para campos obrigatórios.
* Restrição `CHECK` na tabela `movimentacao`, permitindo apenas os valores `entrada` e `saida` para o tipo de movimentação.

---

# 8. Considerações finais

A estrutura do banco foi projetada para atender às necessidades do sistema de controle de almoxarifado, mantendo a integridade dos dados e facilitando futuras expansões.

A separação das informações em tabelas específicas contribui para a organização do sistema, reduz redundâncias e simplifica a manutenção da aplicação.
