#Comando for serve para Objeto iteravel.
#E pra quando souber o numero exato de vezes que o bloco de código deve ser executado.
#Ou pra quando quiser percorrer um objeto iteravel.

texto = input ("Informe o texto: ")
VOGAIS = "AEIOU" #O limitador sobre de o quanto irá percorrer

for letra in texto:
    if letra.upper() in VOGAIS: # verifica se a variavel letra esta dentro das vogais
        print(letra, end="")
else: #for e Else são compativeis, igual ao if
    print()#Adiciona quebra de linha 
    print("Executar ao fim do laço")



