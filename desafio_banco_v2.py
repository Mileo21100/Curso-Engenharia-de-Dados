menu = """ 
     ================ BEM-VINDO ===================
     
     [U] Cadastrar Novo Usuário
     [C] Cadastrar Nova Conta
     [D] Depositar
     [S] Sacar
     [E] Extrato
     [Q] Sair

     ==============================================       
     """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
conta = []
AGENCIA = "001"



def Depositar(valor, saldo, extrato):       
    if valor > 0:
        saldo += valor           
        extrato += f"\nDepósito: {valor:.2f}"
        print(f"Saldo Total: {saldo:.2f}")
    return saldo, extrato


def Sacar(valor, saldo, extrato, limite, limite_saques, numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES

    if excedeu_saldo:
        print("A Operação Falhou! Você não tem saldo suficiente!")

    elif excedeu_limite:
        print("A Operação Falhou! O valor do Saque excede o limite por operação!")

    elif excedeu_saques:
        print("A Operação Falhou! Você excedeu o limite de número de saques!")

    elif valor > 0:
        saldo -= valor
        print(f"Saque no valor de {valor:.2f} efetuado") 
        numero_saques += 1
        extrato += f"\nSaque: {valor:.2f}"

    else:
        print("Operação inválida!")
    
    return saldo, extrato


def Extrato(saldo, extrato):
    print("\n============ EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")


def ListarUsuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados
        

def CadastrarUsuario(usuarios):
    cpf = int(input("Informe o CPF do Cliente:"))
    usuario = ListarUsuarios(cpf, usuarios)

    if usuario:
        print("Usuário já existe")
        return

    nome = input("Informe o nome do Cliente:")
    dt_nasc = input("Informe a Data de Nascimento:") 
    
    usuarios.append({"nome": nome, "cpf": cpf, "dt_nasc": dt_nasc})
    print("===== Usuário criado com sucesso!!! =====")

def CadastrarContaCorrente(conta):
    #Criar validação do cpf já casatrado
    cpf = int(input("Informe o CPF do Cliente: "))
    num_conta = len(conta)+1
    agencia = AGENCIA
    
    conta.append({"Agência":agencia,"C/C": num_conta,"cpf": cpf})
    print("===== Conta criada com sucesso!!! =====")    
    print(conta) ##VALIDAÇÃO


    


while True:

    opcao = input(menu)          

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = Depositar(valor, saldo, extrato)

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = Sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)   

    elif opcao == "E":
        Extrato(saldo, extrato)

    elif opcao == "U":
        CadastrarUsuario(usuarios)

    elif opcao == "C":
        CadastrarContaCorrente(conta)     

    elif opcao == "Q":
        break

    else:
        print("Operação Inválida!") 


     

          