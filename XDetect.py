# from tkinter import font
import cv2
import numpy as np
import pytesseract
# import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot Open Video")

cntr = 0

while True:
    ret , frame = cap.read()
    cntr = cntr + 1
    if((cntr % 20) == 0):
        imgH , imgW , _ = frame.shape
        x1 , y1 , w1 , h1 = 0 , 0 , imgH , imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x , y , w , h = int(boxes[1]) , int(boxes[2]) , int(boxes[3]) , int(boxes[4])
            cv2.rectangle(frame , (x , imgH - y) , (w , imgH - h) , (0 , 0 , 255) , 3)
            cx = (int)((x - (imgH - y))/2)
            cy = (int)((w - (imgH - h))/2)
        cv2.putText(frame , imgchar , (x1 + int(w1/50) , y1 + int(h1 / 50)) , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (0 , 0 , 255) , 3) 

        print(cx , cy)
        cv2.imshow('X Detect' , frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()   