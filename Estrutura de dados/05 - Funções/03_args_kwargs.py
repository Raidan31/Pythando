#Os valores de args vão vir como uma tupla
#kargs vai vir como um dicionário

#função exibir_poema(recebe três argumentos)
#Os nomes *args e **kwargs são desncessário só serão relevantes os asterisco
def exibir_poema(data_extenso, *args, **kwargs):
    #pega todos os valores(join) com o args e concatena com o /n ==(um em cada linha) 
    texto = "\n".join(args)
    #recebe os valores do kwargs coloca o .itens pq o kwargs é um dicionário
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Quinta-feira, 12 de janeiro de 2023",# Data por extenso
    "Zen of Python",#Daqui em diante é considerado args e será exibido na forma de tuplas
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",#Até aqui é args
    autor="Tim Peters",#Daqui até o fim é kwargs
    ano=1999,
)
