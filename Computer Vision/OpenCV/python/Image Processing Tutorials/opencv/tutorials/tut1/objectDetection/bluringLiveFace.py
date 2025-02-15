import cv2
import numpy as np
import matplotlib.pyplot as plt


cam = cv2.VideoCapture(0)
haarPlatedPath = "../../../gallery/haarcascade_frontalface_default.xml"

plateClass = cv2.CascadeClassifier(haarPlatedPath)

while True:
    key = cv2.waitKey(10) & 0xFF
    ret, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if key == ord("q") or not ret:
        break
    plates = plateClass.detectMultiScale(grayFrame, 1.2, 5)
    for (x, y, w, h) in plates:
        faceRIO = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (32, 32))
    cv2.imshow("cam-feed", frame)

cam.release()
cv2.destroyAllWindows()
