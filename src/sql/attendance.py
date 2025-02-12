import psycopg2
from src.sql.user import UserData

class Attendance(UserData):
    def create_table(self): 
        """Creates a user table."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE attendance (
                id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                check_in TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                check_out TIMESTAMP,
                status VARCHAR(10) CHECK (status IN ('Present', 'Absent', 'Late', 'On Leave')),
                remarks TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
        """)
        
        conn.commit()
        print("Table 'users' is ready.")
        cur.close()
        conn.close()
        
    def check_in(self, user_id, status):
        """Inserts a new user into the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("INSERT INTO attendance (user_id, status) VALUES (%s, %s) RETURNING id", (user_id, status))
        # user_id, created_time = cur.fetchone()
        
        conn.commit()
        # print(f"User {username} inserted with ID {user_id} at {created_time}")
        
        cur.close()
        conn.close()
        
    def check_out(self, user_id):
        """Inserts a new user into the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute(f"""
                    UPDATE attendance
                    SET check_out = NOW()
                    WHERE user_id = {user_id}
        """)
        # user_id, created_time = cur.fetchone()
        
        conn.commit()
        # print(f"User {username} inserted with ID {user_id} at {created_time}")
        
        cur.close()
        conn.close()
        
    def fetch_attendance(self):
        """Fetches all users from the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM attendance")
        attd = cur.fetchall()
        
        cur.close()
        conn.close()
        return attd
