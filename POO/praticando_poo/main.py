class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, limite=500):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = 0
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor} realizado com sucesso. Saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente para saque.")