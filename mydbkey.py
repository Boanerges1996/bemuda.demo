import os



class myDb():
    def __init__(self):
        if os.environ.get('vehicle_rental_api_ENV')=="production":
            self.MYQL_HOST = 'remotemysql.com'
            self.MYSQL_USER = 'H0gs53LE43'
            self.MYSQL_PASSWORD = 'NqpuhFBYee'
            self.MYSQL_DB = 'H0gs53LE43'
        else:
            self.MYQL_HOST = 'localhost'
            self.MYSQL_USER = 'root'
            self.MYSQL_PASSWORD = 'Boanergesrhobbie1996'
            self.MYSQL_DB = 'vehicle_api_db'


