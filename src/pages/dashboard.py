import streamlit as st
# from src.utils.session import Session 

# class UserDashboard(Session):
class UserDashboard():
    def dashboard(self):
        st.title("User Dashboard")
        st.header("Welcome to the User Dashboard")
        
        
        col1, col2 = st.columns([3, 2])
        
        with st.sidebar:
            st.header("User Data")
            st.write("Full Name: Jhon Doe")
            st.write("Role: Employee")
            
        with col1:
            st.header("Average Clock In")
            st.header("Average Clock Out")
            
        with col2:
            st.header("Total Days Worked")
            st.header("Total Hours Worked")
        
        
        # st.button("Logout", on_click=self.set_page, args=("home",))
        st.button("Logout")
        

UserDashboard().dashboard()