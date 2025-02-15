from fastapi import FastAPI, File, UploadFile, HTTPException
from src.model.extract_image import Extract
from src.model.similarity import SimilarityFace
from facenet_pytorch import MTCNN, InceptionResnetV1
from torchvision import transforms
from PIL import Image
import torch
import numpy as np
import io

# Initialize FastAPI app
app = FastAPI()

def image_to_numpy(image_bytes: bytes) -> np.ndarray:
    """Convert image bytes to a NumPy array"""
    image = Image.open(io.BytesIO(image_bytes))  # Open image from bytes
    return np.array(image)  # Convert to NumPy array

@app.post("/upload/")
async def upload_image(image1: UploadFile = File(...)):
    try:
        image_bytes = await image1.read()  # Read file content
        img_array = image_to_numpy(image_bytes)  # Convert to NumPy array
        print(type(img_array))
        
        return {
            "filename": image1.filename,
            "shape": img_array.shape,  # Get the shape of the image (H, W, C)
            "dtype": str(type(img_array))  # Data type of array
        }

    except Exception as e:
        return {"error": str(e)}

# @app.post("/similarity/")
# async def compare_faces(image1: UploadFile = File(...), image2: UploadFile = File(...)):
#     return {
#             "data type1": type(image1),
#             "data type2": type(image2),
#             "message": "Similarity computed successfully!"
#         }
    # try:
    #     face1 = Extract().get_face(image1, isList=False)
    #     face1 = np.array(Extract().extract(face1, isList=False))
        
    #     face2 = Extract().get_face(image2, isList=False)
    #     face2 = np.array(Extract().extract(face2, isList=False))
        
    #     result = SimilarityFace().count_similarity(face1, face2, 0.4)

    #     return {
    #         "similarity_score": type(image1),
    #         "message": "Similarity computed successfully!"
    #     }
    
    # except ValueError as e:
    #     raise HTTPException(status_code=400, detail=str(e))

    # except Exception as e:
    #     raise HTTPException(status_code=500, detail="An error occurred while processing the images.")

# Run using: uvicorn filename:app --reload
