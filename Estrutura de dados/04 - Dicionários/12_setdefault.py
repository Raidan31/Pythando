#Apenas adiciona valores quando não houver uma chave correspondente
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

#Não foi adicionado pq já nome já recebia Guilherme
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

#Aqui foi adicionado pq idade não existia
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
