class Conta:

    proximo_id = 1

    def __init__(self, titular, saldo):
        self.id = Conta.proximo_id
        Conta.proximo_id += 1
        self.titular = titular
        self.saldo = saldo


    def mostrar_saldo(self):

        return f"Saldo em conta: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        
        if valor <= 0:
            return False

        self.saldo += valor
        return True

    def sacar(self, valor):

        if valor <= 0:
            return False

        if valor > self.saldo:
            return False
        
        self.saldo -= valor
        return True

    def transferir(self, valor, destino):

        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False
            
