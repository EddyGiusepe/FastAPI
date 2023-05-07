"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro

https://medium.com/@furkankizilay/end-to-end-machine-learning-project-using-fastapi-streamlit-and-docker-6fda32d25c5d


Criando uma interface web para o modelo de previsão de carros com Streamlit
===========================================================================

Neste script criamos a Interface de nosso Modelo de Machine Learning, com streamlit.
Repara que depois de instanciar esta Interface Web em Streamlit você deve instanciar, também, o 
script 'main.py' do fastAPI.

Executamos assim:

$ streamlit run app.py
"""

import pandas as pd
import requests
import streamlit 
import json


df = pd.read_csv("/home/eddygiusepe/1_Eddy_Giusepe/FastAPI/4_End-to-End_ML_FastAPI_Streamlit_Docker/cleaned_car_data.csv")


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

# Quando o botão "Predict" é clicado, obtemos os resultados do nosso modelo usando a
# API que criamos com a ajuda de "request".
    if streamlit.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        prediction = response.text
        streamlit.success(f"A predição do Modelo: {prediction}")






if __name__ == '__main__':
    # Por padrão, ele será executado na porta 8501
    run()
