#Função é um bloco de código identificado por um nome
#O nome poderá receber uma lista de parametros(As entradas da função)
# def é a palavra reservada para função no python

# Declarar a função
# Apenas está registrando em memoria 
def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

#Aqui executa a função registrada acima
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme") #Essa aqui necessita que o nome seja declarado
exibir_mensagem_3() #Por não receber um nome iguais a mensagem2 e 3, essa aqui foi registrada como anonimo
exibir_mensagem_3(nome="Chappie") #Essa aqui se o nome não fosse declarado seria impresso anonimo
