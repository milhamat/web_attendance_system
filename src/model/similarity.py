import torch
import numpy as np
class SimilarityFace:
    def __init__(self):
        self.status = ''
        
    def embed_convert(self, vector_embed):
        conv = list(map(float, vector_embed.strip("[]").split(",")))
        return np.array(conv, dtype=np.float32) 
    
    def count_similarity(self, query_vector: np.ndarray, current_vector: np.ndarray) -> float:
        dot_product = np.dot(query_vector, current_vector)
        norm_product = np.linalg.norm(query_vector) * np.linalg.norm(current_vector)
        
        similarity = 1 - (dot_product / norm_product)

        # Set a threshold for verification
        threshold = 0.4  # Adjust based on your dataset
        if similarity < threshold:
            self.status = 'similar'
        else:
            self.status = 'disimilar'
        return self.status    
    
# Query vector image 

# Current Vector image

# Count Similarity

# Final Result    