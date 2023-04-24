import mediapipe as mp
import cv2
import numpy as np
from os.path import exists
import csv

class hands:

    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    
    def retrieveHandsOverlay(self, image, background=None, receiveResults=False):
        if background is None: # set background to the image if no background has been specified
            background = image
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # turn the image to RGB
        results = self.hands.process(imageRGB) # process the image to receive hand information
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 0 :
                        cv2.circle(background, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                self.mpDraw.draw_landmarks(background, handLms, self.mpHands.HAND_CONNECTIONS)
        if (receiveResults):
            return (background, results)
        return background

    def handsBackground(self, image):
        background = np.array(np.zeros(image.shape)) # create an empty background for the locations to be placed on
        img = self.retrieveHandsOverlay(image, background)
        return img

    def handstoCSV(self, image, classification=None):
        headers = ["LH0x","LH0y","LH1x","LH1y","LH2x","LH2y","LH3x","LH3y","LH4x","LH4y","LH5x","LH5y","LH6x","LH6y","LH7x","LH7y","LH8x","LH8y","LH9x","LH9y","LH10x","LH10y","LH11x","LH11y","LH12x","LH12y","LH13x","LH13y","LH14x","LH14y","LH15x","LH15y","LH16x","LH16y","LH17x","LH17y","LH18x","LH18y","LH19x","LH19y", "LH20x", "LH20y","RH0x","RH0y","RH1x","RH1y","RH2x","RH2y","RH3x","RH3y","RH4x","RH4y","RH5x","RH5y","RH6x","RH6y","RH7x","RH7y","RH8x","RH8y","RH9x","RH9y","RH10x","RH10y","RH11x","RH11y","RH12x","RH12y","RH13x","RH13y","RH14x","RH14y","RH15x","RH15y","RH16x","RH16y","RH17x","RH17y","RH18x","RH18y","RH19x","RH19y", "RH20x", "RH20y"]
        if (classification is not None):
            headers.append('classification')
        if (not exists("handPos.csv")): # add the headers for the file if it doesnt exist
            with open("handPos.csv", "a", newline='') as csvFile:
                csvWriter = csv.writer(csvFile, delimiter=',')
                csvWriter.writerow(headers)
        outputImg, handsResult = self.retrieveHandsOverlay(image, None, True)

        with open("handPos.csv", "a",newline='') as csvFile: # open the CSV
            csvWriter = csv.writer(csvFile, delimiter=',')
            if handsResult.multi_hand_landmarks:
                if (len(handsResult.multi_hand_landmarks) <= 2 and len(handsResult.multi_hand_landmarks) >= 0): # check there are either 1 or 2 hands
                    row = [0] * 84
                    if (classification is not None): # if a classification is provided, add it to the end
                        row.append(classification)
                    handCounter = 0 # counter to check which number hand is currently being processed
                    rightHandInd = -1
                    for i in range(0, len(handsResult.multi_hand_landmarks)):
                        value = handsResult.multi_handedness[i].classification[0].label
                        if (value == "Right"):
                            rightHandInd = i
                    if (rightHandInd == -1):
                        rightHandInd = 0
                    origin = handsResult.multi_hand_landmarks[rightHandInd].landmark[0]
                    h, w, c = image.shape
                    origin = (int(origin.x*w) , int(origin.y*h))
                    for handLms in handsResult.multi_hand_landmarks: # working with each hand
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h) # get the position of the hands
                            handName = handsResult.multi_handedness[handCounter].classification[0].label # get the name of which hand is currently being processed
                            if (len(handsResult.multi_hand_landmarks)==1): #assume that if only one hand is on the screen it is the right hand
                                offset=1
                            else: #if there is more than one hand - check the hands' type to put it in the right category
                                if handName == 'Left':
                                    offset = 0
                                else:
                                    offset = 1
                            cx = origin[0]-cx
                            cy = origin[1]-cy
                            row[(id*2)+(42*offset)] = str(cx)
                            row[(id*2) +(42*offset)+1] = str(cy)
                        handCounter+=1
                    csvWriter.writerow(row)
        return outputImg #remove when in use just for testing
            

