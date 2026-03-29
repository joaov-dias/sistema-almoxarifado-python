📦 Sistema de Controle de Almoxarifado (Python)

Sistema desenvolvido em Python para controle de produtos em um almoxarifado, com funcionalidades de cadastro, consulta, atualização e monitoramento de estoque.

🚀 Funcionalidades
-Cadastrar produtos
-Listar produtos
-Atualizar produtos
-Deletar produtos
-Buscar produto por nome
-Verificar produtos com estoque mínimo

🛠️ Tecnologias utilizadas
Python 3
SQLite
SQL
Git e GitHub

📁 Estrutura do Projeto
PROJETO_ALMOXARIFADO/
│
├── main.py            # Menu principal do sistema
├── produto.py         # Funções de manipulação dos produtos
├── conexao.py         # Conexão com banco SQLite
├── criar_banco.py     # Criação do banco de dados
├── schema.sql         # Estrutura das tabelas
└── almoxarifado.db    # Banco de dados SQLite

▶️ Como executar o projeto
Clone o repositório
git clone https://github.com/joaov-dias/sistema-almoxarifado-python.git

Acesse a pasta
cd sistema-almoxarifado-python

Execute o sistema
python main.py

📌 Funcionalidade de estoque mínimo

O sistema possui verificação automática para identificar produtos com quantidade menor ou igual ao estoque mínimo definido.

Isso permite controle e reposição eficiente dos itens.

📈 Melhorias futuras
 -Entrada de estoque
 -Saída de estoque
 -Histórico de movimentação
 -Sistema de login (ADMIN / USUÁRIO)
 -Relatórios de produtos
 -Interface gráfica
 
👨‍💻 Autor

João Vitor Dias Venchiarutti dos Santos
Projeto para fins de estudo e portfólio.
