#Elif é utilizado para situações que exijam mais de dois desvios. 
#Elif é composto por mais uma expressão lógica e caso retorne verdadeira será executado.
#Não existe limite maximo de ELIF's

opção = int(input
("""Informe a opção:
                    
                    1 - Sacar
                    
                    2 - Extrato

 """))

if opção == 1:
    valor = float(input("Informe a quantia para saque: "))

elif opção == 2:    
    print("Exibindo Extrato....")

else:
    print("Opção Invalida")


