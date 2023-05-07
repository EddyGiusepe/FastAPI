FROM bmltenabled/uvicorn-gunicorn-fastapi:python3.10-slim

WORKDIR /app

COPY /app/requirements.txt /app

RUN pip install -r /app/requirements.txt

# Observa que ./model faz om que essa pasta este em outro nível
COPY ./model /model

# Isto copia tudo o que tem na pasta "app" para a pasta de trabalho (app) (é só coincidência ter o mesmo nome)
# Preciso copiar o arquivo main.py dentro da pasta de trabalho 
COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
