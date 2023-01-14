contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
#Nova variavel recebe a variavel com os dados chave inicial e a chave interna que queira acessar
# Dicinário dentro de um dicionário 
#Email é a chave para o dicionário interno 
telefone = contatos["giovana@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)
