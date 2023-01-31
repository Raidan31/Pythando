
opção = input("Informe o estado da perna do papagaio (Esquerda, Direita Levantada, Ambas, Nenhuma): ")

if opção.lower() == "esquerda":
    print("O papagaio vai falar em inglês")

elif opção.lower() == "direita levantada":    
    print("O papagaio vai falar em espanhol.")

elif opção.lower() == "ambas":    
    print("O papagaio vai cair")

elif opção.lower() == "nenhuma":    
    print("O papagaio vai falar em português")
else:
    print("Opção Inválida")
