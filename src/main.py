import streamlit as st
from src.utils.session import Session 
from src.sql.user import UserData
from src.pages.face_auth import FaceMatch
from src.pages.face_upload import FaceUpload
from src.pages.data_register import Register
from src.pages.dashboard import UserDashboard
    
class LoginPage(Session):
    def __init__(self):
        if "user_id" not in st.session_state:
            st.session_state["user_id"] = 0
            
        if "next_auth" not in st.session_state:
            st.session_state["next_auth"] = False
    
    def login(self):
        userDat = UserData()
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
            userq = userDat.fetch_user_pass(username, password)
            if userq:
                st.success(f"Hello, {username}" )
                st.session_state["page"] = "faceMatch"
                st.session_state["user_id"] = userq[0][0]
                st.session_state["next_auth"] = True
                print("User found:", username)
            else:
                st.error("username and password could be not availabel or worng")
                print("User not found!")
        
    def run_login(self):
        """Runs the app based on the active page."""
        face = FaceMatch()
        reg = Register()
        capt = FaceUpload()
        dash = UserDashboard()
                    
        page = st.session_state["page"]
        if page == "home":
            self.login()
        elif page == "register":
            reg.data_register()
        elif page == "faceMatch":
            face.run()
        elif page == "faceUpload":
            capt.upload_foto()
        elif page == "dashboard":
            dash.dashboard()