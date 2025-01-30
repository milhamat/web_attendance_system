import cv2

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("../artifacts/cascade/haarcascade_frontalface_default.xml")

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Found {0} faces!".format(len(faces)))
    is_detect = False
    for (x, y, w, h) in faces:
        
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        if w >= 270 and h >= 270:
            
            face_roi = frame[y:y+h+50, x:x+w+50]
            
            cv2.imshow('Croped Face', face_roi)
            
            cv2.imwrite("detected_face.jpg", face_roi)
            
        is_detect = True

    cv2.imshow('frame', frame)
    if is_detect:
        print(f"width: {w}, height: {h}")
        break

    
cap.release()
cv2.destroyAllWindows()