import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit UI
st.title("Webcam Live Stream")

# Start the webcam
cap = cv2.VideoCapture(0)

# Streamlit button to capture an image
capture_button = st.button("Capture Image")

# Webcam feed display
frame_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to capture image")
        break

    # Convert BGR (OpenCV) to RGB (Streamlit)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Display the live frame in Streamlit
    frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

    # Capture the image when the button is clicked
    if capture_button:
        image = Image.fromarray(frame_rgb)  # Convert NumPy array to PIL image
        image.save("captured_image.jpg")  # Save image
        st.success("Image captured successfully!")
        st.image(image, caption="Captured Image", use_container_width=True)
        break  # Exit loop after capturing

# Release webcam
cap.release()
