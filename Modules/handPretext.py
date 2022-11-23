import mediapipe as mp
import cv2
import numpy as np
from os.path import exists
import csv

class hands:
    def __init__(self): # create the instances required for hands processing in an object to increase efficiency
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
                    #place the hand skeleton on the image
                    cv2.putText(background, str(id),(cx, cy),cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255),2, cv2.LINE_AA)
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
        headers = ["LH0","LH1","LH2","LH3","LH4","LH5","LH6","LH7","LH8","LH9","LH10","LH11","LH12","LH13","LH14","LH15","LH16","LH17","LH18","LH19","LH20","RH0","RH1","RH2","RH3","RH4","RH5","RH6","RH7","RH8","RH9","RH10","RH11","RH12","RH13","RH14","RH15","RH16","RH17","RH18","RH19","RH20"]
        if (classification is not None):
            headers.append(classification)
        if (not exists("handPos.csv")): # add the headers for the file if it doesnt exist
            with open("handPos.csv", "a", newline='') as csvFile:
                csvWriter = csv.writer(csvFile, delimiter=',')
                csvWriter.writerow(headers)
        outputImg, handsResult = self.retrieveHandsOverlay(image, None, True)

        #imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #results = self.hands.process(imageRGB)

        with open("handPos.csv", "a",newline='') as csvFile: # open the CSV
            csvWriter = csv.writer(csvFile, delimiter=',')
            if handsResult.multi_hand_landmarks:
                if (len(handsResult.multi_hand_landmarks) <= 2 and len(handsResult.multi_hand_landmarks) >= 0): # check there are either 1 or 2 hands
                    row = [0] * 42
                    if (classification is not None): # if a classification is provided, add it to the end
                        row.append(classification)
                    handCounter = 0 # counter to check which number hand is currently being processed
                    for handLms in handsResult.multi_hand_landmarks: # working with each hand
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h) # get the position of the hands #TODO:: get relative postion to each other
                            handName = handsResult.multi_handedness[handCounter].classification[0].label # get the name of which hand is currently being processed
                            if (len(handsResult.multi_hand_landmarks)==1): #assume that if only one hand is on the screen it is the right hand
                                offset=1
                            else: #if there is more than one hand - check the hands' type to put it in the right category
                                if handName == 'Left':
                                    offset = 0
                                else:
                                    offset = 1
                            row[id+(21*offset)] = (str(cx) + '|' + str(cy))
                        handCounter+=1
                    csvWriter.writerow(row)
        return outputImg #remove when in use just for testing
            

