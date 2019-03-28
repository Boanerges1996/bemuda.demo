from flask import Flask,render_template,redirect,request
from flask_mysqldb import MySQL
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

#-------------------------API-----------------------------#


#---------------User[GET,POST,PUT,DELETE]-----------------#
class User(Resource):
    #----------For the signIn Page------------------------#
    def get(self):


if __name__=="__main__":
    app.run(debug=True)