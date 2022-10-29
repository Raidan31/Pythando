# While é utilizado quando não souber o numero maximo de repetições

opçao = -1

while opçao != 0:
    opçao = int(input(" [1] Sacar \n [2] Extrato \n [3] Sair \n: "))

    if opçao == 1:
        print ("Sacando...")
    elif opçao == 2:
        print ("Exibindo o extrato")

else:
    print("Obrigado por utilizar nossos serviços")