from flask import Flask,request,jsonify,redirect,url_for, make_response,flash,send_from_directory,session
from mydbkey import myDb
from flask_mysqldb import MySQL
# from flask_mysqldb import MySQL
from db_service import get_db, close_db
import vehicle_API_Queries
from passlib.hash import sha256_crypt
from functools import wraps
import jwt
import json


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
            verify_user = vehicle_API_Queries.verify_token(decode_token)
        except:
            return jsonify({
                "user-token":"invalid"
            }),401
        return f(*args,**kwargs)

        
    return wrap 



#--------------------USER API----------------------------------------------#
'''
    Has 3 endpoints namely
    1./user/sign_in
    2./user/sign_up
    3./user/profile/<username>
        GET
        UPDATE
        DELETE(Done by only administrators)
'''

# User login authentication
@app.route('/user/sign_in', methods=['POST'])
def sign_in():
    '''
        This is the signup or login of each user of the system
        When a user logs in, the user is authenticated and a generated token is
        given to the user fro anymore request that the user wants to make
    '''
    username = request.json['username']
    password = request.json['user_password']
    mine = vehicle_API_Queries.sign_in(username,password)
    if mine:
        token = jwt.encode({"user":mine.json['username']}, app.config['SECRET_KEY'])
        session['mytoken']=token.decode('UTF-8')
        return jsonify({"token":token.decode('UTF-8')})
    else:
        return jsonify({
            'message':'Invalid credentials'
        })



# User Registration
@app.route('/user/sign_up', methods=['POST'])
def sign_up():
    '''
        This is for the registration of a user into the system witha unique
        A. Username
        B. Telephone number
        C. Email account
    '''
    request_data = request.json
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    othernames = request.json['othernames']
    username = request.json['username']
    tel_no = request.json['telephone_number']
    email = request.json['email']
    user_avatar = request.json['user_avatar']
    password = sha256_crypt.encrypt(request.json['user_password'])
    vehicle_API_Queries.sign_up(firstname,lastname,othernames,username,tel_no,email,password,user_avatar)
    return jsonify({"User":request_data}),201
       


# User profile infomation
@app.route('/user/profile/<string:username>',methods=['GET','PUT','DELETE'])
@loggin_required
def user_info(username):
    '''
        This route gets every information about a particular user and 
        returns it to the front-end to be rendered through an API call
        Before this is done, the user must be logged in first
    '''
    if request.method=='GET':
        try:
            username = str(username)
            my_profile_info = vehicle_API_Queries.user_profile_info(username)
            return jsonify(my_profile_info)
        except:
            return jsonify({
                "message":"invalid profile name"
            })

    elif request.method =='PUT':
        actual_username = username
        verify_user = vehicle_API_Queries.verify_username_in_db(actual_username)
        if verify_user:
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            othernames = request.json['othernames']
            username = request.json['username']
            tel_no = request.json['telephone_number']
            email = request.json['email']
            user_avatar = request.json['user_avatar']
            password = sha256_crypt.encrypt(request.json['user_password'])
            results = vehicle_API_Queries.update_user_info(firstname,lastname,othernames,username,tel_no,email,password,user_avatar,actual_username)
            return results,201
            
        else:
            return jsonify({
                "message":"invalid user"
            })
    elif request.method == 'DELETE':
        '''
            This only works for administrators. It checks the followinf before 
            deleting
            USER ACCOUNT EXISTS
            IF EXIST IS HE AN ADMIN
            IF HE IS AN ADMIN THEN WE CAN DELETE
        '''
        name = request.json['username']
        check_if_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if check_if_user_exist:
            verify_adminStatus = vehicle_API_Queries.verify_user_admin_status(username)
            if verify_adminStatus:
                aboutToBeDeletedUser = vehicle_API_Queries.verify_username_in_db(name)
                if aboutToBeDeletedUser:
                    delete_user = vehicle_API_Queries.delete_user_from_db(name)
                    return delete_user
                else:
                    return jsonify({
                        "message":"The user you are about to delete doesnt exist"
                    })
            
            else:
                return jsonify({
                    "message":"You are not an admin"
                })
            

        else:
            return jsonify({
                "message":"user doesnt exist in account"
            })

#--------------------END USER API--------------------------------------------#






