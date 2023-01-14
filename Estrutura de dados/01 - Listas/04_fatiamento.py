lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"], pois 3 - 1 = 2
print(lista[0:3:2])  # ["p", "t"] O está servindo pra contar o "passo" a cadencia sem o dois iria retornar o p, y, t
print(lista[0:3]) # A logica é 0 + 2 (Retornando o 0 e o 2)
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
