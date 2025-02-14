import streamlit as st
import numpy as np
from PIL import Image
from src.model.extract_image import Extract
from src.sql.image import ImageEmbedd
from src.utils.session import Session 

img_embd = ImageEmbedd()

class FaceUpload(Session):
    def __init__(self):
        pass
    
    def upload_foto(self):
        # Initialize session state for storing images as numpy arrays
        if "uploaded_faces" not in st.session_state:
            st.session_state.uploaded_faces = []

        st.title("Upload Your 5 Face Photos")

        # File uploader
        uploaded_files = st.file_uploader(
            "Upload exactly 5 face images", 
            type=["jpg", "jpeg", "png"], 
            accept_multiple_files=True
        )
        id = st.text_input("ID Number")
        # Convert and store images as numpy arrays
        if uploaded_files:
            # st.session_state.uploaded_faces = uploaded_files[:5]
            st.session_state.uploaded_faces = [
                np.array(Image.open(img_file)) for img_file in uploaded_files[:5]
            ]

        # Display uploaded images
        st.write(f"📸 **Uploaded Images: {len(st.session_state.uploaded_faces)}/5**")
        cols = st.columns(5)

        for i, img_array in enumerate(st.session_state.uploaded_faces):
            with cols[i]:  
                st.image(img_array, caption=f"Image {i+1}", use_container_width=True)

        # Disable submit button until exactly 5 images are uploaded
        submit_disabled = len(st.session_state.uploaded_faces) != 5
        
        col1, col2, col3 = st.columns([1, 1, 6])
        with col1:
            submitButton = st.button("Submit", disabled=submit_disabled)
        
        if submitButton:
            if not id.strip():
                st.error("ID Number cannot be empty")
            faces = Extract().get_face(st.session_state.uploaded_faces)
            extracts = Extract().extract(faces)
            print(type(extracts))
            print(extracts[0])
            print(len(extracts))
            # THE EMBEDDING NEED TO BE SAVE ONE BY ONE
            for face in extracts:
                img_embd.image_store(id, face)
            
            # img_embd.create_table()
            # img_embd.image_store(id, extracts)
            # print(type(st.session_state.uploaded_faces[0]))
        
        if len(uploaded_files) == 5:
            with col2:
                st.button("Next", on_click=self.set_page, args=("home",))

        # Show warning if user uploads more than 5
        if len(uploaded_files) > 5:
            st.warning("⚠️ Only the first 5 images will be used!")
            
