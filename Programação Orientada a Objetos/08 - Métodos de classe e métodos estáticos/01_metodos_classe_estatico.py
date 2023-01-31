# Um metodo de classe recebe um primeiro parametro que aponta para a classe, enquanto um metodo estatico não
# Um metodo de classe pode acessar ou modificar o estado da classe enquanto um metodo estatico não poode acessa-lo ou modifica-lo

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # Os metodos de classe estão ligados a classe e não ao objeto.
                 # Pois recebem um parametro que aponta para a classe e não para a instância do objeto.
                 # Metodo de Fabrica precisa de acesso do contexto da classe

    def criar_de_data_nascimento(cls, ano, mes, dia, nome): #cls vai substituir o self quando se tratar de metodo de classe
                                                            # cls é a instância para a classe 
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod # O metodo de estático não recebe o primeiro argumento explícito
                  # Tambem é um metodo vinculado a classe e não ao objeto de classe
                  # Funções Utilitárias não precisa de acesso ao contexto da classe ou da instância do objeto

    def e_maior_idade(idade):
        return idade >= 18

# classe pessoa + metodo de classe 
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

# Metodo estatisctico 
print(Pessoa.e_maior_idade(18)) 
print(Pessoa.e_maior_idade(8))
