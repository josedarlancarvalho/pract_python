from uuid import uuid4
lista_prod = []

def cadastrar_prod():
    dict_prod = {}
    dict_prod ['nome'] = input("Digite o nome do produto: ")
    dict_prod ['id'] = uuid4()
    dict_prod ['preco'] = input("Digite o valor do produto: ")
    dict_prod ['estoque'] = input("Digite quantos desse produtos tem em estoque: ")
    lista_prod.append(dict_prod)

def listar_prod():
    for c in lista_prod:
        print(f"Nome do produto: {c['nome']}\n ID do produto: {c['id']}\n Valor do produto: {c['preco']}\n Estoque do produto: {c['estoque']}\n")

def excluir_prod():
    listar_prod()
    exc = input("Digite o nome do produto que deseja excluir: ")
    for c in lista_prod:
        if c['nome'] == exc:
            lista_prod.remove(c)
            print(f"Produto {exc} removido com sucesso!")
            break
        else:
            print("ERRO. Nome inválido.")

while True:
    print('''
        OPCOES:
        1- CADASTRAR PRODUTO  
        2- LISTAR PRODUTO
        3- EXCLUIR PRODUTO  
        4- SAIR
          ''')
    op = int(input("Escolha uma opcao:"))
    if op == 1:
        cadastrar_prod()
    elif op == 2:
        listar_prod()
    elif op == 3:
        excluir_prod()
    elif op == 4:
        break
