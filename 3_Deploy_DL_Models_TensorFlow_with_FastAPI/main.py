"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro


FastAPI para instanciar nosso Modelo com TensorFlow
===================================================
Para executar o código FastAPI Swagger-UI, assim:

$ uvicorn main:app --reload
"""
import tensorflow as tf
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


MODEL = tf.keras.models.load_model('./model')

app = FastAPI()


class UserInput(BaseModel):
    user_input: float


@app.get('/')
async def index():
    return {"Mensagem": "Este é um index! Você já está no Swagger-UI 🤗"}

@app.post('/predict/')
async def predict(UserInput: UserInput):
    
    prediction = MODEL.predict([UserInput.user_input])
    return {"prediction": float(prediction)}
