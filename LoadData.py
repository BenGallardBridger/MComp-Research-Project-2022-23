import pandas as pd
import tensorflow as tf
import numpy as np
import os
import cv2
import Modules.handPretext as hands
class loadData:
    def loadTrainTest(csv):
        dataframe = pd.read_csv(csv)
        
        dataframe['classification'] = pd.Categorical(dataframe['classification'])
        dataframe['classification'] = dataframe.classification.cat.codes

        targetVars = dataframe.pop('classification')
        tf_dataset = tf.data.Dataset.from_tensor_slices((dataframe.values, targetVars.values))


        trainSize = int(0.7*len(dataframe))
        testSize = int(0.2*len(dataframe))

        tf_dataset.shuffle()

        train = tf_dataset.take(trainSize)
        test = tf_dataset.skip(trainSize).take(testSize)
        val = tf_dataset.skip(trainSize+testSize)

        return train, test, val

    def loadFromFolders(parentFolderLocation):
        handProcessor = hands.hands()
        for imageFolder in os.scandir(parentFolderLocation):
            for imagePath in os.scandir(imageFolder.path):
                image = cv2.imread(imagePath.path)
                _ = handProcessor.handstoCSV(image, imageFolder.path[-1])