#-------------------DRIVERS API ----------------------------------------------#
'''
    This portion consists of mainly Two endpoints
        /driver/registration/<username> POST
        /driver/info/<username>
            GET
            PUT
            DELETE
'''

@app.route('/driver/registration/<username>', methods=["POST"])
@loggin_required
def driver_registeration(username):
    '''
        This helps in the registration of a user who want to offer driving
        services for money
    '''
    date_of_birth = request.json['date_of_birth']
    residential_address = request.json['residential_address']
    license_number = request.json['license_no']
    sex = request.json['sex']
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        user_id = vehicle_API_Queries.get_user_id(username)
        if_registered = vehicle_API_Queries.check_if_driver_registered(user_id)
        if if_registered:
            return jsonify({
                "message":"driver already exists in driver_info database"
            })
        else:
            register_driver = vehicle_API_Queries.register_driver(date_of_birth,residential_address,
            license_number,sex,user_id)
            return register_driver
    else:
        return jsonify({
            "message":"User doesnt exist and therefore you cant regiser as a Driver"
        })



@app.route('/driver/info/<username>', methods=["GET","PUT","DELETE"])
@loggin_required
def driver_info(username):
    if request.method == "GET":
        '''
            This gets and return all the drivers info from the database
            FIRSTNAME ,LASTNAME, OTHERNAMES, USERNAME, EMAIL
            TELEPHONE NUMBER, AVATAR, LICENSE NUMBER,RESIDENTIAL ADDRESS,SEX
        '''
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            isDriver = vehicle_API_Queries.isDriver(username)
            if isDriver:
                driver_info = vehicle_API_Queries.get_driver_info(username)
                return driver_info
            
            else:
                return jsonify({
                    "message":"User is not a driver"
                })
            

        else:
            return jsonify({
                "message":"The driver you are looking for doesnt exist"
            })
            
    
    elif request.method=="PUT":
        date_of_birth = request.json['date_of_birth']
        residential_address = request.json['residential_address']
        license_no= request.json['license_no']
        sex = request.json['sex']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            isDriver = vehicle_API_Queries.isDriver(username)
            if isDriver:
                user_id = vehicle_API_Queries.get_user_id(username)
                update_user = vehicle_API_Queries.update_driver_info(date_of_birth,residential_address,license_no,sex,user_id)
                return update_user    
            else:
                return jsonify({
                    "message":"User is not a driver"
                })
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


    elif request.method=="DELETE":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            isDriver = vehicle_API_Queries.isDriver(username)
            if isDriver:
                user_id = vehicle_API_Queries.get_user_id(username)
                delete_driver = vehicle_API_Queries.delete_driver(user_id)  
                return delete_driver 
            else:
                return jsonify({
                    "message":"User is not a driver therefore cant delete an account"
                })
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })
        
#--------------------------END DRIVERS API-------------------------------------




# ---------------------------VEHICLES API--------------------------------------
# ---------------------------BUSES--------------------------------------------

@app.route('/user/vehicle/registration/bus_owners/<username>',methods=["POST"])
@loggin_required
def bus_owner_registration(username):
    '''
        Thise endpoint registers bus owners into the Bus_owners table in the
        database
    '''
    company_name = request.json['company_name']
    location = request.json['location']
    owner_avatar = request.json['owner_avatar']

    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        user_id = vehicle_API_Queries.get_user_id(username)
        if_busOwner_in_db = vehicle_API_Queries.check_id_bus_owner_db(user_id)
        if if_busOwner_in_db:
            register_bus_owner = vehicle_API_Queries.register_bus_owner(company_name,location,owner_avatar,user_id)
            return register_bus_owner

        else:
            return jsonify({
                "message":"You are already an owner"
            }),201
        
        
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })


