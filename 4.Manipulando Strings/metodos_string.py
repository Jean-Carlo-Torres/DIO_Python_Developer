string = " Winter is coming "
string

# Métodos de tamanho string
print("Maisculas:", string.upper())
print("Minusculas:", string.lower())
print("Titulo:", string.title())

print()

# Métodos de remoção de espaços
print("Remoção de espaços:", string.strip() + ".")
print("Remoção inicial:", string.rstrip() + ".")
print("Remoção fim:", string.lstrip() + ".")

print()

# Métodos de junções e centralizações
curso = 'Python'

print(curso.center(10, '*'))
print(".".join(curso))