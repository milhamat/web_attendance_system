from PIL import Image
import torch.nn.functional as F
from facenet_pytorch import MTCNN, InceptionResnetV1

class Extract:
    def __init__(self):
        self.mtcnn = MTCNN()
        self.extracted_faces = []
        self.embed_faces = []

    def get_face(self, images, isList=True):
        if isList:
            for img in range(len(images)):
                im = Image.fromarray(images[img])
                self.extracted_faces.append(self.mtcnn(im).unsqueeze(0))
        else:
            im = Image.fromarray(images)
            self.extracted_faces.append(self.mtcnn(im).unsqueeze(0))
        
        return self.extracted_faces
    
    def extract(self, isList=True):
        resnet = InceptionResnetV1(pretrained='casia-webface').eval()
        if isList:
            for face in self.extracted_faces:
                embeding = resnet(face).detach()
                embeddings1 = F.normalize(embeding, p=2, dim=1)
                self.embed_faces.append(embeddings1)
        else:
            embeding = resnet(self.extracted_faces[0]).detach()
            embeddings1 = F.normalize(embeding, p=2, dim=1)
            self.embed_faces.append(embeddings1) 
        
    