@app.route('/user/vehicle/bus_owner/profile/<username>',methods=["PUT","GET","DELETE"])
@loggin_required
def bus_owner_profile(username):
    if request.method =="GET":
        '''
            This Gets the info of a user that has registered as driver
            By useing the username
        '''
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            user_id = vehicle_API_Queries.get_user_id(username)
            verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(user_id)
            if verify_id_in_busOwners:
               get_busOwner_info = vehicle_API_Queries.get_busOwner_info(user_id)
               return jsonify({
                    "Bus owner info": get_busOwner_info
                })
            else:
                return jsonify({
                    "message":"You have not registered your Bus Company"
                })
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="PUT":
        company_name =request.json['company_name']
        location = request.json['location']
        owner_avatar = request.json['owner_avatar']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            user_id = vehicle_API_Queries.get_user_id(username)
            verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(user_id)
            if verify_id_in_busOwners:
               update_info = vehicle_API_Queries.update_busOwner_info(company_name,location,owner_avatar,user_id)
               return update_info
               
            else:
                return jsonify({
                    "message":"Register as a bus user first"
                })
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="DELETE":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            user_id = vehicle_API_Queries.get_user_id(username)
            verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(user_id)
            if verify_id_in_busOwners:
               delete_account = vehicle_API_Queries.delete_busOwner(user_id)
               return delete_account
            else:
                return jsonify({
                    "message":"You cant delete an account you have not created"
                })
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })




@app.route('/user/vehicle/bus/registration/<username>',methods=["POST"])
@loggin_required
def bus_registration(username):
    bus_photo = request.json['bus_photo']
    car_no = request.json['car_no']
    capacity = request.json['capacity']
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(get_userid)
        if verify_id_in_busOwners:
            get_owner_id = vehicle_API_Queries.get_busOwner_id(get_userid)
            register_vehicle = vehicle_API_Queries.register_bus(bus_photo,car_no,capacity,get_owner_id)
            return register_vehicle

        else:
            return jsonify({
                "message":"Register as a bus user first"
            })

            
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })



@app.route('/user/vehicles/bus/all/<username>', methods=["GET"])
@loggin_required
def get_all_vehicles_of_user(username):
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(get_userid)
        if verify_id_in_busOwners:
            get_owner_id = vehicle_API_Queries.get_busOwner_id(get_userid)
            if_owner_id_in_buses = vehicle_API_Queries.check_owner_id_in_buses_db(get_owner_id)
            if if_owner_id_in_buses:
                user_info = vehicle_API_Queries.user_profile_info(username)
                user_info = user_info
                bus_owner_info = vehicle_API_Queries.get_busOwner_info(get_userid)
                buses_info = vehicle_API_Queries.get_allBuses_of_busOwner(get_owner_id)
                allInfo = {
                    "userinfo":user_info,
                    "owner_info":bus_owner_info,
                    "buses":buses_info
                }
                return jsonify({
                    "information":allInfo
                })
            else:
                return jsonify({
                    "message":"Have not registered any buses yet"
                })

        else:
            return jsonify({
                "message":"Register as a bus user first"
            })

        
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })


@app.route('/user/vehicles/buses/info/<username>',methods=["PUT","DELETE"])
@loggin_required
def buses_information(username):
    if request.method=="PUT":
        '''
            Here we use the car number as a value that cannot be changed
            so with that we update the car info where car_no is ...
        '''
        bus_image_url=request.json['bus_url']
        capacity = request.json['capacity']
        car_no = request.json['car_no']

        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(get_userid)
            if verify_id_in_busOwners:
                get_owner_id = vehicle_API_Queries.get_busOwner_id(get_userid)
                if_owner_id_in_buses = vehicle_API_Queries.check_owner_id_in_buses_db(get_owner_id)
                if if_owner_id_in_buses:
                    update_buses = vehicle_API_Queries.update_bus(bus_image_url,capacity,car_no)
                    return update_buses

                else:
                    return jsonify({
                        "message":"Have not registered any buses yet so no update for you"
                    })

            else:
                return jsonify({
                    "message":"Register as a bus user first before can perform update"
                })

    elif request.method=="DELETE":
        '''
            This ehlps in dleting a bus from the database by using the car number
            supplied in the query parameters
        '''
        car_no = request.json['car_no']

        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_id_in_busOwners = vehicle_API_Queries.check_userid_in_busOwners_db(get_userid)
            if verify_id_in_busOwners:
                get_owner_id = vehicle_API_Queries.get_busOwner_id(get_userid)
                if_owner_id_in_buses = vehicle_API_Queries.check_owner_id_in_buses_db(get_owner_id)
                if if_owner_id_in_buses:
                    deleteBus = vehicle_API_Queries.delete_bus(car_no)
                    return deleteBus

                else:
                    return jsonify({
                        "message":"Have not registered any buses yet so no update for you"
                    })

            else:
                return jsonify({
                    "message":"Register as a bus user first before can perform update"
                })
