import streamlit as st
from src.pages.main import LoginPage
from src.pages.face_auth import FaceMatch
from pages.data_register import Register

start = LoginPage()
face = FaceMatch()
reg = Register()

if "page" not in st.session_state:
            st.session_state["page"] = "home"

page = st.session_state["page"]
if page == "home":
    start.login()
elif page == "register":
    reg.data_register()
elif page == "faceMatch":
    face.face_recog()
    

# Initialize session state
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False
    
# if "regist" not in st.session_state:
#     st.session_state["regist"] = False

# Check login status
# if not st.session_state["logged_in"]:
#     start.login()
# else:
#     face.face_recog()

