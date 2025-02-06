# utils/session.py
import streamlit as st

class Session:
    """Parent class to handle session state navigation."""
    
    def __init__(self):
        # Initialize session state if not already set
        if "page" not in st.session_state:
            st.session_state["page"] = "home"

    def set_page(self, page_name):
        """Updates session state to navigate instantly."""
        st.session_state["page"] = page_name
