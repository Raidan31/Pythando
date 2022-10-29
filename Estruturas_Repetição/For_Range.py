#Usada para produzir uma sequencia de numero inteiros
#Inicio (Inclusivo)
#Fim (Exclusivo)
#Ela recebe 3 argumentos:
# 1 - Stop (Obrigatório)
# 2 - Star (Opcional)
# 3 - Step (Opcional) - De quanto em quanto vai contar 

for numero in range(0, 11): # O 11 será excluído da contagem (fim exclusivo)
    print(numero, end=" ") # end=" " esta dando os espaçamento entre os numeros.
else:
    print (""" 
    """)
#Tabuada do 5

for numero in range (0, 51, 5):
    print (numero, end=" ")

