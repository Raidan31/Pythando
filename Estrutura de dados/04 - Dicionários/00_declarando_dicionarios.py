# Conjunto não ordenado de pares chave:valor
#Não pode usar valores mutaveis tipo listas
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

#O dicionário não permite que se repita chaves 

#dicionario = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5} 
#O dicionario trabalha com o conceito de chave e valor

#print (dicionario)
#print (dicionario["Maçã"]) #Demonstra o valor que está armazenado em Maçã

#dicionario["Maçã"] = 25 #Modificou o valor de Maçã para 25

#print (dicionario["Maçã"]) #Valor 25 da Maçã

#print (dicionario.keys()) #Imprime as chaves do dicionário

#print (dicionario.values()) #Imprime os valores do dicionário

#Verifica se já existe uma chave no dicionário e caso não exista irá inserir no dicionário
#print(dicionario.setdefault("Limão", 22))

#print(dicionario)