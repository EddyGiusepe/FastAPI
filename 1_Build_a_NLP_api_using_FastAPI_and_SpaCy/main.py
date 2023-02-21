'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Estudo baseado no maravilhoso link --> https://medium.com/@xnel417x/build-a-nlp-api-using-fastapi-and-spacy-5015b42bf624


'''
Build a NLP api using FastAPI and SpaCy

Dependências

Este aplicativo usa SpaCy e FastAPI e é executado em um servidor Uvicorn e Pydantic para modelagem. Vamos instalar aqueles

* pip install fastapi uvicorn pydantic

Para o spaCy

* pip install -U pip setuptools wheel
* pip install -U spacy
* python -m spacy download en_core_web_sm
'''


from fastapi import FastAPI
import spacy
from pydantic import BaseModel


# Carregamos nosso modelo
en_core_web = spacy.load("en_core_web_sm")

'''
Ao adicionar essa Tag nos dará uma Interface de usuário incrível para documentação.
Nem precisa usar Postman ou Insomnia, pode rodar direto no navegador!
'''
app = FastAPI(tags=['sentence'])


# Nosso Modelo
class Input(BaseModel):
    sentence: str 


@app.post("/analyze_text")
def get_text_characteristics(sentence_input: Input):
    document = en_core_web(sentence_input.sentence)
    output_array = []
    for token in document:
        output = {
            "Index": token.i, "Token": token.text, "Tag": token.tag_, "POS": token.pos_,
            "Dependency": token.dep_, "Lemma": token.lemma_, "Shape": token.shape_,
            "Alpha": token.is_alpha, "Is Stop Word": token.is_stop
        }
        output_array.append(output)
    return {"output": output_array}
    