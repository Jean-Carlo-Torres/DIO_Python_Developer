saldo = 2000

opcao = int(input("Informe a opção desejada: \n1 - Sacar \n2 - Depositar \n3 - Extrato"))

if opcao == 1:
    saque = float(input("Informe o valor do saque: "))

    if saque <= saldo:
        saldo -= saque
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
        
    print(f"Saldo atual de R$ {saldo}")
    
elif opcao == 2:
    deposito = float(input("Informe o valor do depósito: "))
    
    saldo += deposito
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual de R$ {saldo}")
    
elif opcao == 3:
    print(f"Saldo atual de R$ {saldo}")
    
else:
    print("Opção inválida!")