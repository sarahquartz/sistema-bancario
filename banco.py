# Classe Banco

from conta import Conta
import json

class Banco:

    def __init__(self):
        self.contas = []

    def criar_conta(self, titular):
        conta = Conta(titular, 0)
        self.contas.append(conta)
        return conta

    def listar_contas(self):
        return self.contas

    def possui_contas(self):
        return len(self.contas) > 0

    def buscar_conta(self, id_conta):

        for conta in self.contas:
            if conta.id == id_conta:
                return conta

        return None

    def salvar(self):

        dados = []

        for conta in self.contas:
            dados.append(conta.para_dict())

        with open("contas.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def carregar(self):

        try:
            with open("contas.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            self.contas = []

            for conta_dict in dados:
                conta = Conta.de_dict(conta_dict)
                self.contas.append(conta)

            if self.contas:
                maior_id = max(conta.id for conta in self.contas)
                Conta.proximo_id = maior_id + 1

        except FileNotFoundError:
            pass

