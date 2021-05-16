import cv2

capture = cv2.VideoCapture(0)

while True:
   ret, frame=capture.read() #reading every frame

   hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   rgb= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


   cv2.imshow('orginal_frame',frame)
   cv2.imshow('HSV',hsv)
   cv2.imshow('RGB color',rgb)
   cv2.imshow('Gray color',gray)




   if cv2.waitKey(1) & 0xFF ==ord('q'):
      break

capture.release()
cv2.destroyWindow()


