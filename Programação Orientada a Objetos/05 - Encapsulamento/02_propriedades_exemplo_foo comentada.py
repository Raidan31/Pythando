# Por meio do property é possivel modificar implementação interna sem alterar a API publica da classe   

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property  #Decorador pega o valor de x se existir senão retorna 0
    #NÃO É UM METODO É UM ATRIBUTO
    def x(self):
        return self._x or 0

    @x.setter #pega o valor de x se existir senão retorna 0, com o valor de x trabalha com um outro valor
    def x(self, value):
        self._x += value # valor de x + outro valor 

    @x.deleter #Pega o X e transforma em outro valor 
    def x(self):
        self._x = 0 #Pega o X e transforma em 0
        #del self.x #apaga o _x


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
