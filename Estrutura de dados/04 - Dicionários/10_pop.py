#Remove uma chave do seu dicionário
#Remove e retorna a chave que ele removeu
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
            "bananina123@yahoo": {"nome": "Banonio", "telefone": "6969-6969"}
}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "não encontrei")  
# "não encontrei" serve como o resultado caso a chave seja removida
# não atribuir um valor após a remoção da chave irá causar um errro
# ou seja, se remover esse "não encontrei" vai dar erro
print(resultado)
print(contatos) #Aqui demonstra que apenas o bananinha sobrou