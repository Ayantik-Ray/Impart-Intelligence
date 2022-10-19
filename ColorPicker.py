import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("HSV")
# cv2.resizeWindows("HSV" , 640 , 240)
cv2.createTrackbar("HUE MIN" , "HSV" , 0 , 179 , nothing)
cv2.createTrackbar("HUE MAX" , "HSV" , 179 , 179 , nothing)
cv2.createTrackbar("SAT MIN" , "HSV" , 0 , 255 , nothing)
cv2.createTrackbar("SAT MAX" , "HSV" , 255 , 255 , nothing)
cv2.createTrackbar("VAL MIN" , "HSV" , 0 , 255 , nothing)
cv2.createTrackbar("VAL MAX" , "HSV" , 255 , 255 , nothing)

img_hsv = np.zeros((250 , 500 , 3) , np.uint8)

while True:
    h_min = cv2.getTrackbarPos("HUE MIN" , "HSV")
    h_max = cv2.getTrackbarPos("HUE MAX" , "HSV")
    s_min = cv2.getTrackbarPos("SAT MIN" , "HSV")
    s_max = cv2.getTrackbarPos("SAT MAX" , "HSV")
    v_min = cv2.getTrackbarPos("VAL MIN" , "HSV")
    v_max = cv2.getTrackbarPos("VAL MAX" , "HSV")

    # lower = np.array([h_min , s_min , v_min])    
    # upper = np.array([h_max , s_max , v_max])
    # mask = cv2.inRange(img_hsv , upper , lower)
    
    img_hsv[:] = (h_max - h_min , s_max - s_min , v_max - v_min)
    img_bgr = cv2.cvtColor(img_hsv , cv2.COLOR_HSV2BGR)
    
    cv2.imshow("HSV" , img_bgr)

    key = cv2.waitKey(1)
    if key == 27:
        break;
    
cv2.destroyAllWindows()


    
