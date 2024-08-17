from datetime import date
import random

cartoes = ['R$50', 'R$250', 'R$120']

nome= str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
data_registro= date.today()
cartao= random.choice(cartoes)
data_aniversario = input("Digite a sua data de aniversario: [DD/MM/AAAA] ")
    
print(f"Ola {nome}, seja bem vindo. Seu registo dia {data_registro} foi concluido com sucesso. Ouve um sorteio e voce ganhou um vouncher de {cartao}. Parabens")