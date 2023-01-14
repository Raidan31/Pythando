#Discarta um valor que existe no conjunto, se o valor não existir será ignorado
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) #Valor existe é descartado
numeros.discard(45) #Valor n existe é ignorado

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
