#Python não tem regra para encapsulamento
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
# \t afasta os objetos pessoa.nome e pessoa.idade
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
