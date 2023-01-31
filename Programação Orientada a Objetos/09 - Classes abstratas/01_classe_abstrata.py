# Interfaces definem o que uma classe deve fazer e não como
# Classes Abstratas não podem ser instânciadas
# O python não fornece classes abstratas, então utilizamos o modulo ABC
from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    # Metodo abstrato uma vez que se tem um metodo abstrato a classe não pode ser instanciada diretamente 
    @abstractmethod
    def ligar(self): # Metodo padrão
        pass
    
    # Metodo abstrato
    @abstractmethod
    def desligar(self):# Metodo padrão
        pass

    @property
    @abstractproperty #É possivel forçar uma propriedade nas classes abstratas 
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property # Decoração 
    def marca(self):
        return "Philco"

# Todas as classes que implementarem os metodos abstratos terão que implemetar no mesmo padrão
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...") 
        print("Ligado!") 

    def desligar(self):
        print("Desligando o Ar Condicionado...") 
        print("Desligado!") 

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
