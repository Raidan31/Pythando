#Herança é a capacidade de uma classe filha herdar as caracteristicas e os comportamentos da classe pai.
#Herança Simples, a classe filha herda apenas de uma classe pai

#Veiculo é a classe Pai, neste exemplo
class Veiculo:
    def __init__ (self, cor, placa, numero_de_rodas):
        self.cor = cor 
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

#Comportamentos
    def ligar_motor(self):
        print("Ligando Motor")
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#Motocicleta e as demais são classes filho que herdam de veiculo
class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass

#O estar carregado é algo especifico para o caminhão
#não será herdado para as outras classes filhas 
class Caminhão(Veiculo):
    def __init__(self,cor, placa, numero_de_rodas, carregado):
        self.carregado = carregado
        #super invoca o metodo da classe pai
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado


    def estar_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

#Aqui será obrigado a herdar os atributos descritos na classe pai(cor, placa, numero_de_rodas)
#moto = Motocicleta("Preta", "dkg - 3456", "2 rodas" )
#moto.ligar_motor()

#carro = Carro("Branco", "abc-3245", "4 rodas")
#carro.ligar_motor()
                    #Está posição deve ser igual a das características
caminhão = Caminhão("Roxa", "dse - 4589", "8 rodas", True)
caminhão.ligar_motor()
caminhão.estar_carregado()
print(caminhão)