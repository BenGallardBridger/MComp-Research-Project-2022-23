import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(units=60, activation='relu', input_shape=(42)),
    keras.layers.Dense()
])

model.compile(optimizer='adam',
              loss=tf.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#TODO:: Load dataset
