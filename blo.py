import numpy as np
import cv2

def draw_con(rawImage):
	hsv = cv2.cvtColor(rawImage, cv2.COLOR_BGR2HSV)

	hue ,saturation ,value = cv2.split(hsv)


	retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	medianFiltered = cv2.medianBlur(thresholded,5)
	

	contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	print len(contours)

	cv2.drawContours(rawImage,contours,1,(0,255,0),3)


	cv2.imshow(' Image',rawImage)
	cv2.waitKey(0)
	
	cnt=contours[1]

	
	rect = cv2.minAreaRect(cnt)
	box = cv2.cv.BoxPoints(rect)
	
	box = np.int0(box)

	cv2.drawContours(rawImage,[box],0,(0,255,0),2)


	for i in range(4):
		cv2.line(rawImage,(0,0),tuple(box[i]),(0,255,255))

	cv2.imshow(' Image',rawImage)
	cv2.waitKey(0)
	return rawImage


draw_con(cv2.imread('my_test.jpg'))
