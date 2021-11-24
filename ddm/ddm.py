#este es el codigo para el detector de movimiento
import cv2;
import numpy as np

video = cv2.VideoCapture(0)
#se inicializa una variable para hacer un conteo
i = 0

while True:
	ret, frame = video.read()
	if ret == False: break

	cv2.imshow('Frame', frame)
	if cv2.waitKey(1) & 0xff == ord ('q'):
		break
video.release()
