import cv2
import os
import numpy as np
import datetime
cap = cv2.VideoCapture(0) # activate the video capture

letter = input("Enter the letter you are signing: ").upper()

path = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming Repo\MComp-Research-Project-2022-23\Data\Pictures"

path = os.path.join(path, letter)
if (not os.path.exists(path)):
    os.makedirs(path)
previousTime = datetime.datetime.now()
count= len(os.listdir(path));
while True:
    success, image = cap.read()
    image = cv2.flip(image, flipCode=1)
    image = image[0:image.shape[0], 0:image.shape[0]]
    currentTime = datetime.datetime.now()
    
    if ((currentTime - previousTime).seconds >= 4):
        count +=1
        previousTime = currentTime
        #save image
        filename = str(count) + ".jpg"
        newPath = os.path.join(path,filename)
        cv2.imwrite(newPath, image)
        image = np.ones(image.shape)
    cv2.putText(image,(str)(4 - (currentTime - previousTime).seconds),(50,100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image,(str)(count),(50,300), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Output",image)
    cv2.setWindowProperty("Output", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(1)