# 📦 Sistema de Controle de Almoxarifado (Python)

Sistema de gerenciamento de almoxarifado desenvolvido em **Python** com banco de dados **SQLite**, criado com foco em boas práticas de programação, organização modular e controle de estoque.

Esta é a **versão 1.0**, considerada estável, após uma etapa completa de desenvolvimento, testes e refatoração do código.

---

# 🎯 Objetivo

O projeto tem como objetivo fornecer um sistema para gerenciamento de produtos e movimentações de estoque, permitindo o controle de usuários, autenticação, níveis de acesso e geração de relatórios.

Além de atender às funcionalidades propostas, o projeto foi desenvolvido para consolidar conhecimentos em Python, SQL, SQLite, Git e organização de software.

---

# 🚀 Funcionalidades

### Autenticação

* Login de usuários
* Senhas protegidas com bcrypt
* Alteração de senha
* Controle de usuários ativos e inativos

### Controle de acesso (RBAC)

* Perfil ADMIN
* Perfil USUÁRIO
* Restrição de funcionalidades conforme o perfil

### Gerenciamento de usuários

* Cadastro
* Listagem
* Atualização
* Alteração de status
* Controle de permissões

### Gerenciamento de produtos

* Cadastro
* Listagem
* Atualização
* Exclusão
* Busca por nome
* Controle de estoque mínimo

### Movimentação de estoque

* Entrada de produtos
* Saída de produtos
* Registro de movimentações
* Histórico completo

### Relatórios

* Relatório de produtos
* Produtos com estoque mínimo
* Relatório de movimentações
* Exportação de produtos em CSV

### Auditoria

* Registro de logs das principais operações realizadas no sistema

---

# 🛠 Tecnologias utilizadas

* Python 3
* SQLite
* SQL
* bcrypt
* Git
* GitHub

---

# 📁 Estrutura do projeto

```text
sistema-almoxarifado-python/
│
├── main.py
├── setup.py
├── conexao.py
├── usuario.py
├── produto.py
├── movimentacao.py
├── relatorio.py
├── logs.py
├── validacoes.py
├── schema.sql
├── docs/
└── README.md
```

---

# ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/joaov-dias/sistema-almoxarifado-python.git
```

Entre na pasta do projeto:

```bash
cd sistema-almoxarifado-python
```

Execute a configuração inicial:

```bash
python setup.py
```

Inicie o sistema:

```bash
python main.py
```

---

# 🔒 Controle de acesso

O sistema utiliza **RBAC (Role-Based Access Control)**.

Existem dois níveis de acesso:

* **ADMIN**

  * Gerenciamento de usuários
  * Gerenciamento de produtos
  * Relatórios
  * Controle completo do sistema

* **USUÁRIO**

  * Consulta de produtos
  * Entrada e saída de estoque
  * Funcionalidades permitidas pelo perfil

---

# 🗄 Banco de dados

O sistema utiliza **SQLite**, contendo tabelas para:

* Usuários
* Produtos
* Movimentações

A documentação completa do banco encontra-se em:

```
docs/BANCO_DE_DADOS.md
```

---

# 📚 Documentação

A documentação técnica está disponível na pasta:

```text
docs/
```

Contendo:

* DOCUMENTACAO.md
* BANCO_DE_DADOS.md
* HISTORICO.md

---

# 🚀 Melhorias futuras

Algumas funcionalidades planejadas para versões futuras:

* Interface gráfica (CustomTkinter)
* API REST com Flask ou FastAPI
* Dashboard Web
* Leitor de código de barras
* Controle de fornecedores
* Backup automático

---

# 👨‍💻 Autor

**João Vitor Dias Venchiarutti dos Santos**

Projeto desenvolvido como parte dos estudos em Análise e Desenvolvimento de Sistemas, com foco na aplicação de conceitos de programação, banco de dados, autenticação, controle de acesso, organização de código e boas práticas de desenvolvimento.
