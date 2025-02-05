import streamlit as st

class Register():
    def __init__(self):
        pass
    
    def set_page(self, page_name):
        """Updates session state to navigate instantly."""
        st.session_state["page"] = page_name
    
    
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
        