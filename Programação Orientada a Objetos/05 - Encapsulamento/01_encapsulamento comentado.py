#Recurso Publico todos podem acessar
#Recurso Privado só autorizados podem acessar,
# porem não existe limitação de acesso no python apenas é convencionado o uso do underline no inicio 

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # O underline no inicio do saldo é uma convenção que indica que o saldo é um recurso privado
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # saldo mais(+=) o valor
        self._saldo += valor

    def sacar(self, valor):
        # saldo menos(-=) o valor
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
