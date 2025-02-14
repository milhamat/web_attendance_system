import psycopg2

class UserData:
    def __init__(self):
        self.DB_NAME = "user_database"
        self.DB_USER = "postgres"
        self.DB_PASSWORD = "1234"
        self.DB_HOST = "localhost"
        self.DB_PORT = 5432
        self.create_database_user()
        self.create_table_user()
        
    def create_database_user(self):
        """Creates the database if it doesn't exist."""
        conn = psycopg2.connect(dbname="postgres", user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        conn.autocommit = True
        cur = conn.cursor()
        
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{self.DB_NAME}'")
        exists = cur.fetchone()
        
        if not exists:
            cur.execute(f"CREATE DATABASE {self.DB_NAME}")
            print(f"Database '{self.DB_NAME}' created successfully.")
        else:
            print(f"Database '{self.DB_NAME}' already exists.")
        
        cur.close()
        conn.close()
        
    def create_table_user(self): 
        """Creates a user table."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                full_name VARCHAR(100) NOT NULL,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(20) NOT NULL CHECK (role IN ('student', 'employee', 'admin')),
                deaprtmen_id INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        # print("Table 'users' is ready.")
        cur.close()
        conn.close()
        
    def insert_user(self, username, full_name, password, role, department_id):
        """Inserts a new user into the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("INSERT INTO users (username, full_name, password, role, deaprtmen_id) VALUES (%s, %s, %s, %s, %s) RETURNING id, created_at", (username, full_name, password, role, department_id))
        # user_id, created_time = cur.fetchone()
        
        conn.commit()
        # print(f"User {username} inserted with ID {user_id} at {created_time}")
        
        cur.close()
        conn.close()
        
    def fetch_all(self):
        """Fetches all users from the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        
        for user in users:
            print(user)  # (id, username, password, time)
        
        cur.close()
        conn.close()
        return users
    
    def fetch_user_pass(self, username, password):
        """Fetches all users from the database."""
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port=self.DB_PORT)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s;", (username, password))
        # query = "SELECT * FROM users WHERE username = %s AND password = %s;"
        # cur.execute(query, (username, password))
        user = cur.fetchall()
        
        # if user:
        #     print("User found:", user)
        # else:
        #     print("User not found!")
        
        cur.close()
        conn.close()
        return user
        