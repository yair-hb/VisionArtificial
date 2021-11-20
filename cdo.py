import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('autos.mp4')

while True:
  ret, frame = cap.read()
  if ret == False: break
    
  cv2.imshow('Frame', frame)
  
  k= cv2.waitkey(1) & 0xff
  if k == 27:
    break
cap.release()
cv2.destroyAllWindows()
