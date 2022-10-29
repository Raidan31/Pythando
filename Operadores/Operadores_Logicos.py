
saldo = 1000
saque = 250
limite = 200

print (saldo >= saque and saldo <= limite) # Todas as expressões devem voltar a resposta verdadeira caso contrario será Falso


print (saldo >= saque or saldo <= limite) # Necessita de apenas uma expressão seja verdadeira para retornar verdadeiro.


print (not saldo > saque) #not inverte o resultado o que era pra dar True da False

contas = [] # Isso e uma lista e o python considera a sua resposta como false
print(not contas) # Usando o Not ela se torna True

print (not "Saque 1000") # A string é considerada True pelo Python com Not é invertida

print (not "") #Uma string VAZIA é considera False pelo Python

conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print (exp)