'''
    AN endpoint will be made for gettin all buses info in table with all user info 
    and bus owner info
'''
#-------------------------------------------END BUSES-------------------------------------------



# ----------------------------------------TROSKIS-----------------------------------------------
@app.route('/user/troki_owner/registration/<username>', methods=["POST"])
@loggin_required
def register_trokis_owners(username):

    owner_photo = request.json['owner_photo']
    location = request.json["location"]
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
        if verify_troski_owner_in_db:
            register_troski_owner = vehicle_API_Queries.register_trokis_owner(owner_photo,location,get_userid)
            return register_troski_owner

        else:
            return jsonify({
                "message":"You have already registered as a troski owner"
            })
        
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })


@app.route('/user/troski_owner/profile/<username>',methods=["PUT","GET","DELETE"])
@loggin_required
def troski_owner_profile(username):
    if request.method=="GET":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
            if verify_troski_owner_in_db:
                return jsonify({
                    "message":"You have not registered as a troski owner"
                })

            else:
                troskiOwner = vehicle_API_Queries.get_troski_owner_info(get_userid)
                return jsonify(troskiOwner)
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })
    
    elif request.method=="PUT":
        owner_photo = request.json['owner_photo']
        location = request.json["location"]
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
            if verify_troski_owner_in_db:
                return jsonify({
                    "message":"You have not registered as a troski owner and therefore canot delete"
                })

            else:
                updateTroski_owner = vehicle_API_Queries.update_trokis_owner_info(owner_photo,location,get_userid)
                return updateTroski_owner
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


    elif request.method=="DELETE":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
            if verify_troski_owner_in_db:
                return jsonify({
                    "message":"You have not registered as a troski owner"
                })

            else:
                delete_account = vehicle_API_Queries.delete_troski_owner(get_userid)
                return delete_account
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })



@app.route('/user/troski/registration/<username>', methods=["POST"])
@loggin_required
def register_troski(username):
    troski_photo = request.json['troski_photo_url']
    car_no = request.json['car_no']
    capacity = request.json['capacity']
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
        if verify_troski_owner_in_db:
            return jsonify({
                "message":"You have not registered as a troski owner"
            })

        else:
            getOwnerId = vehicle_API_Queries.get_troski_owner_id(get_userid)
            register_troski = vehicle_API_Queries.register_troski(troski_photo,car_no,capacity,getOwnerId)
            return register_troski
        
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })
    pass


@app.route('/user/troskis/info/<username>',methods=["GET","PUT","DELETE"])
@loggin_required
def troskis_info(username):
    if request.method=="GET":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
            if verify_troski_owner_in_db:
                return jsonify({
                    "message":"You have not registered as a troski owner"
                })

            else:
                getOwnerId = vehicle_API_Queries.get_troski_owner_id(get_userid)
                get_troskis = vehicle_API_Queries.get_all_troskis(getOwnerId)
                return jsonify(get_troskis)
            
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="PUT":
        car_photo = request.json['troski_photo_url']
        car_no = request.json['car_no']
        capacity = request.json['capacity']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
            if verify_troski_owner_in_db:
                return jsonify({
                    "message":"You have not registered as a troski owner"
                })

            else:
                getOwnerId = vehicle_API_Queries.get_troski_owner_id(get_userid)
                updateTroskis = vehicle_API_Queries.update_troski(car_photo,capacity,car_no)
                return updateTroskis

        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="DELETE":
        car_no = request.json['car_no']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_troski_owner_in_db = vehicle_API_Queries.verify_troski_owner_in_db(get_userid)
            if verify_troski_owner_in_db:
                return jsonify({
                    "message":"You have not registered as a troski owner"
                })

            else:
                getOwnerId = vehicle_API_Queries.get_troski_owner_id(get_userid)
                delete_troski = vehicle_API_Queries.delete_troski(car_no)
                return delete_troski

        else:
            return jsonify({
                "message":"Account doesnt exist"
            })
# ---------------------------------------END TROSKIS---------------------------------------


# ----------------------------------------PRIVATE CAR---------------------------------------
@app.route('/user/private_car/owner/registration/<username>',methods=["POST"])
@loggin_required
def register_private_car_owner(username):
    location = request.json['location']
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
        if verify_privateCarOwners_db:
            register_owner = vehicle_API_Queries.register_privateCarOwner(location,get_userid)
            return register_owner

        else:
            return jsonify({
                "message":"You are already an owner and therefore cant register more owners"
            })
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })


