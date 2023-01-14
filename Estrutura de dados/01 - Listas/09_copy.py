# A lista é um objeto mutavel
# O copy vai retornar a mesma lista com uma "instancia" - código de registro diferente
listas = [1, "Python", [40, 30, 20]]

l2 = listas.copy()

print(listas)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(listas)) # Exibem dois códigos diferentes apesar de serem as mesmas listas

#Caso altere em uma lista a outra não será alterada
l2[0] = 69

print(l2) # No ponto 0 esse irá receber 69
print(listas) # Esse irá permanecer o mesmo valor


