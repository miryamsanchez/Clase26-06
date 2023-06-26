class Animal:
    def emitir_sonido(self):
        pass

class Perro(Animal):
    def emitir_sonido(self):
        print("Guay, guay")

class Gato(Animal):
    def emitir_sonido(self):
        print("Miau")

class Gallo(Animal):
    def emitir_sonido(self):
        print("Kikiriki")

if __name__ == "__main__":
    perro = Perro()
    gato = Gato()
    gallo = Gallo()

    perro.emitir_sonido()
    gato.emitir_sonido()
    gallo.emitir_sonido()