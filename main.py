from conta import Conta
import os

contas = []

def menu_principal():
    print("\n=== Sistema Bancario ===")
    print("1 - Criar Conta")
    print("2 - Exibir Contas")
    print("3 - Selecionar Conta")
    print("0 - Sair")
    print("========================")

def menu_conta(conta):

    print("========================")
    print("Conta Selecionada")
    print(f"\nConta: {conta.id:04}")
    print(f"Titular: {conta.titular}")
    print(f"Saldo: R$ {conta.saldo:.2f}")
    print("========================")
    print("\n1 - Sacar")
    print("2 - Depositar")
    print("3 - Transferir")
    print("0 - Voltar")
    

def pausar():
    input("\nPressione Enter para continuar...")
    limpar_tela()

def limpar_tela():
    os.system("clear")

def criar_conta(contas):
    titular = input("Digite o nome do titular: ")
    conta = Conta(titular, 100)
    contas.append(conta)
    print("Conta Criada!")

def exibir_contas(contas):
    print("================================")
    for conta in contas:
        print(f"id: {conta.id}, Titular: {conta.titular}, Saldo: {conta.saldo:.2f}")
    print("================================")

def saque(conta, valor):

    if conta.sacar(valor):
        print("\nSaque Efetuado:")
        print(f"Valor R$ {valor:.2f}")
        print(conta.mostrar_saldo())
    else:
        print("\nSaldo Insuficiente!")

def deposito(conta, valor):

    if conta.depositar(valor):
        print("\nDeposito Efetuado:")
        print(f"Valor R$ {valor:.2f}")
        print(conta.mostrar_saldo())
    else:
        print("\nValor Invalido!")

def transferencia(origem, destino, valor):

    if origem.transferir(valor, destino):
        print("\nTrasferencia Efetuada")
        print(f"Valor: R$ {valor:.2f}")
        print("Destino:")
        print(f"Conta: {destino.id:04}")
        print(f"Titular: {destino.titular}")

    else:
        print("Ocorreu um Erro na Transferencia!")

def buscar_conta(contas, id_conta):
    for conta in contas:
        if conta.id == id_conta:
            return conta

    return None



def conta_estado(conta):
    while True:
        menu_conta(conta)
        try:
            select = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite apenas números!")
            pausar()

        if select == 1:
            # Opção de Saque
            try:
                valor = float(input("Digite o valor do Saque: "))
                saque(conta, valor)
            except ValueError:
                print("Digite apenas números")
            pausar()

        elif select == 2:
            # Opção de Deposito
            try:
                valor = float(input("Digite o valor do Deposito: "))
                deposito(conta, valor)
            except ValueError:
                print("Digite apenas números")
            pausar()

        elif select == 3:
            # Opção de Transferencia
            try:
                destino_numero = int(input("Digite o Número da conta: "))
                destino = buscar_conta(contas, destino_numero)

                if destino is None:
                    print("Conta não encontrada!")
                else:
                    valor = float(input("Digite o valor da Transferencia: "))
                    transferencia(conta, destino, valor)

            except ValueError:
                print("Digite apenas números")
            except IndexError:
                print("Conta Invalida!")
            pausar()

        elif select == 0:
            # Sair
            break



while True:

    menu_principal()
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

    elif select == 2:
        exibir_contas(contas)
        pausar()

    elif select == 3:

        try:
            conta_numero = int(input("Digite o número da conta:"))
            conta = buscar_conta(contas, conta_numero)
            limpar_tela()

            if conta is None:
                print("Conta Não Encontrada!")
            else:
                conta_estado(conta)

        except ValueError:
            print("Digite apenas números!")
        except IndexError:
            print("Conta Invalida")
        pausar()


    else:
        print("\nOpção Invalida")
        pausar()
