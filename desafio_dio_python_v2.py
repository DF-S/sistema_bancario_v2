import textwrap

def menu(): 
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Novo Usuario
    [6] Listar Contas
    [7] Sair

    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += (f"\n Depósito R$ {valor:.2f}")
            print(f"Depósito no valor de R$ {valor:.2f}, realizado com sucesso!")
    else:
            print("Valor invalido, tente novamente")
               
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques
        
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
            
    elif excedeu_limite:
        print("Operação falhou! O valor de saque excedeu o limite diario.")
            
    elif excedeu_saque:
        print("Operação falhou! Número de saques execidos.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"\n Saque: R$ {valor:.2f}"
        numero_saques += 1
        print(f"Saque no valor de R$ {valor:.2f}, realizado com sucesso!2")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n====================EXTRATO====================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================================")
            
def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Já existe usuário cadastrado com esse CPF! ")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, n° - bairro - cidade/uf): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuário criado com sucesso! ===")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
