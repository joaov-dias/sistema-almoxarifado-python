# Histórico de Versões

Este documento registra a evolução do Sistema de Controle de Almoxarifado desde o início do desenvolvimento.

---

# v1.0.0 – Julho/2026 (Versão Estável)

## Documentação

* Atualização completa do README.
* Criação da documentação técnica do projeto.
* Documentação da estrutura do banco de dados.

## Refatoração

* Criação do módulo `validacoes.py`.
* Simplificação dos módulos `usuario.py` e `produto.py`.
* Reorganização do fluxo do sistema.
* Redução de código duplicado.
* Melhor organização das responsabilidades dos módulos.

## Setup

* Criação do `setup.py` para configuração inicial do sistema.
* Remoção da criação separada do banco de dados.
* Atualização do `.gitignore`.

## Relatórios

* Relatórios de produtos.
* Relatório de estoque mínimo.
* Histórico de movimentações.
* Exportação de dados em CSV.

---

# v0.9.0 – Junho/2026

## Segurança

* Implementação de autenticação utilizando hash com bcrypt.
* Alteração segura de senha.
* Sistema de auditoria (logs) para registro das ações dos usuários.

---

# v0.8.0 – Maio/2026

## Usuários

* Cadastro de usuários.
* Sistema de login.
* Controle de acesso baseado em cargos (RBAC).
* Sistema flexível de permissões.
* Listagem de usuários.
* Busca e atualização de usuários.
* Alteração de status dos usuários.
* Bloqueios de segurança para impedir alterações indevidas.

---

# v0.7.0 – Maio/2026

## Sistema

* Reorganização do menu principal.
* Integração do histórico de movimentações.

---

# v0.6.0 – Abril/2026

## Estoque

* Entrada de produtos.
* Saída de produtos.
* Registro de movimentações.
* Melhorias gerais no gerenciamento de estoque.

---

# v0.5.0 – Março/2026

## Produtos

* Cadastro de produtos.
* Busca de produtos por nome.
* Verificação automática de estoque mínimo.

## Projeto

* Criação do README inicial.
* Inclusão da descrição do projeto.
* Correção de conflitos no `.gitignore`.

---

# v0.1.0 – Março/2026

## Início do Projeto

* Criação do repositório.
* Estrutura inicial do sistema.
* Primeira versão funcional do Sistema de Controle de Almoxarifado em Python utilizando SQLite.

---

## Tecnologias Utilizadas

* Python
* SQLite
* bcrypt
* CSV
* Git
* GitHub

---

## Observação

O projeto foi desenvolvido de forma incremental, com foco na organização do código, aplicação de boas práticas de programação, segurança, controle de acesso, auditoria e documentação, servindo como projeto de portfólio e de aprendizado em Python.
