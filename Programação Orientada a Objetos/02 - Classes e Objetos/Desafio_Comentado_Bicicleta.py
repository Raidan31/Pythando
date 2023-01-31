#Aqui foi declarada a classe da bicicleta
#init serve como iniciador
# Classes definem características e comportamentos de um objeto. O objeto representa uma instância concreta da classe.  
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18):
#Atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro #novo atributo

# Metodos
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

#Metodo Manual:
#No metodo manual teria que adicionar a mão cada alteração nos atributos, aqui foi necessário adicionar o novo atributo aro

    #def __str__(self):
        #return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}, aro = {self.aro} "
                                                                                                               #novo atributo 
#Metodo automatico
#No metodo automatico será necessário apenas adicionar um atributo na class
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
                                                  #join concatenou as strings                            #dict retorna um dicionário
                                                                                                    #para interar tem que usar o items                          




#self.cor etc são os atributos da classe
#Self é uma referencia explicita ao objeto
#Self é a instância do objeto que foi passado
#Self não é obrigatório porem é uma convenção 
#Declaração dos metodos 
#metodos são funções definidas em uma classe
#Self é um argumento/atributos dentro dos metodos q deve ser definido 



b1 = Bicicleta("vermelho", "caloi", 2022, 600) 
b1.buzinar()
b1.correr() 
b1.parar()

#Acessando os atributos

#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
#b2 é argumento posicional é o self
#Aqui vai imprimir a buzina para a b2
#Bicicleta.buzinar(b2) #==b2.buzinar()
print(b2)


    
     
     
     
