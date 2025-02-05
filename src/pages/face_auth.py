import streamlit as st
import cv2
# from PIL import Image

class FaceMatch:
    
    def __init__(self):
        pass

    def face_recog(self):
        # Streamlit UI
        st.title("Web Attendance System")

        # Start the webcam
        cap = cv2.VideoCapture(0)

        faceCascade = cv2.CascadeClassifier("./artifacts/cascade/haarcascade_frontalface_default.xml")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            frame_placeholder = st.empty()
            frame_placeholder.image("./artifacts/user.jpg", channels="BGR", use_container_width=True)
            
        st.write("")  
        st.write("")

        # Streamlit button to capture an image
        start = st.button("Start Camera")
        capture = False

        if start:
            while cap.isOpened():
                ret, frame = cap.read()
                
                if not ret:
                    st.error("Failed to capture image")
                    break
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1, # change to 1.2 if there any error detecting face due image quality 
                    minNeighbors=5,
                    minSize=(30, 30)
                )
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    print(f'width: {w}, height: {h}')
                    if w >= 300 and h >= 300:
                        face_roi = frame[y:y+h+50, x:x+w+50]
                        print(type(face_roi))
                        # cv2.imwrite("detected_face.jpg", face_roi)
                        capture = True
                        
                
                # Convert BGR (OpenCV) to RGB (Streamlit)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Display the live frame in Streamlit
                with col2:
                    frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)
                    
                if capture:
                    break

        # Release webcam
        cap.release()

        with col2:
            frame_placeholder.image("./artifacts/user.jpg", channels="BGR", use_container_width=True)
