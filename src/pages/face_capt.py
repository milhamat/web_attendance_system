import streamlit as st
from src.utils.session import Session 

class FaceCapture(Session):
    def __init__(self):
        if "count" not in st.session_state:
            st.session_state["count"] = 0
    
    def increment_counter(self):
        st.session_state.count += 1
    
    def capture(self):
        st.title("Face Capture")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            frame_placeholder = st.empty()
            frame_placeholder.image("./artifacts/user.jpg", channels="BGR", use_container_width=True)
            
        st.write("Please capture your face 5 times")
        st.write(f"Picture Taken: {st.session_state.count}")
        col4, col5, col6 = st.columns([2, 2, 6])
        print(st.session_state.count)
        takePictButton = st.empty()
        with col4:
            takePictButton.button("Take a Picture", on_click=self.increment_counter)
        
        if st.session_state.count == 5:
            with col4:
                st.button("Next", on_click=self.set_page, args=("home",))
                st.session_state.count = 0
                takePictButton.empty()