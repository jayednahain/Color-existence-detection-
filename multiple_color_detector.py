import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while (1):
   _,frame=capture.read()

   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   lower_blue= np.array([110,80,80])
   high_blue= np.array([130,255,255])

   lower_green= np.array([50,50,50])
   high_green= np.array([70,255,255])

   color_area_blue = cv2.inRange(hsv,lower_blue,high_blue)

   color_area_yellow = cv2.inRange(hsv, lower_green, high_green)


   blue_result = cv2.bitwise_and(frame,frame,mask=color_area_blue)
   yellow_result= cv2.bitwise_and(frame,frame,mask=color_area_yellow)

   cv2.imshow('orginal_frame', frame)
   cv2.imshow('HSV', hsv)
   cv2.imshow('blue color area', color_area_blue)
   cv2.imshow('blue result', blue_result)

   cv2.imshow('green color area', color_area_yellow)
   cv2.imshow('yellow color', yellow_result)


   if cv2.waitKey(1) & 0xFF == ord('q'):
      break



capture.release()
cv2.destroyWindow()