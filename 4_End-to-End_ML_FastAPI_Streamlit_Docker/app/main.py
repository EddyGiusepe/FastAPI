"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro
"""

"""
Criando uma API com FastAPI
===========================

Executamos assim:

$ uvicorn main:app --reload
ou
$ python main.py
"""

from fastapi import FastAPI
import joblib
import uvicorn
import numpy as np
import pandas as pd


app = FastAPI(title='🤗 Machine learning: Regressão Linear para previsão de preço do carros 🤗',
              version='1.0',
              description="""Data Scientist.: PhD. Eddy Giusepe Chirinos Isidro\n
              Projeto de aprendizado de máquina end-to-end para prever os preços de carros.""")


model = joblib.load("../model/LinearRegressionModel.pkl")


"""
A classe 'BaseModel' é a classe base que você pode estender para
criar suas próprias classes de modelo de dados com base em pydantic.

A biblioteca pydantic oferece uma maneira fácil e robusta de validar e
trabalhar com dados em seu código Python.
"""
from pydantic import BaseModel

class Data(BaseModel):
    name: str
    company: str
    year: int
    kms_driven: float
    fuel_type: str


# Criamos nossa EndPoint inicial ou chamada também root (raíz):
@app.get('/')
@app.get('/home')
def read_home():
    """
    Endpoint inicial que pode ser usado para testar a disponibilidade do aplicativo..
    """
    return {'message': 'O sistema está saudável.'}


# Criamos uma endpoint de API de ML para prever a solicitação (request) recebida do cliente:
@app.post("/predict")
def predict(data: Data):
    result = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                        data=np.array([data.name, data.company, data.year, data.kms_driven, data.fuel_type]).reshape(1,5)))[0]
    return result







if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    