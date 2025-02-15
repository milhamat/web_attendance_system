import streamlit as st
from src.utils.session import Session 
from src.sql.attendance import Attendance

attd = Attendance()
class UserDashboard(Session):
    def dashboard(self):
        # time_query = attd.fetch_attendance(st.session_state["user_id"])
        time_query = attd.fetch_attendance('1')
        
        try:
            dt = time_query[-1][0]
        except Exception as e:
            print("Error", e)
            
        # Extract date and time
        current_date = dt.date()
        exact_time = dt.time()
            
        st.title("User Dashboard")
        
        basic_data = st.container(border=True)
        basic_data.write("**Name**         : Jhon")
        basic_data.write("**Role**         : employe")
        basic_data.write("**Dept ID**      : 110123")
        basic_data.write(f"**Current Date** : {current_date}")
        
        st.subheader("Clock In")
        clock_in_border = st.container(border=True)
        clock_in_border.write(f"**{exact_time}**")
        
        st.subheader("Clock Out")
        clock_out_border = st.container(border=True)
        clock_out_border.write(f"**---**")
        
        
        
        st.button("Logout", on_click=self.set_page, args=("home",), key="button_logout")
    