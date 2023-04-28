"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro

Método Novo
===========
Por outro lado, a mesma lógica pode ser implementada usando o evento 'lifespan' da seguinte forma:

$ uvicorn main_2:app --reload
"""
import random
from contextlib import asynccontextmanager

from fastapi import FastAPI

sentiments = ["positive", "neutral", "negative"]


def fake_answer(text: str):
    return random.choice(sentiments)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    app.state.models = {}
    app.state.models["sentiment_analysis"] = fake_answer
    yield
    # shutdown
    app.state.models.clear()
    sentiments.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(text: str = "Olá Mundo!"):
    result = app.state.models["sentiment_analysis"](text)
    return {"text": text, "result": result}

"""
O evento de vida útil (lifespan) depende do decorador 'asynccontextmanager' para adicionar
o gerenciador de contexto assíncrono a uma função. Basta importá-lo da seguinte forma:

                    from contextlib import asynccontextmanager

Continue decorando uma função 'asynccontextmanager' e implementando a lógica desejada com base na seguinte sintaxe:                    

                    @asynccontextmanager
                    async def lifespan(app: FastAPI):
                        # startup logic before yield statement
                        yield
                        # shutdown logic after yield statement

Depois disso, passe a função 'lifespan' como argumento de entrada durante a instanciação FastAPI.  

                    app = FastAPI(lifespan=lifespan)


Avançando, o evento 'lifespan' é o método recomendado para lógica de inicialização e desligamento.
Na versão futura, FastAPI terá suporte para 'state', que pode ser usado para compartilhar os objetos
entre 'lifespane' e 'requests'.                                        
"""