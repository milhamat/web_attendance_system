import streamlit as st
from src.utils.session import Session 
from src.pages.face_auth import FaceMatch
from src.pages.face_capt import FaceCapture
from src.pages.data_register import Register
from src.pages.dashboard import UserDashboard
    
class LoginPage(Session):
    def login(self):
        st.title("Login Page")
        
        # Input fields
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        col1, col2, col3 = st.columns([1, 1, 6])
        
        # Login button
        with col1:
            loginButton = st.button("Login")
        
        with col2:
            st.button("Sign In", on_click=self.set_page, args=("register",))
            
        if loginButton:
            if username == "admin" and password == "password":
                st.session_state["page"] = "faceMatch"
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")
        
    def run(self):
        """Runs the app based on the active page."""
        face = FaceMatch()
        reg = Register()
        capt = FaceCapture()
        dash = UserDashboard()
                    
        page = st.session_state["page"]
        if page == "home":
            self.login()
        elif page == "register":
            reg.data_register()
        elif page == "faceMatch":
            face.face_recog()
        elif page == "faceCapture":
            capt.capture()
        elif page == "dashboard":
            dash.dashboard()