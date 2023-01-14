#O python trabalha com escopo local e global dentro do bloco da função o escopo é local
# Para usar objetos globais a palavra reservada é "global"
salario = 2000


def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")
    
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = (f"O salário com bonus será =  {salario_bonus(500, lista)}")
print(salario_com_bonus)
print(lista)