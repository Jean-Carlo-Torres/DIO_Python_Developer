Nome= "Saul Goodman"
Idade = 42
profissao = "Advogado"
formacao = "Direito"

# dicionario
dados = {"Nome":Nome, "Idade":Idade, "profissao":profissao, "formacao":formacao}

# formatação com %
print("Olá, meu nome é %s, tenho %d anos e trabalho como %s e sou formado em  %s" %(Nome,Idade,profissao,formacao))

print()

# formatação com .format
print("Olá, meu nome é {}, tenho {} anos e trabalho como {} e sou formado em  {}".format(Nome,Idade,profissao,formacao))

print()

# formatação com f-string
print(f"Olá, meu nome é {Nome}, tenho {Idade} anos e trabalho como {profissao} e sou formado em  {formacao}")

print()

# formtação com dicionario
print(f"Olá, meu nome é {Nome}, tenho {Idade} anos e trabalho como {profissao} e sou formado em  {formacao}".format(**dados))