#Todos os objetoss nascem com os mesmos numeros de atributos de classe e de instância 
#Atributos de instância são diferentes pra cada objeto (cada objeto tem uma cópia)
#já os atributos de classe são compartilhados entre os objetos

#Variavel de classe
class Estudante:
    escola = "DIO" #dinamicamente tipado
    #Atibuto escola é compartilhado com aluno 1 e 2 com as variaveis que armazem a instância de estudante
#Variaveis de instância 
    def __init__(self, nome, matricula):
        self.nome = nome #Self é o que identifica o qque é instância
        self.matricula = matricula

    def __str__(self) -> str: # Pra poder verificar os dados
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
