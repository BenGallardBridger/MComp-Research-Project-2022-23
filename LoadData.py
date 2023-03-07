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

    def createHandSkeletons(parentFolderLocation, handImgLocation):
        handProcessor = hands.hands()
        for imageFolder in os.scandir(parentFolderLocation):
            currentLetter = os.path.split(imageFolder)[1]
            currentPath = handImgLocation + "\\" + currentLetter
            os.chdir(currentPath)
            for imagePath in os.scandir(imageFolder.path):
                image = cv2.imread(imagePath.path)
                newImg = handProcessor.handsBackground(image)
                imagename = os.path.split(imagePath)[1]
                cv2.imwrite(imagename,newImg)

    def videoToImages(parentFolderLocation, imagePath):
        for videoPath in os.scandir(parentFolderLocation):
            currentLetter = os.path.split(videoPath)[1][0]
            imagePathTemp = imagePath + "\\" + currentLetter
            os.chdir(imagePathTemp)
            video = cv2.VideoCapture(videoPath.path)
            success,image = video.read()
            count = 0
            while success:
                cv2.imwrite(currentLetter + "%d.jpg" % count, image)
                success,image = video.read()
                count += 1