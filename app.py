from src.main import LoginPage

start = LoginPage()
start.run_login()

# import numpy as np
# from src.sql.image import ImageEmbedd
# ## TEST THE SIMILARITY FUNCTION!!! ADD MORE ONE PERSON
# img_embed = ImageEmbedd()

# def cosine_distance(vec1: np.ndarray, vec2: np.ndarray) -> float:
#     """Compute the cosine distance between two vectors."""    
#     dot_product = np.dot(vec1, vec2)
#     norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
#     return 1 - (dot_product / norm_product)

# adam = img_embed.image_fetch(1)
# brad = img_embed.image_fetch(2)
# # ADAM
# adam1 = adam[0][1] 
# adam1 = list(map(float, adam1.strip("[]").split(",")))
# adam1 = np.array(adam1, dtype=np.float32) 

# adam2 = adam[1][1] 
# adam2 = list(map(float, adam2.strip("[]").split(",")))
# adam2 = np.array(adam2, dtype=np.float32) 

# # BRAD
# brad1 = brad[0][1] 
# brad1 = list(map(float, brad1.strip("[]").split(",")))
# brad1 = np.array(brad1, dtype=np.float32) 
 

# # SIMILAR
# print(cosine_distance(adam1, adam2))
# # UNSIMILAR
# print(cosine_distance(adam1, brad1))

# from src.pages.face_auth import FaceMatch

# face = FaceMatch()
# face.run()

