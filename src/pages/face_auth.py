import cv2
import numpy as np
import streamlit as st
from src.utils.session import Session 
from src.sql.image import ImageEmbedd
from src.sql.attendance import Attendance
from src.model.extract_image import Extract
from src.model.similarity import SimilarityFace

img_embed = ImageEmbedd()
similar = SimilarityFace()
attd = Attendance() 

class FaceMatch(Session):
    def __init__(self):
        if "start_auth" not in st.session_state:
            st.session_state["start_auth"] = False
            
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            self.frame_placeholder = st.empty()  # Store placeholder in class
    
    def pass_check(self):
        st.session_state.start_auth = True
        
    def update_frame(self, frame):
        """Update the Streamlit image dynamically."""
        self.frame_placeholder.image(frame, channels="RGB", use_container_width=True)
        
    def extract_image(self, frame):
        face = Extract().get_face(frame, isList=False)
        extracted = Extract().extract(face, isList=False)
        # TAKE SIMILARITY RESULTS
        query_image = img_embed.image_fetch(st.session_state["user_id"])
        # query_image = img_embed.image_fetch(1)
        query_image = query_image[0][1]
        query_image = similar.embed_convert(query_image)
        extracted = np.array(extracted)
        result = similar.count_similarity(query_image, extracted, 0.4)
        if result == "similar":
            self.pass_check()
        else:
            print("Diferent Person")
            # st.error("Differeant person please take another picture")
            

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
                if w >= 300 and h >= 300:
                    face_roi = frame[y:y+h+50, x:x+w+50]
                    self.extract_image(face_roi)
                    # st.success("Face detected")
                else:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
          
            # Convert BGR (OpenCV) to RGB (Streamlit)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Update the Streamlit image in the UI class
            self.update_frame(frame_rgb)

            # Stop streaming when "Stop Capture" is pressed
            if st.session_state.start_auth:
                break

        cap.release()
        
    def run(self):
        self.frame_placeholder.image("./artifacts/user.jpg", channels="RGB", use_container_width=True)
        
        status = st.selectbox("Status", ["Check-in", "Check-out"])
        col4, col5, col6 = st.columns([2, 2, 6])
        button_placeholder = st.empty()
        with col4:
            if button_placeholder.button("Start Capture", key='button_start_capture'):
                self.capture_video()
                
        if st.session_state.start_auth:
            st.session_state.start_auth = False
            self.frame_placeholder.image("./artifacts/user.jpg", channels="RGB", use_container_width=True)
            attd.create_table_attd()
            if status == "Check-in":
                attd.check_in(user_id=st.session_state["user_id"], status="Present")
            else:
                attd.check_out(st.session_state["user_id"])
            with col4:
                button_placeholder.empty()
                st.button("Dashboard", on_click=self.set_page, args=("dashboard",), key='button_next_to_dashboard')
                