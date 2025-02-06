import streamlit as st
from src.utils.session import Session 

class UserDashboard(Session):
    def dashboard(self):
        st.title("User Dashboard")
        st.write("Welcome to the User Dashboard")
        st.button("Logout", on_click=self.set_page, args=("home",))