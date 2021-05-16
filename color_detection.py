import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while (1):
   _,frame=capture.read()

   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   lower_blue= np.array([110,80,80])
   high_blue= np.array([130,255,255])

   mask = cv2.inRange(hsv,lower_blue,high_blue)

   result = cv2.bitwise_and(frame,frame,mask=mask)

   cv2.imshow('orginal_frame', frame)
   cv2.imshow('HSV', hsv)
   cv2.imshow('RGB color', mask)
   cv2.imshow('Gray color', result)


   if cv2.waitKey(1) & 0xFF == ord('q'):
      break



capture.release()
cv2.destroyWindow()