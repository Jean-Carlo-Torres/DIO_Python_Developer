menu = '''
[d] Depositar
[s] Sacar
[c] Consultar saldo
[x] Sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 3

while True:
    print(menu)
    opcao = input("Digite a opção desejada: ")

    if opcao == "d":
        valor = int(input("Digite o valor a ser depositado: "))
        saldo += valor
        extrato += f"Depósito de R${valor}\n"

    elif opcao == "s":
        if numero_saques > 0:
            valor = int(input("Digite o valor a ser sacado: "))
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque de R${valor}\n"
                numero_saques -= 1
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques atingido")

    elif opcao == "c":
        print(f"Saldo: R${saldo}")

    elif opcao == "x":
        break

    else:
        print("Opção inválida")
        
print(f"Saldo final: R$ {saldo}")