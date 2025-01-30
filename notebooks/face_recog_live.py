# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2

cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("../artifacts/cascade/haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1, # change to 1.2 if there any error detecting face due image quality 
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))
	is_detect = False
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		# cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	  
		if w >= 270 and h >= 270:
			# Extract the face ROI
			face_roi = frame[y:y+h+100, x:x+w+100]

			# Show the cropped face in a new window
			cv2.imshow("Cropped Face", face_roi)

			# Save the cropped face image
			cv2.imwrite("detected_face.jpg", face_roi)
		is_detect = True

	if is_detect:
        break
		print(f"width: {w}, height: {h}")
 
	# Display the resulting frame
	# cv2.imshow('frame', frame)
	# if cv2.waitKey(1) and 0xFF == ord('q'):
	# 	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()