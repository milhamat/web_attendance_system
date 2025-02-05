import streamlit as st
from src.pages.main import LoginPage
from src.pages.face_auth import FaceMatch
from src.pages.data_register import Register
from src.pages.face_capt import FaceCapture
from src.pages.dashboard import UserDashboard

start = LoginPage()
face = FaceMatch()
reg = Register()
capt = FaceCapture()
dash = UserDashboard()

if "page" not in st.session_state:
    st.session_state["page"] = "home"
            
if "count" not in st.session_state:
     st.session_state.count = 0

page = st.session_state["page"]
if page == "home":
    start.login()
elif page == "register":
    reg.data_register()
elif page == "faceMatch":
    face.face_recog()
elif page == "faceCapture":
    capt.capture()
elif page == "dashboard":
    dash.dashboard()
    



