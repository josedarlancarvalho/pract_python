class Animal():
    
    def emitir_som(self):
        print("qualquer som")

class Cachorro(Animal):

    def emitir_som(self):
        print("AU AU")

class Gato(Animal):

    def emitir_som(self):
        print("MIAU")

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()