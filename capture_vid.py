import streamlit as st
import cv2
import numpy as np
from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading

st.title("Simple Video Capture with OpenCV in Streamlit")

# Placeholder for the video feed
frame_placeholder = st.empty()
frame_placeholder.image("./artifacts/user.jpg", channels="RGB", use_container_width=True)

# Initialize session state for video capture
if 'cap' not in st.session_state:
    st.session_state.cap = None
if 'captured_frame' not in st.session_state:
    st.session_state.captured_frame = None
if 'running' not in st.session_state:
    st.session_state.running = False

def start_camera():
    st.session_state.cap = cv2.VideoCapture(0)
    st.session_state.running = True
    while st.session_state.running:
        ret, frame = st.session_state.cap.read()
        if not ret:
            st.error("Failed to capture video")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")

def stop_camera():
    st.session_state.running = False
    if st.session_state.cap:
        st.session_state.cap.release()
        st.session_state.cap = None
        frame_placeholder.empty()
        frame_placeholder.image("./artifacts/user.jpg", channels="RGB", use_container_width=True)

def capture_frame():
    if st.session_state.cap:
        ret, frame = st.session_state.cap.read()
        if ret:
            st.session_state.captured_frame = frame
            st.success("Frame Captured!")
        else:
            st.error("Failed to capture frame")

def get_captured_frame():
    if st.session_state.captured_frame is not None:
        return np.array(st.session_state.captured_frame)
    else:
        return None

if st.button("Start Camera"):
    stop_camera()
    thread = threading.Thread(target=start_camera)
    add_script_run_ctx(thread)
    thread.start()

if st.button("Capture Frame"):
    capture_frame()

if st.session_state.captured_frame is not None:
    st.image(cv2.cvtColor(st.session_state.captured_frame, cv2.COLOR_BGR2RGB), channels="RGB", caption="Captured Frame")
    st.write("Captured frame as NumPy array:")
    st.write(get_captured_frame())
