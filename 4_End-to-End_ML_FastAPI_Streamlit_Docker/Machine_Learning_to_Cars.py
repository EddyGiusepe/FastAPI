"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro
"""

"""
Deploy de um Modelo de Machine Learning para prever preços de carros
====================================================================

Este script foi baseado no tutorial da Medium do cientista Furkan Kizilay.
Ele aborda este estudo em 11 passos:
* Carregamento de dados
* Engenharia de feature
* Limpeza de dados
* Remoção de Outliers
* Visualização de dados (relação entre variáveis)
* Extraindo dados de treinamento
* Encoding
* Construir o modelo
* Criar API com FastAPI
* Criar uma interface web para o modelo com Streamlit.
* Dockerizamos
"""
"""
Carregamento de dados
=====================
"""
import pandas as pd

df = pd.read_csv("./cars.csv")
print(df.head())
print(df.shape)

"""
Feature Engineering
===================
"""
# Adicionamos uma nova feature --> nome da empresa ("company")
df["company"] = df.name.apply(lambda x: x.split(" ")[0])
print(df.head())

"""
Limpeza de dados
================
"""
# Observamos que a SÉRIE --> "year" tem valores que não são anos (year). Vamos eliminar eles:
print(df["year"].value_counts())
print(df["year"].unique())
print("Verificamos o Type: ", type(df["year"].iloc[0]))

# Trabalhamos com uma copia:
df2 = df.copy()
df2 = df2[df2["year"].str.isnumeric()] # True, se todos os carateres da string forem numéricos.
df2["year"] = df2["year"].astype(int) # Convertemos a Inteiro.

print("Vejamos novamente: ", df2["year"].unique())

# Eliminamos na coluna/série "Price" a palavra: Ask For Price, assim:
df2 = df2[df2["Price"] != "Ask For Price"]
print(df2.Price)
# Fazemos os reset do index:
df2 = df2.reset_index(drop=True)
print(df2.head())

# Vejamos o método .info():
print(df2.info())

# A coluna Price tem vírgulas em seus preços e está como object:
df2.Price = df2.Price.str.replace(",","").astype(int) # No final converte para Inteiro.
print(df2.head())
