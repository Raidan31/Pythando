#Elif é utilizado para situações que exijam mais de dois desvios. 
#Elif é composto por mais uma expressão lógica e caso retorne verdadeira será executado.
#Não existe limite maximo de ELIF's

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print ("Maior de Idade, pode tirara a CNH")

elif idade == IDADE_ESPECIAL:
    print ("Pode fazer aula teórica")

else:
    print ("Não pode tirar carteira e nem fazer aula teórica")





