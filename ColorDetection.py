import cv2
import numpy as np
import pandas as pd

r = g = b = 0
index = ['color' , 'color_name' , 'hex' , 'R' , 'G' , 'B']
csv = pd.read_csv('colors.csv' , names = index , header = None)

cap = cv2.VideoCapture(0)
cap.set(3 , 1280)
cap.set(4 , 720)


def getColorName(B , G , R):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(B - int(csv.loc[i , "B"])) + abs(G - int(csv.loc[i , "G"])) + abs(R - int(csv.loc[i , "R"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i , "color_name"]

    return cname 


while True:
    _ , frame = cap.read()
    height , width , _ = frame.shape
    cx = (int)(width / 2)
    cy = (int)(height / 2)
    b , g , r = frame[cy , cx]
    colour = frame[cy , cx]
    b , g , r = int(colour[0]) , int(colour[1]) , int(colour[2])
    print(b , g , r)
    
    name = getColorName(b , g , r)
    print(name)
    cv2.circle(frame , (cx , cy) , 50 , (25 , 25 , 25) , 3 )
    cv2.putText(frame , name , (10 , 50) , 0 , 1 ,  (b , g , r) , 3)
    
    cv2.imshow("Frame" , frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cap.destroyAllWindows()
