#Recebe apenas o valor sem ser nomeado / só recebe quando forem nomeados
#Hibrido
def criar_carro(modelo, ano, placa, /,*, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#Valores por posição sem nomeação "Palio", 1999, "ABC-1234",/ com nomeação marca="Fiat", motor="1.0", combustivel="Gasolina
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Esse aqui da erro por terem parametros por nomeação antes da barra ex: modelo="Palio", ano=1999, placa="ABC-1234
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
