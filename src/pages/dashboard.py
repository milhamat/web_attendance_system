import streamlit as st

class UserDashboard:
    
    def __init__(self):
        pass
    
    def set_page(self, page_name):
        """Updates session state to navigate instantly."""
        st.session_state["page"] = page_name
    
    def dashboard(self):
        st.title("User Dashboard")
        st.write("Welcome to the User Dashboard")
        st.button("Logout", on_click=self.set_page, args=("home",))