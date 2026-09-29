from conta import Conta

conta_sarah = Conta("Sarah", 1000)
print(conta_sarah.titular)
conta_sarah.mostrar_saldo()
print("Saque efetuado")
print(f"Saldo anterior:")
conta_sarah.mostrar_saldo()
conta_sarah.depositar(20)
print("Saldo Atual")
conta_sarah.mostrar_saldo()
conta_sarah.sacar(300)
conta_sarah.mostrar_saldo()