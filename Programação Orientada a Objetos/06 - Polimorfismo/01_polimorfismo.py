#Poliformismo com herança as classes filhas recebem os metodos da classe pai
#contudo a classe filha não é obrigada a receber caso não seja compativel

class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro): 
    def voar(self):#Avestruz não voa ou seja não precisa receber o metodo voar do passaro (classe pai)
        print("Avestruz não pode voar") 

# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()

#Passando a instancia para o plano de voo
#Em cada uma delas o voa irá se comportar de forma diferente 
#Todas com voar, mas se comportam de forma diferente
plano_voo(Pardal()) 
plano_voo(Avestruz())
plano_voo(Aviao())
