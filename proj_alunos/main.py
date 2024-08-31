alunos = []

def notas():
    alunos_dict = {}
    alunos_dict['nome'] = input("Digite o nome do aluno: ")
    alunos_dict['materia'] = input("Qual matéria deseja adicionar as notas? ")
    alunos_dict['nota_1'] = int(input("Nota 1: "))
    alunos_dict['nota_2'] = int(input("Nota 2: "))
    alunos.append(alunos_dict)

def mostrar_notas():
    for c in alunos:
        print(f"Aluno: {c['nome']}\nMatéria: {c['materia']}\nNota 1: {c['nota_1']}\nNota 2: {c['nota_2']}\n")

def calcular_media():
    mostrar_notas()
    op = input("Qual matéria deseja calcular a média? ")
    materia_encontrada = False
    for c in alunos:
        if op.lower() == c['materia'].lower():  # Case insensitive comparison
            media = (c["nota_1"] + c["nota_2"]) / 2
            print(f"Média em {c['materia']}: {media:.2f}")
            materia_encontrada = True
            break  # Para após encontrar a primeira ocorrência
    if not materia_encontrada:
        print("Matéria não encontrada.")

def status_aluno():
    for c in alunos:
        media = (c["nota_1"] + c["nota_2"]) / 2
        print(f"Matéria: {c['materia']}\nMédia: {media:.2f}")
        if media >= 7:
            print(f"{c['materia']} = APROVADO")
        elif 5 <= media < 7:
            print(f"{c['materia']} = EM RECUPERAÇÃO")
        else:
            print(f"{c['materia']} = REPROVADO")
        print()  # Adiciona uma linha em branco para melhorar a legibilidade

def menu():
    while True:
        print("""
            OPÇÕES:
            1- ADICIONAR NOTA
            2- MOSTRAR NOTAS
            3- CALCULAR E MOSTRAR A MÉDIA
            4- VERIFICAR O STATUS DO ALUNO
            5- SAIR
            """)
        try:
            op = int(input("Escolha uma opção: "))
            if op == 1:
                notas()
            elif op == 2:
                mostrar_notas()
            elif op == 3:
                calcular_media()
            elif op == 4:
                status_aluno()
            elif op == 5:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            
menu()
