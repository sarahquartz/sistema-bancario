class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def mostrar_saldo(self):

        print(f"Saldo em conta: R$ {self.saldo}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return self.saldo
        else: 
            return

    def sacar(self, valor):

        if valor > self.saldo and valor > 0:
            return False
        else:
            self.saldo -= valor
            return True

    def transferir(self, valor, destino):

        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False
            
