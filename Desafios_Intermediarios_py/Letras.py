#RESPOSTAS QUE EU CHEGUEI

#from string import ascii_uppercase
#alphabet = list(ascii_uppercase)
#letra = "C"
#adicional = int(alphabet.index(letra)) + 1
#print(adicional)

# Versão melhorada 

letter = "a"
position = ord(letter) - ord('A') + 1
# função ord() do Python para obter a posição da letra no alfabeto
print(position)