from conta import Conta
import os

contas = []

def menu():
    print("\n=== Sistema Bancario ===")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Transferir")
    print("5 - Exibir Contas")
    print("0 - Sair")
    print("========================")

def pausar():
    input("\nPressione Enter para continuar...")
    limpar_tela()

def limpar_tela():
    os.system("clear")

def criar_conta(contas):
    titular = input("Digite o nome do titular: ")
    conta = Conta(titular, 0)
    contas.append(conta)

def exibir_contas(contas):
    for conta in contas:
        print(f"id: {conta.id}, Titular: {conta.titular}, Saldo: {conta.saldo}")


while True:

    menu()
    try:
        select = int(input("Digite a opção desejada: "))

    except ValueError:
        print("Digite apenas números!")
        continue

    if select == 0:
        break

    elif select == 1:
        criar_conta(contas)
        pausar()

    elif select == 5:
        exibir_contas(contas)
        pausar()

    else:
        print("\nOpção Invalida")
        pausar()
