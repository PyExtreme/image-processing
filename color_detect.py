#!/usr/bin/env python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def greenCircleDetect(hsv_frame):
	low_green = np.array([25, 52, 72])
	high_green = np.array([102, 255, 255])
	green_mask = cv2.inRange(hsv_frame, low_green, high_green)
	green = cv2.bitwise_and(hsv_frame, hsv_frame, mask=green_mask)
	cv2.imshow('green', green)

def redCircleDetect(hsv_frame):
	low_red = np.array([161, 155, 84])
	high_red = np.array([179, 255, 255])
	red_mask = cv2.inRange(hsv_frame, low_red, high_red)
	red = cv2.bitwise_and(hsv_frame, hsv_frame, mask=red_mask)
	cv2.imshow('red', red)

def blueCircleDetect(hsv_frame):
	low_blue = np.array([94, 80, 2])
	high_blue = np.array([126, 255, 255])
	blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
	blue = cv2.bitwise_and(hsv_frame, hsv_frame, mask=blue_mask)
	cv2.imshow('blue', blue)

while True:
	ret, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	greenCircleDetect(hsv_frame)
	redCircleDetect(hsv_frame)
	blueCircleDetect(hsv_frame)

	cv2.imshow('frame', frame)
	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()
