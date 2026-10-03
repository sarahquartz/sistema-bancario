from datetime import datetime

class Conta:

    proximo_id = 1

    def __init__(self, titular, saldo):
        self.id = Conta.proximo_id
        Conta.proximo_id += 1
        self.titular = titular
        self.saldo = saldo
        self.extrato = []


    def mostrar_saldo(self):

        return f"Saldo em conta: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        
        if valor <= 0:
            return False

        self.saldo += valor
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.extrato.append(f"[{data}] Deposito: R$: {valor:.2f}")
        return True

    def sacar(self, valor):

        if valor <= 0:
            return False

        if valor > self.saldo:
            return False

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.extrato.append(f"[{data}] Saque: R$: {valor:.2f}")
        self.saldo -= valor
        return True

    def transferir(self, valor, destino):

        if valor <= 0:
            return False

        if valor > self.saldo:
            return False

        if destino.id == self.id:
            return False

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.saldo -= valor
        self.extrato.append(f"[{data}] Transferencia Efetuada: R$ {valor:.2f}")
        destino.saldo += valor
        destino.extrato.append(f"[{data}] Transferencia Recebida: R$ {valor:.2f}")

        return True

    def para_dict(self):
        return {"id": self.id,
                "titular": self.titular,
                "saldo": self.saldo,
                "extrato": self.extrato}

    @classmethod
    def de_dict(cls, dados):
        conta = cls(dados["titular"], dados["saldo"])
        conta.id = dados["id"]
        conta.extrato = dados["extrato"]
        return conta

