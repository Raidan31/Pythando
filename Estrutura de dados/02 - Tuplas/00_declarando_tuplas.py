#As truplas são estruturas imutaveis diferente da lista 
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas) 

letras = tuple("python") #tuple serve para criar tuplas
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) 
# A virgula no final serve para não confudir o python pois pode confundir com uma operação
print(pais)
