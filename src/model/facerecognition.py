# import cv2
# import streamlit as st

# class VideoCapture:
#     def recognize(self):
#         """Capture a single frame from the webcam and return it."""
#         cap = cv2.VideoCapture(0)  # Open webcam
#         ret, frame = cap.read()  # Capture a single frame

#         if not ret:
#             st.error("Failed to capture video")
#             cap.release()
#             return None

#         cap.release()  # Release the webcam

#         # Convert frame from BGR (OpenCV) to RGB (Streamlit)
#         return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# # class FaceRecognition:
# #     def __init__(self):
# #         pass
    
# #     def recognize(self, video_ui):
# #         cap = cv2.VideoCapture(0)
# #         faceCascade = cv2.CascadeClassifier("./artifacts/cascade/haarcascade_frontalface_default.xml")

# #         while cap.isOpened():
# #             ret, frame = cap.read()
# #             if not ret:
# #                 st.error("Failed to capture image")
# #                 break

# #             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #             faces = faceCascade.detectMultiScale(
# #                 gray,
# #                 scaleFactor=1.1,
# #                 minNeighbors=5,
# #                 minSize=(30, 30)
# #             )

# #             for (x, y, w, h) in faces:
# #                 cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# #                 if w >= 300 and h >= 300:
# #                     face_roi = frame[y:y+h+50, x:x+w+50]
# #                     print(type(face_roi))
# #                     # st.session_state["captured_face"] = face_roi  # Save to session state
# #                     # st.session_state["capture"] = True

# #             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #             video_ui.update_frame(frame_rgb)
            
# #         cap.release()
            

        