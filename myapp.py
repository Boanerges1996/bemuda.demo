from flask import Flask,request,jsonify,redirect,url_for, make_response,flash,send_from_directory,session
from mydbkey import myDb
from flask_mysqldb import MySQL
# from flask_mysqldb import MySQL
from db_service import get_db, close_db
import vehicle_API_Queries
from passlib.hash import sha256_crypt
from functools import wraps
import jwt
import vehicle_Rent_api_Query


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Boanerges'
# app.config['JWT_AUTH_URL_RULE']='/user/sign_in'


# jwt = JWT(app,vehicle_API_Queries.sign_in,vehicle_API_Queries.identity)


#Creates an instance of the Mysql
mysql = MySQL(app)


# set database config on app instance
configuration = myDb()
app.config['MYSQL_HOST']=configuration.MYQL_HOST
app.config['MYSQL_USER']=configuration.MYSQL_USER
app.config['MYSQL_PASSWORD']=configuration.MYSQL_PASSWORD
app.config['MYSQL_DB']=configuration.MYSQL_DB


#-------------------User API-------------------------------------------#
#All the mysql query fuction are stored in the functions below
#--------------------USER API----------------------------------------------#
'''
    Has 3 endpoints namely
    1./user/sign_in
    2./user/sign_up
    3./user/profile/info/<id>
        GET
        UPDATE
        DELETE(Done by only administrators)
    4./user/profile/info/all/<id> ONLY DONE BY ADMINISTRATORS
'''

def loggin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        if 'myToken' in request.headers:
            token = request.headers['myToken']
            
        if not token:
            return jsonify({
                "message":"login to access this route"
            }),401
        try:
            decode_token = jwt.decode(token,app.config['SECRET_KEY'])
            username = decode_token["user"]
            verify_token = vehicle_Rent_api_Query.verify_token(username)
        except:
            return jsonify({
                "user-token":"invalid"
            }),401
        return f(*args,**kwargs)

        
    return wrap 


@app.route('/user/sign_up',methods=["POST"])
def sign_up():
    request_data = request.json
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    othernames = request.json['othernames']
    username = request.json['username']
    tel_no = request.json['telephone_number']
    email = request.json['email']
    password = sha256_crypt.encrypt(request.json['user_password'])
    some_data = vehicle_Rent_api_Query.sign_up(firstname,lastname,othernames,username,tel_no,email,password)
    user_info = {**request_data,**some_data}
    return jsonify(user_info),201


@app.route('/user/sign_in',methods=["POST"])
def sign_in():
    username = request.json["username"]
    password = request.json["password"]
    user_info = vehicle_Rent_api_Query.sign_in(username,password)
    return user_info,201


@app.route('/user/profile/info/<id>',methods=["PUT","GET","DELETE"])
@loggin_required
def user_info(id):
    if request.method=="GET":
        user_info = vehicle_Rent_api_Query.get_user_info(id)
        return user_info

    
    elif request.method=="PUT":
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        othernames = request.json['othernames']
        username = request.json['username']
        tel_no = request.json['telephone_number']
        email = request.json['email']
        password = sha256_crypt.encrypt(request.json['user_password'])
        avatar = request.json['avatar']
        update_info = vehicle_Rent_api_Query.update_user_info(firstname,lastname,othernames,username,tel_no,email,avatar,password,id)
        return update_info


    elif request.method=="DELETE":
        user_id = request.json['user_id']
        verify_isAdmin = vehicle_Rent_api_Query.verify_if_is_admin(id)
        if verify_isAdmin:
            delete_user = vehicle_Rent_api_Query.delete_user(user_id)
            return delete_user


        else:
            return jsonify({
                "Message":"You are not an admin and therefore cant delete a user"
            })


@app.route('/user/profile/info/all/<id>',methods=["GET"])
@loggin_required
def get_all_users(id):
    verify_isAdmin = vehicle_Rent_api_Query.verify_if_is_admin(id)
    if verify_isAdmin:
        get_all_users = vehicle_Rent_api_Query.get_all_users()
        return get_all_users
    else:
        return jsonify({
            "message":"You are not an admin and therefore cant get all info"
        })


# -------------------------------END USER API---------------------------------------------



# -------------------------------DRIVER API ----------------------------------------------

@app.route('/user/driver/registration/<id>',methods=["POST"])
@loggin_required
def register_driver(id):
    date_of_birth = request.json["date_of_birth"]
    sex=request.json["sex"],
    license = request.json["license_no"]
    residential_address = request.json["residential_address"]
    verify_id_exist = vehicle_Rent_api_Query.verify_id_exist(id)
    if verify_id_exist:
        verify_isAdmin = vehicle_Rent_api_Query.verify_if_is_admin(id)

        if verify_isAdmin:
            register_driver_Admin = vehicle_Rent_api_Query.register_driver(date_of_birth,license,
            sex,residential_address,id)
            return register_driver_Admin
        else:
            verify_id_in_drivers = vehicle_Rent_api_Query.verify_userID_in_drivers(id)

            if verify_id_in_drivers:
                register_driver = vehicle_Rent_api_Query.register_driver(date_of_birth,
                license,sex,residential_address,id)
                return register_driver

            else:
                return jsonify({
                    "message":"Only administrators can register more drivers"
                })
    

    else:
        return jsonify({
            "message":"Invalid id, therefore cant register as a driver"
        })







@app.after_request
def _close_db(res):
    res.headers.add('Access-Control-Allow-Origin','*')
    res.headers.add('Access-Control-Allow-Methods','POST,GET,PUT,DELETE')
    res.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    close_db()
    return res



if __name__=="__main__":
    app.run(debug=True)