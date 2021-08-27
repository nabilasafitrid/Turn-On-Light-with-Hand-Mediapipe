import cv2
import time
import os
import HandTrackingModule as htm
import sys
import serial
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

cmd = "a"
port = serial.Serial('COM3', baudrate=115200, timeout=0.5)

while True:
    aka = 0
    success, img = cap.read()
    height, width, channels = img.shape
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
 

    if len(lmList) != 0:
            
        fingers = []

            # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
           fingers.append(1)
        else:
           fingers.append(0)
           

            # 4 Fingers
        for id in range(1, 5):
             if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
                    
             else:
                fingers.append(0)
                
        
        totalFingers = fingers.count(1)
            #print(totalFingers)
        if totalFingers == 0:
            cmd="off"
            port.write(str.encode('0'));
        if totalFingers == 5:
            cmd="on"
            port.write(str.encode('1'));
        else :
            cmd: "nohand"
            
            
        cv2.putText(img, cmd, (100, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
        
    cv2.imshow("Tracking",img)
        
    ch = 0xFF & cv2.waitKey(1)         
    if ch == ord("q"):
        break
 
cv2.destroyAllWindows()
