# from src.main import LoginPage

# start = LoginPage()
# start.run_login()

## MAKE DASHBOARD UI
from src.pages.dashboard import UserDashboard

dash = UserDashboard()
dash.dashboard()

# import psycopg2

# DB_NAME = "user_database"
# DB_USER = "postgres"
# DB_PASSWORD = "1234"
# DB_HOST = "localhost"
# DB_PORT = 5432

# conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
# cur = conn.cursor()
            
# # cur.execute("SELECT check_in, check_out FROM attendance WHERE user_id = %s;", ('1'))
# cur.execute("SELECT * FROM attendance")
# time_query = cur.fetchall()
            
# cur.close()
# conn.close()

# print(time_query[-1][0])
# try:
#     dt = time_query[-1][3]
# except Exception as e:
#     print("Error", e)

# dt = time_query[-1][3]
# if dt is None:
#     print("---")
    
# # Extract date and time
# current_date = dt.date()  # Gets YYYY-MM-DD
# exact_time = dt.time()  # Gets HH:MM:SS.ssssss

# # Print results
# print("Current Date:", current_date)
# print("Exact Time:", exact_time)
# print(type(time_query[-1][2]))
