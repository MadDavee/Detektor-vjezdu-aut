import cv2
import time
from time import sleep
import numpy as np
from pyfirmata import Arduino, util


board = Arduino('COM4')

car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")
 
cap = cv2.VideoCapture(r'pauto.mp4')
 
while True:
     
    #Přečtení snímků z videa
    respose, color_img = cap.read()
     
    if respose == False:
        break
     
    # Převod na "šedivé" plátno
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
     
    # Detekování z modelů
    faces = car_cascade.detectMultiScale(gray_img, 1.1, 1)
     
    # Vyzobrazení obdélníků na autech + LED
    i=0
    for (x, y, w, h) in faces:
        if i%2==0:
            cv2.rectangle(color_img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            i +=1
     
        cv2.imshow('img', color_img)
        board.digital[13].write(1)
             
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
 

cap.release()
board.digital[13].write(0)
cv2.destroyAllWindows()