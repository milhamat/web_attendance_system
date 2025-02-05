import streamlit as st
from src.pages.main import LoginPage
from src.pages.face_auth import FaceMatch

start = LoginPage()
face = FaceMatch()

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Check login status
if not st.session_state["logged_in"]:
    start.login()
else:
    face.face_recog()

