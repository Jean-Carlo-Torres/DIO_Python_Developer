contatos = {
    "funcionario.1@gmail.com": {"nome": "João", "telefone": "3333-3333"},
    "funcionario.2@gmail.com": {"nome": "Maria", "telefone": "4444-4444"},
    "funcionario.3@gmail.com": {"nome": "Pedro", "telefone": "5555-5555"},
}

print("=== Lista de emails de funcionarios ===")
print(contatos)
print()

# método .copy
contatos2 = contatos.copy()
print("=== Cópia da lista de emails ===")
print(contatos2)
print()

# método .get
print("=== Busca por dados de um email ===")
print(contatos.get("funcionario.1@gmail.com", {}))
print()

# método .items
print("=== Busca por itens de um dicionário  ===")
print(contatos.items())
print()

# método .keys
print("=== Busca por chaves de um dicionário  ===")
print(contatos.keys())
print()

# método .values
print("=== Busca por valores de um dicionário  ===")
print(contatos.values())
print()

# método .pop
print("=== Remoção de um item de um dicionário  ===")
print(contatos.pop("funcionario.3@gmail.com")) #popitem
print(contatos)
print()

# método .setdefault
print("=== Busca por um valor de uma chave  ===")
funcionario = {"nome": "João", "telefone": "3333-3333"}

print(funcionario.setdefault("nome", "Maria"))

funcionario.setdefault("cargo", "Programador")
print(funcionario)
print()

# método .fromkeys
print("=== Criação de dicionário com chaves ===")
print(dict.fromkeys(["nome","telefone"]))
print(dict.fromkeys(["nome","telefone"], "vazio"))
print()


# método .clear
contatos.clear()
contatos