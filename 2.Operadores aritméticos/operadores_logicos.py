
print("////////////////////////////")

print("True and True:", True and True)
print("True and False:", True and False)
print("True or True:", True or True)
print("True or False:", True or False)
print("False or False:", False or False)

print("////////////////////////////")


saldo = 1000
saque = 200
limite = 100
conta_especial = True


print("operadores:")
print(saldo >= saque)
print(saque <= limite)

print("E (and):")
print(saldo >= saque and saque <= limite)

print("OU (or):")
print(saldo >= saque or saque <= limite)

print("parenteses")
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
