#If ternario permite escrever uma expressão em uma unica linha
#É composto por tres partes:
# 1 - Retorno caso a expressão volte verdadeira (antes do if)
# 2 - Expressão Logica (if) 
# 3 - Retorno caso a expressão não seja atendida (else)

saldo = 1000
saque = 1500

status = "Sucesso" if saldo >= saque else "Falha"

print (f"{status} ao realizar o saque")
