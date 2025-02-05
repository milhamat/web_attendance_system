import streamlit as st
from pages.data_register import Register

reg = Register()
class LoginPage:
    def __init__(self):
        pass
            
            
    def set_page(self, page_name):
        """Updates session state to navigate instantly."""
        st.session_state["page"] = page_name
        
        
    def login(self):
        st.title("Login Page")
        
        # Input fields
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # Login button
        if st.button("Login"):
            if username == "admin" and password == "password":
                st.session_state["page"] = "faceMatch"
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")
        
        st.button("Sign In", on_click=self.set_page, args=("register",))