import streamlit as st
from src.utils.session import Session 
from src.sql.user import UserData

userDat = UserData()

class Register(Session):
    
    def data_register(self):
        # if st.session_state["regist"]:
        st.title("Data Registration")
        username = st.text_input("Username")
        fullname = st.text_input("Full Name")
        password = st.text_input("Password", type="password")
        repassword = st.text_input("Re-type Password", type="password")
        role = st.selectbox("Role", ["Student", "Employee", "Lecturer"])
        id = st.text_input("ID Number")
        
        col1, col2, col3 = st.columns([1, 1, 6])
        with col1:
            submitButton = st.button("Submit")
        
        if submitButton:
            if not username.strip():
                st.error("Username cannot be empty")
            elif not fullname.strip():
                st.error("Full Name cannot be empty")
            elif not password.strip():
                st.error("Password cannot be empty")    
            elif password != repassword:
                st.error("Password does not match") 
            elif not role.strip():
                st.error("Role cannot be empty")
            elif not id.strip():
                st.error("ID Number cannot be empty")
            else:
                userDat.insert_user(username, fullname, password, role, id)
                st.success("Registration successful!")
                with col2:
                    st.button("Next", on_click=self.set_page, args=("faceUpload",))
                    print(f"username: {username}, fullname: {fullname}, password: {password}, repassword: {repassword}, role: {role}, id: {id}")