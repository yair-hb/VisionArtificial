#esta es una prueba para ver si podemos hacer un merge 
#en este codigo se deben checar las librerias ya que marca un error
#ya comprobamos que se actualizo en github
#comentario de prueba 
import time
import cv2
import numpy as np

video = cv2.VideoCapture(0)
i = 0
while True:
	ret, frame = video.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if i == 20:
		bgGray = gray
	if i > 20:
		dif  = cv2.absdiff(gray, bgGray)
		_, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
		cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(frame, cnts, -1, (0,0,255), 1)
		cvs.imshow('dif', dif)
		cvs.imshow('th', th)
		for c in cnts:
			area = cv2.contourArea(c)
			if area >= 9000:
				x,y,w,h = cv2.boundingRect(c)
				cv2.rectangle(frame, (x,x), (x+y, y+h), (255,0,0),2)

	cv2.imshow('Frame', frame)
	i = i+1
	if cv2.waitKey(1) & 0xff == ord ('q'):
		break
video.release()
