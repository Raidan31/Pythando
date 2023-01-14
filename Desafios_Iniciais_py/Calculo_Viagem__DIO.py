tempo_velocidade = input().split()
tempo  = int(tempo_velocidade[0])
velocidade  = int(tempo_velocidade[1])

km_litro = velocidade / 12
resultado = tempo * km_litro

print(f"{resultado:1.3f}")