@app.route('/user/private_car/owner/info/<username>',methods=["GET","PUT","DELETE"])
@loggin_required
def private_car_owner_info(username):

    if request.method=="GET":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
            if verify_privateCarOwners_db:
                return jsonify({
                    "message":"You have not registered as an owner therfore cant get any info"
                })
                

            else:
                get_owner_info = vehicle_API_Queries.get_privateCarOwnerInfo(get_userid)
                return jsonify(get_owner_info)
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="PUT":
        location = request.json['location']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
            if verify_privateCarOwners_db:
                return jsonify({
                    "message":"You have not registered as an owner therefore cant update any info"
                })
                

            else:
               update = vehicle_API_Queries.update_privateCarOwner_info(location,get_userid)
               return update
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


    elif request.method=="DELETE":
        
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
            if verify_privateCarOwners_db:
                return jsonify({
                    "message":"You have not registered as an owner therefore cant delete any info"
                })  

            else:
               delete = vehicle_API_Queries.delete_privateCarOwner_info(get_userid)
               return delete
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


@app.route('/user/private_car/registration/<username>',methods=["POST"])
@loggin_required
def register_private_car(username):
    car_type= request.json['car_type']
    car_photo= request.json['car_photo_url']
    car_number= request.json['car_number']
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
        if verify_privateCarOwners_db:
            return jsonify({
                "message":"You have not registered as an owner therefore cant register a private car"
            })  

        else:
            get_owner_id = vehicle_API_Queries.get_privateCar_ownerId(get_userid)
            register_car = vehicle_API_Queries.register_privateCar(car_type,car_photo,car_number,get_owner_id)
            return register_car
           
    else:
        return jsonify({
            "message":"Account doesnt exist"
        })



@app.route('/user/private_car/info/<username>',methods=["GET","PUT","DELETE"])
@loggin_required
def private_car_info(username):

    if request.method=="GET":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
            if verify_privateCarOwners_db:
                return jsonify({
                    "message":"You have not registered as an owner therefore cant get a private car info"
                })  

            else:
                get_owner_id = vehicle_API_Queries.get_privateCar_ownerId(get_userid)
                get_info = vehicle_API_Queries.get_privateCar(get_owner_id)
                return jsonify(get_info)
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="PUT":
        car_type= request.json['car_type']
        car_photo= request.json['car_photo_url']
        car_number= request.json['car_number']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
            if verify_privateCarOwners_db:
                return jsonify({
                    "message":"You have not registered as an owner therefore cant Update a private car"
                })  

            else:
                get_owner_id = vehicle_API_Queries.get_privateCar_ownerId(get_userid)
                update = vehicle_API_Queries.update_car(car_type,car_photo,car_number)
                return update
        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


    elif request.method=="DELETE":
        '''
            This hasnt been tested
        '''
        car_no = request.json['car_no']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify_privateCarOwners_db = vehicle_API_Queries.verify_userID_in_privateCArOwner(get_userid)
            if verify_privateCarOwners_db:
                return jsonify({
                    "message":"You have not registered as an owner therefore cant delete a private car"
                })  

            else:
                get_owner_id = vehicle_API_Queries.get_privateCar_ownerId(get_userid)
                delete_car = vehicle_API_Queries.delete_car(car_no)
                return delete_car

        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

# ------------------------------END PRIVATE CARS---------------------------------------------------


# ---------------------------------------OTHER VEHICLES----------------------------------
@app.route('/user/other_vehicle/owners/registration/<username>',methods=["POST"])
@loggin_required
def register_otherVehicle_owners(username):
    photo = request.json["photo_url"]
    location = request.json["location"]
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
        if verify:
            register = vehicle_API_Queries.register_other_owners(photo,location,get_userid)
            return register

        else:
            return jsonify({
                "message":"already registered"
            })

    else:
        return jsonify({
            "message":"Account doesnt exist"
        })


