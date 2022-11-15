'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Para executar este script, escrever no Terminal:
# uvicorn main:app --reload

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Criação de uma aplicação FastAPI
app = FastAPI()

class Item(BaseModel):
    '''Uma classe Item e dentro (BaseModel) a classe pai'''
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    '''Função de bem-vinda.'''
    return "Olá a todos! estou usando FastAPI!!!"

@app.get("/items/{item_id}") # https://fastapi.tiangolo.com/#check-it
def read_item(item_id: int, q: Union[str, None] = None):
    '''Função de'''
    return {"item_id": item_id, "q": q}

@app.get("/calculadora")
def calcular(operando_1: float, operando_2: float):#.../calculadora?operando_1=2&operando_2=5
    '''Soma de dois números.'''
    return {'soma': operando_1 + operando_2}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    '''Função de Itens.'''
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
