import torch
class SimilarityFace:
    def __init__(self):
        self.status = ''
    
    def count_similarity(self, query_vector, current_vector):
        
        similarity = torch.nn.functional.cosine_similarity(query_vector, current_vector).item()
        # Convert to cosine distance (1 - similarity)
        cosine_distance = 1 - similarity

        # Set a threshold for verification
        threshold = 0.4  # Adjust based on your dataset
        if cosine_distance < threshold:
            self.status = 'Same person'
        else:
            self.status = 'Different persons'
        return self.status    
    
# Query vector image 

# Current Vector image

# Count Similarity

# Final Result    