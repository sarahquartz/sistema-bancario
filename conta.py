class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def mostrar_saldo(self):
        print(f"Saldo em conta: R$ {self.saldo}")