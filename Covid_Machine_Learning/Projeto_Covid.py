#!/usr/bin/env python
# coding: utf-8

# # Projeto Covid-19
# 
# ## Digital Innovation One
# 
# Primeiro importar bibliotecas

# In[1]:


import pandas as pd


# Pandas são os dataframes/datasets que serão usados

# In[2]:


import numpy as np


# Numpy serve para realizar os calculos cientifícos

# In[3]:


from datetime import datetime


# É necessário importar o datetime para trabalhar com datas

# In[4]:


import plotly.express as px


# plotly.express é a biblioteca para visualização

# In[5]:


import plotly.graph_objects as go


# plotly.graph_objects serve para suprir as limitações graficas do plotly.express

# In[6]:


url = 'https://github.com/neylsoncrepalde/projeto_eda_covid/blob/master/covid_19_data.csv?raw=true'


# A url são os dados do projeto em questão

# In[7]:


df = pd.read_csv(url, parse_dates = ['ObservationDate', 'Last Update'] )
df


# df está armazenando os dados da url. pd.read_csv é uma ferramenta da biblioteca pandas. parse_dates foi utilizado para transformar as colunas Observation Date e Last Update no formato Data

# In[8]:


#df.dtypes confere os tipos de cada coluna

df.dtypes


# Nomes de colunas não devem ter letras maiusculas nem caracteres especiais. Vamos implementar uma função para fazer a limpeza dos nomes dessas colunas.

# In[9]:


# re de Regular expressions para corrigir as colunas
import re
    
def corrige_colunas(col_name):
    return re.sub(r"[/| ]", "", col_name).lower() 

# sempre que houver / ou tiver espaço irá retornar sem barra e sem espaço e minuscula


# In[10]:


corrige_colunas("Ra/i D a n")

#exemplo do que foi feito


# In[11]:


#Correção de todas as colunas do dataframe

df.columns # Retorna as colunas do data frame


# In[12]:


#Atribuição do df.columns ao uma lista compreensivel por meio de um for loop

df.columns = [corrige_colunas(col) for col in df.columns] 


# In[13]:


df


# ## Trabalhando com o Brasil
# 
# Vamos selecionar apenas os dados do Brasil para investigar

# In[14]:


#Filtrando apenas pelo Brasil 

df.loc[df.countryregion == "Brazil"] 


# In[15]:


df.countryregion.value_counts() 


# In[16]:


df.countryregion.unique() #Mostra apenas os paises


# In[17]:


df.loc[df.countryregion == "Brazil"] 


# In[18]:


#Condição para receber apenas os dados do Brasil com casos maiores que 0 confirmados 
Brasil = df.loc[
        (df.countryregion == "Brazil") &
        (df.confirmed > 0)
    
] 


# In[19]:


Brasil


# # Casos confirmados

# In[20]:


#Grafico da evolução de casos confirmados

px.line(Brasil, 'observationdate', 'confirmed', title='Casos Confirmados no Brasil')


# ## Novos Casos por Dia

# In[21]:


# Tecnica de Programação Funcional
# Criação da coluna novos casos

Brasil["novoscasos"] = list(map(
    lambda x: 0 if (x==0) else Brasil["confirmed"].iloc[x] - Brasil["confirmed"].iloc[x-1],
    np.arange(Brasil.shape[0])
)) 
#Traduzindo - Se for o primeiro caso, retorna zero. A partir do segundo caso, faz hj menos ontem. Vai ser aplicado no np.arange
#brasil.shape = retorna as dimenções do dataframe linhas e colunas, o (0) serve pra pegar apenas as linhas
# i.loc faz subsete de colunas pelo indice 
#Cria uma nova coluna novos casos
#lambda é uma função anonima - função sem nome
# map retornar um inteirador por isso foi necessário utilizar o list pois a saida do map será coagida no list


# In[22]:


Brasil


# In[23]:


px.line(Brasil, x= "observationdate", y="novoscasos", title = "Novos Casos por Dia") 


# # Mortes

# In[24]:


fig = go.Figure()

fig.add_trace(
    go.Scatter(x=Brasil.observationdate, y=Brasil.deaths, name='Mortes', mode='lines+markers',
              line=dict(color='red'))
)
#Edita o layout
fig.update_layout(title='Mortes por COVID-19 no Brasil',
                   xaxis_title='Data',
                   yaxis_title='Número de mortes')
fig.show()

# trace é uma camada de dados
# Scatter consegue fazer linhas e colunas


# # Taxa de Crescimento
# 
# taxa_crescimento = (presente/passado)**(1/numero de dias) - 1

# In[25]:


def taxa_crescimento (data, variable, data_inicio = None, data_fim = None):
    # Se a data inicio for None, define como a primeira data disponivel 
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0 ].min() 
        # vai definir o valor minimo referente a variavel maior q zero
    else:
        data_inicio = pd.to_datetime(data_inicio) #passa data inicio como texto

    if data_fim == None:
        data_fim = data.observationdate.iloc[-1] # -1 PRA PEGAR O ULTIMO CASO
    else: 
        data_fim = pd.to_datatime(data_fim)
    
    #Definir os valores do presente e do passsado
    
    passado = data.loc[data.observationdate == data_inicio, variable].values[0]
    presente = data.loc[data.observationdate == data_fim, variable].values[0]
    
    #Definir o numero de pontos no tempo que serão avaliados
    
    n = (data_fim - data_inicio).days #.days para retornar o numero de dias
    
    # Calculara a taxa
    
    taxa = (presente/passado)**(1/n) - 1
    
    return taxa*100


