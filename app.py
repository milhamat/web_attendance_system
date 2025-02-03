import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

def login():
    st.title("Login Page")
    
    # Input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Login button
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

def main_page():
    st.title("Welcome to the App")
    st.write("You are now logged in!")
    if st.button("Logout"):
        st.session_state["logged_in"] = False

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Check login status
if not st.session_state["logged_in"]:
    login()
else:
    main_page()

