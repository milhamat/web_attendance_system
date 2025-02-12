# from src.main import LoginPage

# start = LoginPage()
# start.run()

from src.sql.user import UserData

userDat = UserData()

# userDat.create_database()
# userDat.create_table()
# userDat.insert_user('marlo', 'Mark Doe', 'asdlkasjh!@#$', 'employee', 2)
# print(type(userDat.fetch_users()))
print(userDat.fetch_users())
    



