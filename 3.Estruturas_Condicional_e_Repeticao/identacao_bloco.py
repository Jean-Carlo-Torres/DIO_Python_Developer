def sacar(valor):
    saldo = 1000
    
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado com sucesso!")
        print("Saldo atual: R$", saldo)
        
def depositar(valor):
    saldo = 1000
    
    saldo += valor
    print("Deposito de R$", valor, " realizado com sucesso!")
    print("Saldo atual: R$", saldo)
        
sacar(500)
depositar(700)