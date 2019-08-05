import cv2
import numpy as np
import cv2.cv as cv
import time
import serial
cap = cv2.VideoCapture(0)
while(1):
	
        #capture a frame
	ret, frame = cap.read()
	#convert bgr to hsv
    	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    	# define range of desired color in HSV
	lower_orange = np.array([0,105,194])
	upper_orange = np.array([27,255,255])
    	#threshold the hsv image to get desired color
   	mask = cv2.inRange(hsv, lower_orange, upper_orange)
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)
	# morphological operations
	kernel = np.ones((5,5),np.uint8)
    	erosion = cv2.erode(mask,kernel,iterations = 1)
    	dilation = cv2.dilate(mask,kernel,iterations = 1)
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	# Detect circles using HoughCircles
	circles =cv2.HoughCircles(closing,cv.CV_HOUGH_GRADIENT,2,120,param1=100,param2=55,minRadius=10,maxRadius=0)
	x=int(round(i[0])
        y=int(round(i[1])
        z=int(round(i[2])

	#Draw Circles
        if circles is not None:
        		for i in circles[0,:]:
                # If the ball is far, draw it in green
                		cv2.circle(frame,(x,y,z),(255,0,0),4)
                		cv2.circle(frame,(x,y),1,(0,255,0),4)
        
            
	cv2.imshow('tracking',frame)
    	cv2.imshow('Original',frame)
   	cv2.imshow('Mask',mask)
	cv2.imshow('Result',res)
    	

   	k = cv2.waitKey(5) & 0xFF
   	if k == 27:
        		break

cv2.destroyAllWindows()
cap.release()


















