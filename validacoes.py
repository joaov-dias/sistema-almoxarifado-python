def ler_campo_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print(f"Campo '{mensagem}' não pode ficar vazio.")

def verificar_permissao(usuario,cargos_permitido ):
    if usuario["cargo"] not in cargos_permitido:
        print("Acesso negado! Voce não tem permissao para usar essa função")
        return False
    return True

def ler_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor.isdigit():
            valor = int(valor)
            if valor >= 1:
                return valor

        print(f"Digite um numero inteiro maior ou igual a 1")

def ler_cargo(mensagem):
    while True:
        cargo = ler_campo_obrigatorio(mensagem).upper()
        if cargo in ["ADMIN","USUARIO"]:
            return cargo

        print("Cargo invalido, somente ADMIN ou USUARIO")

def ler_status(mensagem):
    while True:
        status = ler_campo_obrigatorio(mensagem).upper()
        if status in ["ATIVO","INATIVO"]:
            return status
        print("Status Invalido, somente ATIVO ou INATIVO")
