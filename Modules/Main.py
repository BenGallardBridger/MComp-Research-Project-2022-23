import handPretext
import cv2

cap = cv2.VideoCapture(0) # activate the video capture
hand = handPretext.hands() # create an object to process the hand tracking pretext tasks
while True:
    success, image = cap.read()
    image = cv2.flip(image, flipCode=1)
    outputImg = hand.handstoCSV(image)
    cv2.imshow("Output",outputImg)
    cv2.waitKey(1)
