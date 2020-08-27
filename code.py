#Invisible Cloak By A.D

import numpy as np
import cv2
import time
capture=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
final = cv2.VideoWriter('pOtterF.avi' , fourcc, 20.0, (640,480))
time.sleep(2)
background = 0 #capture the background
for i in range(30):
    ret, background = capture.read()#capture the image
    
    
while(capture.isOpened()):
    ret, img = capture.read()
    
    if not ret:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #for red 
    lower_red = np.array([0,120,70])
    upper_red = np.array([20,255,255])
    mask1 = cv2.inRange(hsv , lower_red , upper_red)
    
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv , lower_red , upper_red)
    
    #for Green comment out the above 6 lines of code for red color and use the following three lines
    # lower_green = np.array([25,52,72])
    # upper_green = np.array([102,255,255])
    # mask1 = cv2.inRange(hsv , lower_green , upper_green)
    
    #for blue comment out the above 6 lines of code for red color and use the following three lines
    #lower_blue = np.array([94, 80, 2])
    #upper_blue = np.array([126, 255, 255])
    #mask1 = cv2.inRange(hsv , lower_blue , upper_blue)
    
    mask1=mask1+mask2  # for green and blue remove this line

    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1)
    
        
    mask2 = cv2.bitwise_not(mask1) 
    
    
    
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    
    final_output = cv2.addWeighted(res1 , 1, res2 , 1 , 0)
    final.write(final_output)
    
    cv2.imshow('pOtterF' , final_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #press 'q' to close the window
        break
        
capture.release()
final.release()
cv2.destroyAllWindows()
