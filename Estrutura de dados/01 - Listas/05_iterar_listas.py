carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): #Indice para percorrer a lista
    print(f"{indice}: {carro}")
