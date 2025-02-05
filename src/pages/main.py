import streamlit as st
from face_auth import FaceMatch

face = FaceMatch()

class LoginPage:
    def __init__(self):
        pass
        
        
    def login(self):
        st.title("Login Page")
        
        # Input fields
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # Login button
        if st.button("Login"):
            if username == "admin" and password == "password":
                st.session_state["logged_in"] = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")

    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Check login status
    if not st.session_state["logged_in"]:
        login()
    else:
        face.face_recog()