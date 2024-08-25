menu = """ 
     ================ BEM-VINDO ===================
     
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

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor           
            extrato += f"Depósito: {valor:.2f}"
            print(f"Saldo Total: {saldo:.2f}")


    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

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

        else:
            print("Operação inválida!")

    

    elif opcao == "E":
        print("\n============ EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "Q":
        break

    else:
        print("Operação Inválida!")  

          