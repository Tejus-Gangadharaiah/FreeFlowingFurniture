import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	cv.imshow('Image',frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()