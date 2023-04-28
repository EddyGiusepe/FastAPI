"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro

🤗 Este script foi baseado no Analytics Vidhya de Rahmat Faisal 🤗  
"""

"""Criando nosso Modelo com Keras"""
# Imaginamos que temos a seguinte função:
def f(x):
    y = (2 * x) - 1
    return y

print(f(2))

"""
De maneira similar vamos a construir uma REDE NEURAL para que faça essa tarefa.
"""
"""Criamos a nossa Rede Neural simples"""

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Construimos nosso Modelo com o Método Sequential:
model = tf.keras.Sequential([
   keras.layers.Dense(units=4, input_shape=[1]),
   keras.layers.Dense(units=8),
   keras.layers.Dense(units=1),
   ])

print(model.summary())


# O gráfico do Modelo:
tf.keras.utils.plot_model(model, show_shapes=True, to_file='TensorflowModel.png')


# Agora ajustamos nosso Modelo (Treinamos):
xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(xs, ys, epochs=100)


# Fazemos uma predição:
print(model.predict([10.0]))
"""
Lembre-se de que a Rede Neural lida com probabilidades. Com apenas 6 pontos de dados, não podemos
saber com certeza a resposta. Como resultado, o resultado de x=10 é muito próximo de y=19, mas não
necessariamente de 19.
"""
# Save nosso Modelo:
model.save('model')

