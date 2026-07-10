from conexao import conectar
from produto import estoque_minimo
from movimentacao import listar_movimentacoes
from datetime import datetime
import csv 
import os



def menu_relatorio():
    while True:
        print("""
              ================= RELATORIOS ==============

              1 - Relatorio de Produtos
              2 - Produtos com Estoque Minimo
              3 - Movimentaçoes
              4 - Exportar CSV
              0 - Voltar
              
              """)
        
        opcao = input("Escolha uma Opção: ").strip()

        if opcao == "1":
            relatorio_produto()
        
        elif opcao == "2":
            estoque_minimo()

        elif opcao == "3":
            listar_movimentacoes()

        elif opcao == "4":
            exportar_produto_csv()

        elif opcao == "0":
            break

        else:
            print("Opção em Valida.")


def relatorio_produto():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_produto,nome,categoria,qtd,qtd_minima,local,status FROM produto ORDER BY nome")

    produtos = cursor.fetchall()

    os.makedirs("relatorios", exist_ok=True)

    if not produtos:
        print("\nProduto não encontrado.")
    else:
        for produto in produtos:
            print(f"""
    ID..................: {produto[0]}
    NOME................: {produto[1]}
    CATEGORIA...........: {produto[2]}
    QUANTIDADE..........: {produto[3]}
    QUANTIDADE MINIMA...: {produto[4]}
    LOCAL...............: {produto[5]}
    STATUS..............: {produto[6]}
    --------------------------------------------------------------

""")
            
    conexao.close()

def exportar_produto_csv():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_produto,nome,categoria,qtd,qtd_minima,local,status FROM produto ORDER BY nome")

    produtos = cursor.fetchall()
    if not produtos:
        print("Nenhum Produto encontrado.")
        conexao.close()
        return

    nome_arquivo = f"relatorios/produtos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open (nome_arquivo,"w", newline="",encoding="utf-8") as arquivo:

        writer = csv.writer(arquivo, delimiter=",")

        writer.writerow(["ID","Nome","Categoria","Quantidade","Qtd_minima","Local","Status"])

        for produto in produtos:
            writer.writerow(produto)

    print(f"Arquivo '{nome_arquivo}' exportado com sucesso!")

    conexao.close()
