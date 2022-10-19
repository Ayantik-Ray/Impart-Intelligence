import cv2
import numpy as np
import pandas as pd

r = g = b = 0
index = ['color' , 'color_name' , 'hex' , 'R' , 'G' , 'B']
csv = pd.read_csv('colors.csv' , names = index , header = None)

cap = cv2.VideoCapture(0)
cap.set(3 , 1280)
cap.set(4 , 720)


# def getColorName(B , G , R):
#     minimum = 10000
#     for i in range(len(csv)):
#         d = abs(B - int(csv.loc[i , "B"])) + abs(G - int(csv.loc[i , "G"])) + abs(R - int(csv.loc[i , "R"]))
#         if d <= minimum:
#             minimum = d
#             cname = csv.loc[i , "color_name"]

#     return cname 


while True:
    _ , frame = cap.read()
    height , width , _ = frame.shape
    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    cx = (int)(width / 2)
    cy = (int)(height / 2)

    h , s , v = hsv_frame[cy , cx]
    
    if (h > 5 and h < 12):
        name = "Orange"
    elif (h >= 12 and h < 17):
        name = "Yellow - orange"
    elif (h > 16 and h < 34):
        name = "Yellow"
    elif (h > 33 and h < 40):
        name = "Yellow green"
    elif (h > 40 and h < 66):
        name = "Green"
    elif (h > 65 and h < 76):
        name = "Blue green"
    elif (h > 75 and h < 122):
        name = "Blue"
    elif (h > 121 and h < 144):
        name = "Purple"
    elif (h > 143 and h < 170):
        name = "Pink"
    elif (h > 170 and h < 179):
        name = "Pink red"
    elif (h > 0 and h < 5):
        name = "Red Orange"
    elif (h == 0 or h == 179):
        name = "Red"
    elif (s == 0):
        name = "White"
    elif (v == 0):
        name = "Black"
    elif (v > 65 and v < 140):
        name = "Grey"
    elif (h > 4 and h < 15) and (v > 150 and v < 190):
        name = "Brown"


    colour = frame[cy , cx]
    b , g , r = int(colour[0]) , int(colour[1]) , int(colour[2])
    # print(b , g , r)
    
    # name = getColorName(b , g , r)
    # print(name)
    

    cv2.circle(frame , (cx , cy) , 50 , (25 , 25 , 25) , 3 )
    cv2.putText(frame , name , (10 , 50) , 0 , 1 ,  (b , g , r) , 3)
    
    cv2.imshow("Frame" , frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cap.destroyAllWindows()
