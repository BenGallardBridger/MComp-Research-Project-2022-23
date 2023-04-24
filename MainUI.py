import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import matplotlib.pyplot as plt
import os
from keras.backend import argmax
from Modules import handPretext
import cv2
import numpy as np

def create_model():
    batch_size = 32
    img_height = 480
    img_width = 480
    model = models.Sequential()
    model.add(layers.Rescaling(1./255, input_shape=(img_height, img_width, 3))),
    model.add(layers.Conv2D(32, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(6))

    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    
    checkpoint_path = r'C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming Repo\MComp-Research-Project-2022-23\Checkpoints\cp6.ckpt'

    model.load_weights(checkpoint_path)

    return model

def makeGuess(model, currentImg):
    img = np.array(currentImg)
    predicted = model.predict(img[None,:,:], verbose = 0)

    #predicted = model.predict(currentImg)
    
    prediction = argmax(predicted, axis=-1)[0]
    prediction = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[prediction]
    print(prediction)

currentModel = create_model()

cap = cv2.VideoCapture(0) # activate the video capture
hand = handPretext.hands() # create an object to process the hand tracking pretext tasks
counter = 0
while True:
    success, originalImg = cap.read()
    originalImg = cv2.flip(originalImg, flipCode=1)
    originalImg = originalImg[0:originalImg.shape[0], 0:originalImg.shape[0]]
    processedImg = hand.handsBackground(originalImg)
    counter = counter + 1
    if (counter >4):
        makeGuess(currentModel, processedImg)
        counter = 0
    cv2.imshow("Output",originalImg)
    cv2.waitKey(1)