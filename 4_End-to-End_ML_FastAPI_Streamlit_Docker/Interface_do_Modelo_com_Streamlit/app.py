"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro


Criando uma interface web para o modelo de previsão de carros com Streamlit
===========================================================================

Executamos assim:

$ streamlit run app.py
"""

import pandas as pd
import streamlit 

df = pd.read_csv("../cleaned_car_data.csv")


def run():
    streamlit.title("🤗 Machine learning: Regressão Linear para previsão de preço do carros 🤗")
    name = streamlit.selectbox("Selecione o modelo do carro", df.name.unique())
    company = streamlit.selectbox("Selecione o nome da companhia", df.company.unique())
    year = streamlit.number_input("Ano do carro")
    kms_driven = streamlit.number_input("Quilômetros percorridos")
    fuel_type = streamlit.selectbox("Tipo de combustível", df.fuel_type.unique())


# Vamos armazenar os dados que recebemos do usuário através da interface na variável 'data'.
    data = {
        'name': name,
        'company': company,
        'year': year,
        'kms_driven': kms_driven,
        'fuel_type': fuel_type,
        }







if __name__ == '__main__':
    run()
