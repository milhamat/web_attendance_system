import mlflow
from src.sql.image import ImageEmbedd

img_embed = ImageEmbedd()

face1 = img_embed.image_fetch("1") # each has 5 face
face2 = img_embed.image_fetch("2")

mlflow.set_tracking_uri('sqlite:///mlflow.db')
mlflow.set_experiment("web_attendance_system")
mlflow.enable_system_metrics_logging()

# mlflow.log_param("Threshold", threshold)
# mlflow.log_metric("Cosine Similarity", similarity)
# mlflow.log_param("Match", is_match)