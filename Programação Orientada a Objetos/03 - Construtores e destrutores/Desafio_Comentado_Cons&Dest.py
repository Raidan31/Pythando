#Metodo construtor(__init__) é sempre utilizado para adicionar nova instância da classe
#init é executado no inicio
class Cachorro: 
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando Classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

#Metodo destrutor(__del__) é sempre utilizado para destruir uma instância é destruida
#Não é tão utilizado, pois o python tem coletor de lixo para desalocar memoria automaticamente 
#del é executado no final

    def __del__(self):
        print("Destruindo instância")

    def latir(self):
        print("Au au")


def criar_cachorro():
    c = Cachorro("Apolo", "Branco", False)
    print(c.nome)

#c = Cachorro("Bolt", "preta")

#c.latir()

criar_cachorro()