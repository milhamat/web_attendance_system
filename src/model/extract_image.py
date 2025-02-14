import torch
from PIL import Image
import torch.nn.functional as F
from facenet_pytorch import MTCNN, InceptionResnetV1

class Extract:
    def __init__(self):
        self.mtcnn = MTCNN()

    def get_face(self, images, isList=True):
        if isList:
            extracted_faces = []
            for img in range(len(images)):
                im = Image.fromarray(images[img])
                extracted_faces.append(self.mtcnn(im).unsqueeze(0))
        else:
            im = Image.fromarray(images)
            extracted_faces = self.mtcnn(im).unsqueeze(0)
        
        return extracted_faces
    
    def extract(self, extracted_faces, isList=True):
        resnet = InceptionResnetV1(pretrained='casia-webface').eval()
        if isList:
            embed_faces = []
            for face in extracted_faces:
                with torch.no_grad():
                    embeding = resnet(face)
                embeddings1 = embeding.squeeze().numpy()
                
                embed_faces.append(embeddings1.tolist())
                
        else:
            with torch.no_grad():
                    embeding = resnet(extracted_faces)
            embeddings1 = embeding.squeeze().numpy()
            
            embed_faces = embeddings1.tolist()
            
        return embed_faces
        
    