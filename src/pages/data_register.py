import streamlit as st
from src.utils.session import Session 

class Register(Session):
    
    def data_register(self):
        # if st.session_state["regist"]:
        st.title("Data Registration")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        repassword = st.text_input("Re-type Password", type="password")
        
        if st.button("Submit"):
            if not username.strip():
                st.error("Username cannot be empty")
            elif not password.strip():
                st.error("Password cannot be empty")    
            elif password != repassword:
                st.error("Password does not match") 
            else:
                st.success("Registration successful!")
                st.button("Next", on_click=self.set_page, args=("faceCapture",))
        