#É possivel ter IF dentro de IF



conta_normal = False
conta_universitaria = False

    
saque = 500

cheque_especial = 1000
saldo = 2000

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso! ")
    if saque == (saldo + cheque_especial):
        print ("Saque realizado com cheque especial")
    else:
        print ("Limite insuficiente! O saque não será realizado")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso! ")
    else:
        print ("Saldo Insuficiente!")
else: 
    print ("Sistema não reconheceu o tipo de conta")