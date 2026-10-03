# Classe Banco

from conta import Conta

class Banco:

    def __init__(self):
        self.contas = []

    def criar_conta(self, titular):
        conta = Conta(titular, 0)
        self.contas.append(conta)
        return conta

    def listar_contas(self):

        if not self.contas:
            return False
        
        return True

    def buscar_conta(self, id_conta):

        for conta in self.contas:
            if conta.id == id_conta:
                return conta

        return None

