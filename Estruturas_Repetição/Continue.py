#for numero in range(30):

    #if numero == 10: # Pula o 10 e continua a contar
    #    continue 

    #print (numero, end=" ")


while True: #looping ifinito
    numero = int(input("Informe um numero!: "))

    if numero % 2 == 0:
       continue  #só vai exibir numero impar

    print (numero)