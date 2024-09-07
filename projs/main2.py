#adicionar atividade, data e marcar com o concluida
atividade = []
def adicionar_atividade():
    atividade_dict = {}
    atividade_dict ['titulo_atividade'] = input("Digite o titulo da atividade: ")
    atividade_dict ['descricao_atividade'] = input("Digite a descrição da atividade: ")
    atividade_dict ['data'] = input("Digite a data da atividade: [DD/MM/AAAA] ")
    atividade_dict ['hora'] = input("Digite a hora da atividade: [HH:MM]")
    atividade_dict ['status'] = False
    atividade.append(atividade_dict)
    print (f"Atividade {atividade_dict['titulo_atividade']} adicionada com sucesso! ")
    
def marcar_concluida():
    mostrar_atividade()
    conc = input("Digite o titulo da atividade que deseja marcar como concluida: ")
    for c in atividade:
        if c['titulo_atividade'] == conc:
            c['status'] = True
            print(f"Atividade {c['titulo_atividade']} marcada como concluida.")
            break
        else:
            print("Essa atividade não existe. Tente novamente mais tarde!")

    
def exluir_atividade():
    mostrar_atividade()
    exc = input("Digite o titulo da atividade que deseja excluir: ")
    for c in atividade:
        if c['titulo_atividade'] == exc:
            atividade.remove(c)
            print(f"Atividade '{exc}' excluída com sucesso!")
            break
        else:
            print("Essa atividade não existe. Tente novamente mais tarde!")

def mostrar_atividade():
    for c in atividade:
        print(f"Titulo da atividade: {c['titulo_atividade']}\nDescrição da atividade: {c['descricao_atividade']}\nData da atividade: {c['data']}\nHora da atividade: {c['hora']}\nAtividade concluida? {c['status']}\n")
        

def menu():
    while True:
        print("""
            OPÇÕES:
            1- ADICIONAR ATIVIDADE
            2- MARCAR ATIVIDADE COMO CONCLUIDA
            3- EXCLUIR ATIVIDADE
            4- MOSTRAR TODAS AS ATIVIDADES
            5- SAIR
            """)
        try:
            op = int(input("Escolha uma opção: "))
            if op == 1:
                adicionar_atividade()
            elif op == 2:
                marcar_concluida()
            elif op == 3:
                exluir_atividade()
            elif op == 4:
                mostrar_atividade()
            elif op == 5:
                print("Saindo...")
                break
            else:
                print("Opção invalida. Tente novamente.")
        except ValueError:
            print("Entrada invalida. Por favor, insira um numero.")
            
menu()