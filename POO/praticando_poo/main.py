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


    def exibir_saldo(self):
        print(f"Saldo da conta: {self.saldo}")


    def __str__(self):
        return f"Conta: {self.numero_conta}, Titular: {self.nome_titular}, Saldo: R${self.saldo}, Limite: R${self.limite}"


class Banco:
    def __init__(self):
        self.contas = []
        

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"conta {conta.numero_conta} adicionada com sucesso")
    

    def remover_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                self.contas.remove(conta)
                print(f"conta {numero_conta} removida com sucesso")
                return
        print("conta nao encontrada")

    
    def listar_contas(self):
        if self.contas:
            for conta in self.contas:
                print(conta)
        else:
            print("nenhuma conta cadastrada")

banco = Banco()

conta1 = ContaBancaria(numero_conta="123134", nome_titular="joao")
conta2 = ContaBancaria(numero_conta="124345", nome_titular="maria")
conta3 = ContaBancaria(numero_conta='173245', nome_titular="darlan")


banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)
conta3.depositar= (1234)
conta2.depositar= (1234)
conta1.depositar= (1234)

banco.listar_contas()

banco.remover_conta("123134")

banco.listar_contas()