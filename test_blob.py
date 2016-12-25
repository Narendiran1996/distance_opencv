import numpy as np
import cv2
cap = cv2.VideoCapture(0)
def draw_con(rawImage):
	hsv = cv2.cvtColor(rawImage, cv2.COLOR_BGR2HSV)

	hue ,saturation ,value = cv2.split(hsv)


	retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	medianFiltered = cv2.medianBlur(thresholded,5)
	

	contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	print np.shape(rawImage)
	print len(contours)
	
	cv2.drawContours(rawImage,contours,0,(0,255,0),3)
	print cv2.contourArea(contours[0])

	cv2.imshow(' Image',rawImage)
	cv2.waitKey(0)
	
	cnt=contours[2]

	
	rect = cv2.minAreaRect(cnt)
	box = cv2.cv.BoxPoints(rect)
	
	box = np.int0(box)

	cv2.drawContours(rawImage,[box],0,(0,255,0),2)
	print box
	h1=box[0][1]-box[3][1]
	h2=box[1][1]-box[2][1]
	
	print (h1+h2)/float(2)
	cv2.imshow(' Image',rawImage)
	cv2.waitKey(0)
	return rawImage
draw_con(cv2.imread('cc.jpg'))
