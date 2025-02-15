from fastapi import FastAPI, File, UploadFile, HTTPException
from src.model.extract_image import Extract
from src.model.similarity import SimilarityFace
from PIL import Image
import numpy as np
import io

app = FastAPI()

def image_to_numpy(image_bytes: bytes) -> np.ndarray:
    """Convert image bytes to a NumPy array"""
    image = Image.open(io.BytesIO(image_bytes))  
    return np.array(image) 

@app.post("/similarity/")
async def upload_image(image1: UploadFile = File(...), image2: UploadFile = File(...)):
    try:
        img1 = await image1.read()  
        img1 = image_to_numpy(img1)  
        
        face1 = Extract().get_face(img1, isList=False)
        face1 = np.array(Extract().extract(face1, isList=False))
        
        img2 = await image2.read()  
        img2 = image_to_numpy(img2) 
        
        face2 = Extract().get_face(img2, isList=False)
        face2 = np.array(Extract().extract(face2, isList=False))
        
        result = SimilarityFace().count_similarity(face1, face2, 0.4)
        
        return {
            "similarity_score": result
        }

    except Exception as e:
        return {"error": str(e)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the images.")

