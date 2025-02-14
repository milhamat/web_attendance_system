import psycopg2
import numpy as np
from src.sql.user import UserData

class ImageEmbedd(UserData):
    def create_table_image(self):
        """Creates the image_embeddings table if it doesn't exist."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS image_embeddings (
                id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                embedding VECTOR(512), --2048
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
        """)
        conn.commit()
        print("Table 'image_embeddings' is ready.")
        cur.close()
        conn.close()
    
    def image_store(self, user_id, embedding):
        """Stores an image embedding into the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        # embedding_list = embedding.tolist()  # Convert NumPy array to a list
        embedding_list = embedding
        cur.execute(
            "INSERT INTO image_embeddings (user_id, embedding) VALUES (%s, %s) RETURNING id;",
            (user_id, embedding_list)
        )
        conn.commit()
        print(f"Stored embedding for user {user_id}.")
        cur.close()
        conn.close()
    
    def image_fetch(self, user_id):
        """Fetches image embeddings for a given user."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        cur.execute("SELECT id, embedding FROM image_embeddings WHERE user_id = %s;", (user_id,))
        records = cur.fetchall()
        
        # for record in records:
        #     embedding_id, embedding_vector = record
        #     embedding_array = np.array(embedding_vector)  # Convert to NumPy array
        #     print(f"ID: {embedding_id}, Embedding: {embedding_array[:5]}...")  # Print first 5 values for preview

        cur.close()
        conn.close()
        return records
    