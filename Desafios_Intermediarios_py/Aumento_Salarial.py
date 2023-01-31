salario = 1120


if  salario >= 0 and salario <= 600:
    reajuste = (salario * 0.17) 
    novo_salario = reajuste + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 17 %")

elif salario > 600 and salario <= 900:
    reajuste = (salario * 0.13)
    novo_salario = reajuste + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 13 %")

elif salario > 900 and salario <= 1500:
    reajuste = (salario * 0.12)
    novo_salario = reajuste + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 12 %")

elif salario > 1500 and salario <= 2000:
    reajuste = (salario * 0.10)
    novo_salario = reajuste + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 10 %")


else:
    reajuste = (salario * 0.5)
    novo_salario = reajuste + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 5 %")




