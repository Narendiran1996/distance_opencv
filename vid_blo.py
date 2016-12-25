import numpy as np
import cv2

cap = cv2.VideoCapture(1)

def draw_con(rawImage):

	hsv = cv2.cvtColor(rawImage, cv2.COLOR_BGR2HSV)

	hue ,saturation ,value = cv2.split(hsv)


	retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	medianFiltered = cv2.medianBlur(thresholded,5)
	

	contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	
	
	if(len(contours)>1):
		cnt=contours[1]

		cv2.drawContours(rawImage,contours,1,(0,255,0),3)

		rect = cv2.minAreaRect(cnt)
		box = cv2.cv.BoxPoints(rect)
	
		box = np.int0(box)

		cv2.drawContours(rawImage,[box],0,(0,255,0),2)


		for i in range(4):
			cv2.line(rawImage,(0,0),tuple(box[i]),(0,255,255))

		h1=box[0][1]-box[3][1]
		h2=box[1][1]-box[2][1]
	
		hi=(h1+h2)/float(2)
		if hi>200 and hi<600 and cv2.contourArea(cnt)<300000:
			print "workin"
			print (8.06*29.5)/hi*100
			return rawImage
		else:
			return None
		
	

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   
    ret_img=draw_con(frame)
    if ret_img!=None:
	    cv2.imshow('frame',ret_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
