import cv2
import streamlit as st
from src.utils.session import Session 
from src.model.extract_image import Extract

class FaceMatch(Session):
    def __init__(self):
        if "start_auth" not in st.session_state:
            st.session_state["start_auth"] = False
            
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            self.frame_placeholder = st.empty()  # Store placeholder in class
    
    def capture(self):
        st.session_state.start_auth = True
        
    def update_frame(self, frame):
        """Update the Streamlit image dynamically."""
        self.frame_placeholder.image(frame, channels="RGB", use_container_width=True)

    # Function to capture video and update the placeholder
    def capture_video(self):
        cap = cv2.VideoCapture(0)
        faceCascade = cv2.CascadeClassifier("./artifacts/cascade/haarcascade_frontalface_default.xml")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture video")
                break

            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                if w >= 300 and h >= 300:
                    face_roi = frame[y:y+h+50, x:x+w+50]
                    Extract().get_face(face_roi, isList=False)
                    self.capture()
                    print("Face detected")
                    
            # Convert BGR (OpenCV) to RGB (Streamlit)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Update the Streamlit image in the UI class
            self.update_frame(frame_rgb)

            # Stop streaming when "Stop Capture" is pressed
            if st.session_state.start_auth:
                break

        cap.release()
        
    def run(self):
        # st.title("Face Authentication")
        # self.update_frame("./artifacts/user.jpg")
        self.frame_placeholder.image("./artifacts/user.jpg", channels="RGB", use_container_width=True)
        col4, col5, col6 = st.columns([2, 2, 6])
        button_placeholder = st.empty()
        with col4:
            if button_placeholder.button("Start Capture"):
                self.capture_video()
                
        if st.session_state.start_auth:
            # self.update_frame("./artifacts/user.jpg")
            st.session_state.start_auth = False
            self.frame_placeholder.image("./artifacts/user.jpg", channels="RGB", use_container_width=True)
            with col4:
                button_placeholder.empty()
                st.button("Dashboard", on_click=self.set_page, args=("dashboard",))
                