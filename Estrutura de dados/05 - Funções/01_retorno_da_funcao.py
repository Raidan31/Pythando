#Estruturas das funções

#Soma dos numeros
def calcular_total(numeros):
    return sum(numeros)

#Informa o numero antecessor e o sucessor do valor aplicado
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

#Valores que serão aplicados nas funções
print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
print(func_3()) #None

