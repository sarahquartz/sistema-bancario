class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def mostrar_saldo(self):

        print(f"Saldo em conta: R$ {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):

        if valor > self.saldo:
            return 0
        else:
            self.saldo -= valor
            return valor