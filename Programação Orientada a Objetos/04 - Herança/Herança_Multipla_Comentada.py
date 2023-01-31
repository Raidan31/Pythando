#Herança é a capacidade de uma classe filha herdar as caracteristicas e os comportamentos da classe pai.
#Herança Multipla, a classe filha herda de varias classes pai
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    #**kwargs foi necessário para que as classes pais(mamifero e oviparo) recebessem a construção do avô numero de patas
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Oviparo(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

#A classe gato está herdando tudo o que foi colocado em mamifero e animal
class Gato(Mamifero):
    pass

#A classe onitorrinco está herdando de todas as classe com exceção da do gato
class Ornitorrinco(Mamifero, Oviparo):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        #__mro__ é a priorização da impressão das instâncias em STS])
        print(Ornitorrinco.__mro__)
        #super chamando a classe pai
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

    def __str__(self):
        return "Ornitorrinco"



#Com o ** kwargas fooi necessário tornar os argumetos abaixo em nomeados ex:nro_patas=4
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)
#Aqui tbm foi necessári nomear os argumentos
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)


   