@app.route('/user/other_vehicle/owners/info/<username>',methods=["GET","PUT","DELETE"])
@loggin_required
def other_vehicle_owner_info(username):
    if request.method=="GET":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
            if verify:
                return jsonify({
                    "message":"you have no acoount and therefore cant fetch any info"
                })

            else:
                get_info = vehicle_API_Queries.get_otherVehicleOwnersInfo(get_userid)
                return jsonify(get_info)
               

        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="PUT":
        photo = request.json['photo_url']
        location = request.json['location']
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
            if verify:
                return jsonify({
                    "message":"you have no acoount and therefore cant update any info"
                })

            else:
                update = vehicle_API_Queries.update_OtherVehicleOwnersInfo(photo,location,get_userid)
                return update

        else:
            return jsonify({
                "message":"Account doesnt exist"
            })

    elif request.method=="DELETE":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
            if verify:
                return jsonify({
                    "message":"you have no acoount and therefore cant fetch any info"
                })

            else:
                delete = vehicle_API_Queries.delete_OtherVehicleOwnersInfo(get_userid)
                return delete

        else:
            return jsonify({
                "message":"Account doesnt exist"
            })



@app.route('/user/other_vehicle/registration/<username>',methods=["POST"])
@loggin_required
def register_OtherVehicle(username):
    photo = request.json['photo_url']
    car_no = request.json['car_no']
    car_type = request.json['car_type']
    verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
    if verify_user_exist:
        get_userid = vehicle_API_Queries.get_user_id(username)
        verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
        if verify:
            return jsonify({
                "message":"you have no account and therefore cant register vehicle"
            })

        else:
            get_ownerid = vehicle_API_Queries.get_otherVehicleOwnerId(get_userid)
            register = vehicle_API_Queries.register_OtherVehicles(photo,car_no,car_type,get_ownerid)

            return register

    else:
        return jsonify({
            "message":"Account doesnt exist"
        })


@app.route('/user/other_vehicle/info/<username>',methods=["GET","PUT","DELETE"])
@loggin_required
def otherVehicleInfo(username):
    if request.method=="GET":
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
            if verify:
                return jsonify({
                    "message":"you have no account and therefore cant get any vehicle"
                })

            else:
                get_ownerid = vehicle_API_Queries.get_otherVehicleOwnerId(get_userid)
                verify_ownerid = vehicle_API_Queries.verify_ownerid_in_OtherVehicles(get_ownerid)
                if verify_ownerid:
                    get_vehicle_info = vehicle_API_Queries.get_otherVehicles(get_ownerid)
                    return jsonify(get_vehicle_info)

                else:
                    return jsonify({
                        "message":"You have not registered any vehicles"
                    })


        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


    elif request.method=="PUT":
        photo = request.json["photo_url"]
        car_type = request.json["car_type"]
        car_no = request.json["car_no"]
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
            if verify:
                return jsonify({
                    "message":"you have no account and therefore cant get any vehicle"
                })

            else:
                get_ownerid = vehicle_API_Queries.get_otherVehicleOwnerId(get_userid)
                verify_ownerid = vehicle_API_Queries.verify_ownerid_in_OtherVehicles(get_ownerid)
                if verify_ownerid:
                    update_info = vehicle_API_Queries.update_otherVehiclesInfo(photo,car_type,car_no)
                    return update_info

                else:
                    return jsonify({
                        "message":"You have not registered any vehicles therefore you cant update what you have not registered for"
                    })


        else:
            return jsonify({
                "message":"Account doesnt exist"
            })


    elif request.method=="DELETE":
        '''
            A function to verify if car number is in databse before deleting
        '''
        car_no = request.json["car_no"]
        verify_user_exist = vehicle_API_Queries.verify_username_in_db(username)
        if verify_user_exist:
            get_userid = vehicle_API_Queries.get_user_id(username)
            verify = vehicle_API_Queries.verify_otherVehicleOwner_in_db(get_userid)
            if verify:
                return jsonify({
                    "message":"you have no account and therefore cant delete any vehicle"
                })

            else:
                get_ownerid = vehicle_API_Queries.get_otherVehicleOwnerId(get_userid)
                verify_ownerid = vehicle_API_Queries.verify_ownerid_in_OtherVehicles(get_ownerid)
                if verify_ownerid:
                    delete_vehicle = vehicle_API_Queries.delete_otherVehicles(car_no)
                    return delete_vehicle,201

                else:
                    return jsonify({
                        "message":"You have not registered any vehicles therefore you cant update what you have not registered for"
                    })


        else:
            return jsonify({
                "message":"Account doesnt exist"
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