import streamlit as st

class FaceCapture:
    def increment_counter(self):
        st.session_state.count += 1
    
    def capture(self):
        st.title("Face Capture")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            frame_placeholder = st.empty()
            frame_placeholder.image("./artifacts/user.jpg", channels="BGR", use_container_width=True)
            
        st.write("Please capture your face")
        st.write(f"Capture count: {st.session_state.count}")
        st.button("Take a Picture", on_click=self.increment_counter)