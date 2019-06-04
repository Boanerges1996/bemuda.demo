import os



class myDb():
    def __init__(self):
        # if os.environ.get('vehicle_rental_api_ENV')=="production":
        #     self.MYQL_HOST = 'remotemysql.com'
        #     self.MYSQL_USER = 'H0gs53LE43'
        #     self.MYSQL_PASSWORD = 'NqpuhFBYee'
        #     self.MYSQL_DB = 'H0gs53LE43'
        if os.environ.get('second_db_ENV')=="second production":
            self.MYQL_HOST = 'sql10.freemysqlhosting.net'
            self.MYSQL_USER = 'sql10294510'
            self.MYSQL_PASSWORD = 'b2mfXxfqfl'
            self.MYSQL_DB = 'sql10294510'
        else:
            self.MYQL_HOST = 'localhost'
            self.MYSQL_USER = 'root'
            self.MYSQL_PASSWORD = 'Boanergesrhobbie1996'
            self.MYSQL_DB = 'vehicle_api_db'


