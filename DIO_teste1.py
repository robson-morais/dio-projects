menu = ("""
      Selecione uma das opções a seguir:
      [D] Depositar
      [S] Sacar
      [E] Extrato
      [Q] Sair
""")
saldo = 0
limite = 500
extrato = ""
quant_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        deposito = int(input("Digite o valor do depósito: "))

        while deposito <= 0:
            print ("Valor invalido. Por favor, digite novamente.")
            deposito = int(input("Digite o valor do depósito: "))

        saldo += deposito
        extrato += f"Depósito: R$ {deposito: .2f}\n"

    elif opcao == "s":

        saque = float(input("Digite o valor desejado: "))
        while saque <= 0:
            saque = float(input("Valor inválido. Por favor, digite novamente: "))

        limite_valor = saque > limite
        limite_saldo = saque > saldo
        quant_max_saques = quant_saques >= LIMITE_SAQUES

        if limite_valor:
            print ("O valor máximo disponível para saques é de R$ 500,00")

        elif limite_saldo:
            print("Seu saldo é insuficiente.")
        
        elif quant_max_saques:
            print("Limite de saques diários atingido. Tente novamente mais tarde.")
        
        else:
            saldo -= saque
            extrato += f"Saque: R${saque: .2f}\n"
            quant_saques += 1
        

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("\n=============================")

    elif opcao == "q":
        break


    else:
        print("Opção inválida. Por favor selecione uma das opções a seguir: ")