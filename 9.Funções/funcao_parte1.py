# def exibir_mensagem():
#     print("Olá, Mundo!")
    
# def exibir_mensagem_com_nome(nome):
#     print("Olá,", nome)
    
# def exibir_mensagem_com_nome_na_funcao(nome = "Kaido"):
#     print(f"Seja bem vindo, {nome}!")
      
# exibir_mensagem()
# exibir_mensagem_com_nome("Kaido")
# exibir_mensagem_com_nome_na_funcao()
# exibir_mensagem_com_nome_na_funcao("Zoro")

def calcular_total(numeros):
    print("== Soma total ==")
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"== Antecessor e Sucessor de {numero} ==")
    print(f"Antecessor: {antecessor}")
    print(f"Sucessor: {sucessor}")
    return antecessor, sucessor

print(calcular_total([1,2,3,4,5]))
print(retorna_antecessor_e_sucessor(5))