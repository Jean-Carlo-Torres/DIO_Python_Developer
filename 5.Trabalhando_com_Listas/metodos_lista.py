lista = []

# Método [].append
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
print()

# Método .copy
lista2 = lista.copy()
print(lista2)
print()

# Método .clear
print("Método clear..")
lista.clear()
print()

# Método .count
cores = ["vermelho", "verde", "azul", "verde", "vermelho"]
print("Qt. vermelho:",cores.count("vermelho"))
print("Qt. verde:",cores.count("verde"))
print("Qt. azul:",cores.count("azul"))
print()

# Método .extend
linguagens = ["Python", "Java", "C#"]
linguagens.extend(["C", "C++"])
print(linguagens)
print()

# Método .index
print("Posição do C#:", linguagens.index("C#"))
print("Posição do Python:",linguagens.index("Python"))
print()

# Método .sort
linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
print()

# Método .reverse
print(linguagens.reverse())
print(linguagens)
print()

# Método .pop
linguagens.pop() # Remove o último elemento

# Método .remove
linguagens.remove("C") # Remove o elemento C

# Método .len
print("Quantidade de itens na lista:",len(linguagens))


