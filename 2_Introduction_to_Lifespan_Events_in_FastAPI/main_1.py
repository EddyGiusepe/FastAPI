"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro


Introdução aos eventos de tempo de vida no FastAPI
==================================================
Nova implementação para lógica de inicialização e desligamento está baseado no Tutorial
do Engenheiro Sênior: Ng Wai Foong.

Aqui vamos aprender a implementar eventos de tempo de vida em nosso FastAPI
para lógica de inicialização e desligamento. A partir da versão 0.93.0, o módulo
fastapi suporta oficialmente o evento lifespan, que substitui os eventos startup e shutdown.

**os eventos de inicialização e desligamento serão obsoletos na versão futura.**

Uma das principais vantagens do evento de vida útil é que toda a lógica pode ser implementada
em uma única função. Além disso, o código para os eventos 'startup' e 'shutdown' deve ser
implementado após a inicialização da instância FastAPI.

O evento 'lifespan' simplifica todo o processo por ter apenas uma única função que deve ser
declarada antes da instanciação FastAPI.

🧐 Vejamos as diferenças 🧐
"""
"""
Método Antigo
-------------
O seguinte código usa os eventos 'startup' e 'shutdown' para inicialização do modelo.

Executamos assim:

$ uvicorn main_1:app --reload
"""
import random
from fastapi import FastAPI

sentiments = ["positive", "neutral", "negative"]


def fake_answer(text: str):
    return random.choice(sentiments)


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.state.models = {}
    app.state.models["sentiment_analysis"] = fake_answer


@app.on_event("shutdown")
async def shutdown_event():
    app.state.models.clear()
    sentiments.clear()


@app.get("/predict")
async def predict(text: str = "Olá Mundo!"):
    result = app.state.models["sentiment_analysis"](text)
    return {"text": text, "result": result}

"""
Descrição:
----------
O trecho de código acima executa as seguintes ações:

* Global:
  -------
         inicializa uma variável global chamada 'sentiments' com uma lista de três elementos
* Startup:
  --------
          inicializa uma variável de estado chamada 'models' com um dicionário para a função fake_answer
* Shutdown:
  ---------
           - limpa todos os itens na variável models
           - limpa todos os itens na variável sentiments
"""