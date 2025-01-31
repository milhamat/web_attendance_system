import streamlit as st
import cv2
from PIL import Image

# Streamlit UI
st.title("Webcam Live Stream")

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
capture_button = st.button("Capture Image")
# start = st.button("Start")

# Webcam feed display
# frame_placeholder = st.empty()
# frame_placeholder.image("./artifacts/user.jpg", channels="BGR", use_container_width=True)

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
    
    # Convert BGR (OpenCV) to RGB (Streamlit)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Display the live frame in Streamlit
    with col2:
        frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

    # Capture the image when the button is clicked
    # if capture_button:
    #     image = Image.fromarray(frame_rgb)  # Convert NumPy array to PIL image
    #     image.save("captured_image.jpg")  # Save image
    #     st.success("Image captured successfully!")
    #     st.image(image, caption="Captured Image", use_container_width=True)
    #     break  # Exit loop after capturing
    
# Release webcam
cap.release()


