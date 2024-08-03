class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("plano invalido")
    
    def mudar_plano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("plano invalido")

        
cliente = Cliente("darlan", "darlan@gmail.com", "basic")
print(cliente.plano)

cliente.mudar_plano("premium")
print(cliente.plano)