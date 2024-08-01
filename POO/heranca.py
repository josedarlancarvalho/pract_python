class Carro:
    numero_rodas = 4
    numero_passageiros = 5

    def acelerar(self):
        print("acelerando...")

    def frear(self):
        print("freando...")

    def buzinar(self):
        print("buziando...")


class Uno(Carro):
    modelo = 'uno'
    ano = 2005
    marca = 'fiat'

uno = Uno()
uno.acelerar()