class CuentaBancaria:
    
    # atributos
    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo
        
    # metodos
    def depositar(self, cantidad):
        return self.saldo + cantidad
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            return self.saldo - cantidad
        else:
            return False
        
    def mostrar_saldo(self):
        return print(self.saldo)
        