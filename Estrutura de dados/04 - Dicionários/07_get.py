#Metodo GET serve para buscar uma chave no dicionário, se não achar é equivalente retorna None
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#contatos["chave"]  # KeyError esse erro ocorre pois a chave não existe no dicionário

resultado = contatos.get("chave")  # None
print(resultado)

#É possivel configurar para que retorne outro resultado em vez de none
#Foi configurado para retornar {}
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