# # Taxa de Crescimento Médio de Covid no Br em todo o periodo

# In[26]:


taxa_crescimento(Brasil, 'confirmed')


# In[27]:


def taxa_crescimento_diaria(data, variable, data_inicio=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
        # vai definir o valor minimo referente a variavel maior q zero
        
    else:
        data_inicio = pd.to_datetime(data_inicio) #passa data inicio como texto
        
    data_fim = data.observationdate.max()
    
    #Definir o numero de pontos no tempo que serão avaliados
    
    n = (data_fim - data_inicio).days #.days para retornar o numero de dias
    
    #Taxa calculada de um dia para o outro
    
    taxas = list(map(
        lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / data[variable].iloc[x-1],
        range(1,n+1) # range recebe 1 pq o 0 não aprensenta nenhum caso 
    
    ))
    return np.array(taxas)*100


# In[28]:


tx_dia = taxa_crescimento_diaria(Brasil, 'confirmed')


# In[29]:


tx_dia


# In[30]:


primeiro_dia = Brasil.observationdate.loc[Brasil.confirmed > 0].min()

px.line(x=pd.date_range(primeiro_dia, Brasil.observationdate.max())[1:],
        y=tx_dia, title="Taxa de Crescimento de Crescimento de Casos no BR",
        labels={'y':'Taxa de crescimento', 'x':'Data'})


# # Predições
# 
# Vamos construir um modelo de séries temporais para prever os novos casos. Antes analisemos a série temporal.

# In[31]:


from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


# In[32]:


confirmados = Brasil.confirmed #Serviu para pegar as datas e tranformar como indice do confirmados
confirmados.index = Brasil.observationdate
confirmados


# In[33]:


# Decomposição da serie dos confirmados
res = seasonal_decompose(confirmados)


# In[34]:


fig, (ax1, ax2, ax3, ax4) = plt.subplots (4, 1, figsize = (10, 8))
# Quatro eixos, 4 linhas e 1 coluna, tamanho 10 altura e 8 de largura

ax1.plot(res.observed)
ax2.plot(res.trend)
ax3.plot(res.seasonal)
ax4.plot(confirmados.index, res.resid)
ax4.axhline(0, linestyle='dashed', c='black')
plt.show()


# # ARIMA - Modelo Autorregressivo Integrado de Médias Móveis

# In[35]:


get_ipython().system('pip install pmdarima')


# In[36]:


from pmdarima.arima import auto_arima
modelo = auto_arima(confirmados) 


# In[37]:


fig = go.Figure(go.Scatter(
    x=confirmados.index, y=confirmados, name='Observed'
))

fig.add_trace(go.Scatter(x=confirmados.index, y = modelo.predict_in_sample(), name='Predicted'))

fig.add_trace(go.Scatter(x=pd.date_range('2020-05-20', '2020-06-05'), y=modelo.predict(15), name='Forecast'))

fig.update_layout(title='Previsão de casos confirmados para os próximos 15 dias',
                 yaxis_title='Casos confirmados', xaxis_title='Data')
fig.show()


# # Modelo de Crescimento
# 
# ## Biblioteca fbprophet

# In[38]:


#Instalação da biblioteca fbprophet

get_ipython().system('conda install -c conda-forge fbprophet -y')


# In[ ]:


from fbprophet import Prophet


# In[ ]:


#Pré Processamentos necessários para trabalhar com fbprophet

train = confirmados.reset_index()[:-5] #Vai ficar duas colunas - Do inicio até os 5 ultimos
test = confirmados.reset.index()[-5:] # Dos 5 ultimos até o final

#Renomeando Colunas - Exigencia da Biblioteca

trai.rename(columns={'observationdate' : 'ds', 'confirmed': 'y'}, inplace = True)
test.rename(columns={'observationdate' : 'ds', 'confirmed': 'y'}, inplace = True)

# Definir o modelo de crescimento 

profeta = Prophet(growth='logistic', changepoints = ['2020-03-21', '2020-03-30', '2020-04-25',
                                                    '2020-05-03', '2020-05-10' ])

# Modelo será com base na contaminação de toda a população brasileira
pop = 211463256
train['cap'] = pop

# Treinar o modelo - .fit(train) - Deve fica após as definiçõe de limite 'cap'

profeta.fit(train)

# Construir previsõe para o futuro

future_dates = profeta.make_future_dateframe(periods = 200)
future_dates['cap'] = pop
forecast = profeta.predict(future_dates)


# # Grafico - fbprophet

# In[ ]:


fig = go.Figure()

fig.add_trace(go.Scatter(x = forecast.ds, y = forecast.yhat, name = 'Predição'))
fig.add_trace(go.Scatter(x = train.ds, y = train.y, name = 'Obsservados - Treino'))
fig.update_layout(title = 'Prediçõe de Casos Confirmados no Brasil')
fig.show()


# In[ ]:




