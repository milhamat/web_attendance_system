import streamlit as st
import numpy as np
from PIL import Image
from matplotlib import cm
from facenet_pytorch import MTCNN

class Extract:
    def __init__(self):
        self.mtcnn = MTCNN()
        self.extracted_faces = []
        
    # def extract(self, images):
    #     for img in range(len(images)):
    #         im = Image.fromarray(images[img])
    #         self.extracted_faces.append(self.mtcnn(im))
    #     return self.extracted_faces

    def extract(self, images, isList=True):
        if isList:
            for img in range(len(images)):
                im = Image.fromarray(images[img])
                self.extracted_faces.append(self.mtcnn(im).unsqueeze(0))
        else:
            im = Image.fromarray(images)
            self.extracted_faces.append(self.mtcnn(im).unsqueeze(0))
        
        return self.extracted_faces
    