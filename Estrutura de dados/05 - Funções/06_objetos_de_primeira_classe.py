#Objetos de primeira classe podem atribuir funções a variaveis
#passar como parametro para as funções 
#usalos como valores em estruturas de dados (listas, tuplas, dicionários etc)
#E usar como valor de retorno 

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b



def exibir_resultado(a, b, ValorFuncao):
    resultado = ValorFuncao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(15, 10, subtrair) # Resultado 5

op = somar # A variavel recebendo a função de somar
print(op(10,4)) 