import mlflow
import random
import time
import numpy as np
from itertools import combinations
from src.sql.image import ImageEmbedd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

class TestPerformance:
    def embed_convert(self, vector_embed):
            conv = list(map(float, vector_embed.strip("[]").split(",")))
            return np.array(conv, dtype=np.float32) 

    def count_similarity(self, query_vector: np.ndarray, current_vector: np.ndarray, thres:float) -> float:
            dot_product = np.dot(query_vector, current_vector)
            norm_product = np.linalg.norm(query_vector) * np.linalg.norm(current_vector)
            
            similarity = 1 - (dot_product / norm_product)
            
            threshold = thres # 0.4
            if similarity < threshold:
                status = 1
            else:
                status = 0
            return status  
        
    def run_test(self):
        img_embed = ImageEmbedd()
        numbers = range(5)
        pairs = combinations(numbers, 2)
        THRESHOLD = 0.4
        y_label = [1] * 10 + [0] * 10
        pred = []
        start_time = time.time()

        face1 = img_embed.image_fetch("1") # each has 5 face
        face2 = img_embed.image_fetch("2")

        # SIMIILAR FACE
        for a, b in pairs:
            f1 =  self.embed_convert(face1[a][1])
            f2 =  self.embed_convert(face1[b][1])
            pred.append(self.count_similarity(f1, f2, THRESHOLD))  
            
        # DISIMILAR FACE
        for n in range(10):
            f1 =  self.embed_convert(face1[random.randint(0, 4)][1])
            f2 =  self.embed_convert(face2[random.randint(0, 4)][1])
            pred.append(self.count_similarity(f1, f2, THRESHOLD))
            
        end_time = time.time()
        accuracy = accuracy_score(y_label, pred)
        precision = precision_score(y_label, pred)
        recall = recall_score(y_label, pred)
        f1 = f1_score(y_label, pred)
        response_time = end_time - start_time

        mlflow.set_tracking_uri('sqlite:///mlflow.db')
        mlflow.set_experiment("web_attendance_system")

        with mlflow.start_run():
            mlflow.log_param("Threshold", THRESHOLD)
            mlflow.log_metric("Accuracy", accuracy)
            mlflow.log_metric("Precision", precision)
            mlflow.log_metric("Recall", recall)
            mlflow.log_metric("F1", f1)
            mlflow.log_metric("response_time", response_time)

