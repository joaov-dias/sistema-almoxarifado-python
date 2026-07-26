# DOCUMENTAÇÃO TÉCNICA

# Sistema de Controle de Almoxarifado

Versão: **1.0**

---

# 1. Introdução

O Sistema de Controle de Almoxarifado foi desenvolvido em Python com o objetivo de gerenciar produtos, usuários e movimentações de estoque por meio de uma aplicação de linha de comando (CLI).

O projeto foi criado como parte dos estudos em Análise e Desenvolvimento de Sistemas, buscando aplicar conceitos de programação, banco de dados, autenticação, controle de acesso, organização modular do código e boas práticas de desenvolvimento.

Durante sua evolução, o sistema passou por diversas melhorias e uma etapa completa de refatoração, tornando o código mais organizado, reutilizável e de fácil manutenção.

---

# 2. Objetivo do projeto

O principal objetivo é fornecer um sistema para controle de estoque que permita:

* Gerenciar usuários.
* Controlar produtos.
* Registrar movimentações de entrada e saída.
* Gerar relatórios.
* Registrar logs das operações realizadas.
* Garantir segurança através de autenticação e controle de permissões.

Além disso, o projeto serviu como ferramenta prática para consolidar conhecimentos em Python, SQLite, SQL e Git.

---

# 3. Arquitetura do sistema

O sistema segue uma arquitetura modular.

Cada módulo possui uma responsabilidade específica, facilitando a manutenção e futuras evoluções.

Principais características:

* Separação de responsabilidades.
* Reutilização de código.
* Centralização das validações.
* Organização por módulos.
* Persistência dos dados em SQLite.

---

# 4. Estrutura do projeto

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
├── almoxarifado.db
├── README.md
└── docs/
    ├── DOCUMENTACAO.md
    ├── BANCO_DE_DADOS.md
    ├── HISTORICO.md
    └── imagens/
```

---

# 5. Fluxo de funcionamento

O funcionamento do sistema ocorre na seguinte ordem:

1. O arquivo `setup.py` cria o banco de dados, caso ele não exista, e realiza a configuração inicial do sistema.
2. O primeiro usuário administrador é criado durante a configuração inicial.
3. O usuário executa `main.py`.
4. É realizado o processo de autenticação.
5. O sistema identifica o perfil do usuário.
6. O menu é exibido conforme as permissões do perfil.
7. As operações realizadas atualizam o banco de dados e registram logs quando necessário.

---

# 6. Módulos do sistema

## main.py

Responsável por controlar o fluxo principal da aplicação, realizar o login dos usuários e apresentar os menus do sistema conforme as permissões de acesso.

---

## setup.py

Realiza a configuração inicial do sistema.

Responsabilidades:

* Criar o banco de dados.
* Executar o `schema.sql`.
* Verificar a existência de um usuário administrador.
* Criar o primeiro administrador com senha protegida por bcrypt.

---

## usuario.py

Gerencia todas as operações relacionadas aos usuários.

Funcionalidades:

* Cadastro.
* Listagem.
* Atualização.
* Alteração de senha.
* Alteração de status.
* Login.
* Controle de permissões.

---

## produto.py

Gerencia o cadastro e o controle dos produtos.

Funcionalidades:

* Cadastro.
* Consulta.
* Atualização.
* Exclusão.
* Busca por nome.
* Entrada de estoque.
* Saída de estoque.
* Controle de estoque mínimo.

---

## movimentacao.py

Responsável pelo registro das movimentações de estoque.

Cada entrada ou saída gera um histórico contendo:

* Produto.
* Usuário.
* Tipo da movimentação.
* Quantidade.
* Observação.
* Data e hora.

---

## relatorio.py

Responsável pela geração dos relatórios do sistema.

Inclui:

* Relatório de produtos.
* Produtos com estoque mínimo.
* Relatório de movimentações.
* Exportação para CSV.

---

## logs.py

Responsável pelo registro das ações relevantes realizadas pelos usuários.

Os logs auxiliam na auditoria e rastreabilidade das operações do sistema.

---

## validacoes.py

Centraliza todas as validações utilizadas pelos módulos.

Entre elas:

* Campos obrigatórios.
* Valores inteiros.
* Cargo.
* Status.
* Verificação de permissões.

Essa abordagem reduz duplicação de código e facilita a manutenção.

---

## conexao.py

Responsável por criar e fornecer a conexão com o banco SQLite utilizada pelos demais módulos.

---

# 7. Controle de acesso

O sistema utiliza o modelo **RBAC (Role-Based Access Control)**.

Perfis disponíveis:

## ADMIN

Possui acesso completo ao sistema.

Pode:

* Gerenciar usuários.
* Gerenciar produtos.
* Gerar relatórios.
* Alterar status de usuários.
* Executar todas as operações administrativas.

## USUARIO

Possui acesso apenas às funcionalidades permitidas para operação diária do sistema, conforme as regras implementadas.

---

# 8. Funcionalidades

O sistema oferece:

* Login de usuários.
* Cadastro de usuários.
* Atualização de usuários.
* Alteração de senha.
* Alteração de status.
* Cadastro de produtos.
* Atualização de produtos.
* Exclusão de produtos.
* Busca por nome.
* Entrada de estoque.
* Saída de estoque.
* Histórico de movimentações.
* Relatórios.
* Exportação CSV.
* Registro de logs.

---

# 9. Validações implementadas

Durante a refatoração, as validações foram centralizadas no módulo `validacoes.py`.

As principais validações incluem:

* Campos obrigatórios.
* Valores inteiros válidos.
* Controle de cargos.
* Controle de status.
* Verificação de permissões.
* Validação de autenticação.
* Controle de estoque para evitar saídas inválidas.

Essa centralização reduziu duplicações e aumentou a consistência do sistema.

---

# 10. Segurança

O sistema implementa mecanismos básicos de segurança:

* Senhas armazenadas utilizando bcrypt.
* Autenticação de usuários.
* Controle de acesso baseado em perfis.
* Verificação do status do usuário antes do login.
* Registro de logs para auditoria.
* Controle das operações conforme o perfil autenticado.

---

# 11. Melhorias futuras

Possíveis evoluções do projeto:

* Interface gráfica utilizando CustomTkinter.
* API REST utilizando Flask ou FastAPI.
* Dashboard Web.
* Leitor de código de barras.
* Controle de fornecedores.
* Backup automático.
* Dockerização da aplicação.

---

# 12. Considerações finais

O desenvolvimento deste projeto permitiu aplicar conceitos fundamentais de programação em Python, banco de dados relacionais, autenticação, organização modular, controle de acesso e boas práticas de desenvolvimento.

A versão 1.0 representa uma aplicação estável, estruturada e preparada para futuras evoluções, servindo tanto como ferramenta de aprendizado quanto como projeto de portfólio.
