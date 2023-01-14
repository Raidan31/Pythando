#Conjunto é uma coleção de objetos que tem elementos unicos/sem ser duplicados

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4} elimina os itens duplicados

#Não garante a ordem sempre q executar vai vir uma ordem diferente neste caso
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

#Outra forma de utilizar o set
#Ordem aleatória
linguagens = {"python", "java", "python"}
print(linguagens)