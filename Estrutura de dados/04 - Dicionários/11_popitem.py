#A diferença é que não informa a chave 
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
          
}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

contatos.popitem()  # KeyError pq o dicionário está vazio
