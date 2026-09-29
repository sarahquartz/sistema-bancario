from conta import Conta

conta_sarah = Conta("Sarah", 1000)
conta_thiago = Conta("Thiago", 2000)

print(conta_sarah.titular)
conta_sarah.mostrar_saldo()
print("Saque efetuado")
print(f"Saldo anterior:")
conta_sarah.mostrar_saldo()
conta_sarah.depositar(20)
print("Saldo Atual")
conta_sarah.mostrar_saldo()

if conta_sarah.sacar(3000):
    conta_sarah.mostrar_saldo()
else:
    print("Saldo insuficiente")

if conta_sarah.transferir(10000, conta_thiago):
    conta_sarah.mostrar_saldo()
    conta_thiago.mostrar_saldo()
else:
    print("Saldo Insuficiente")