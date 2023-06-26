class BankAccount:
    def __init__(self, numeroCuenta, titular,saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo
    
    def depositarDinero(self, dinero):
        if dinero > 0:
            self.saldo = self.saldo + dinero
            print(f"Deposito exitoso, su saldo actual es de: {self.saldo}")
        else:
            print ("No se realizo el deposito")
        
    def retirarDinero(self, dinero):
        if self.saldo > 0 and dinero < self.saldo:
            self.saldo - dinero 
            print(f"Retiro exitoso, su saldo actual es de {self.saldo}")
        else:
            print("No se puede realizar el retiro")

    def estadoCuenta():
        print(f"{self.titular}Su saldo actual es de {self.saldo}")

    if __name__=="__main__":
        b = BankAccount("666666", "Jhoe Doe")
        b.depositarDinero(10000)
        b.retirarDinero(5000)
        print(b.estadoCuenta())
