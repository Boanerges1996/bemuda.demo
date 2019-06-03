from db_service import get_db, close_db
from passlib.hash import sha256_crypt
import gc
from flask import jsonify,flash
import jwt
from flask import current_app as app

def sign_up(firstname,lastname,othernames,username,tel_no,email,password):
    cursor = get_db().cursor()
    query= '''
        INSERT INTO user_info (firstname,lastname,othernames,telephone_number,
        email,username,user_password) VALUES (%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(firstname,lastname,othernames,tel_no,email,username,password,))
        get_db().commit()
        queryTwo = '''
            SELECT user_id,user_avatar,isAdmin FROM user_info WHERE username=%s
        '''
        cursor.execute(queryTwo,(username,))
        some_info = cursor.fetchall()[0]
        mytoken = jwt.encode({"user":username},app.config["SECRET_KEY"])
        token = mytoken.decode('UTF-8')
        return {
            "id":some_info[0],
            "user_avatar":some_info[1],
            "token":token,
            "isAdmin":str(some_info[2])
        }
    except Exception as error:
        return jsonify({
            "message":"Either username,email or telephone number exists"
        })

def sign_in(username,password):
    cursor = get_db().cursor()
    query = '''
        SELECT user_password FROM user_info WHERE username=%s
    '''
    cursor.execute(query,(username,))
    result = cursor.fetchall()
    if result == tuple():
        return jsonify({
            "Message":"Invalid username"
        })
    else:
        myPassword=result[0][0]
        if sha256_crypt.verify(password,myPassword):
            queryTwo = '''
                SELECT user_id,firstname,lastname,othernames,username,email,telephone_number,
                user_avatar,isAdmin FROM user_info WHERE username=%s
            '''
            cursor.execute(queryTwo,(username,))
            mytoken = jwt.encode({"user":username},app.config["SECRET_KEY"])
            token = mytoken.decode("UTF-8")
            user_info = cursor.fetchall()[0]
            return jsonify({
                "user_id":user_info[0],
                "firstname":user_info[1],
                "lastname":user_info[2],
                "othernames":user_info[3],
                "username":user_info[4],
                "email":user_info[5],
                "telephone_number":user_info[6],
                "user_avatar":user_info[7],
                "isAdmin":user_info[8],
                "token":token
            })
        

def get_user_info(id):
    cursor = get_db().cursor()
    query = '''
        SELECT user_id,firstname,lastname,othernames,username,email,telephone_number,
                user_avatar FROM user_info WHERE user_id=%s
    '''
    cursor.execute(query,(int(id),))
    user_info = cursor.fetchall()
    if user_info == tuple():
        return jsonify({
            "message":"invalid user id"
        })
    else:
        return jsonify({
            "user_id":user_info[0][0],
            "firstname":user_info[0][1],
            "lastname":user_info[0][2],
            "othernames":user_info[0][3],
            "username":user_info[0][4],
            "email":user_info[0][5],
            "telephone_number":user_info[0][6],
            "user_avatar":user_info[0][7],
            
        })

def verify_token(decode_token):
    '''
        This gets a decoded token from the user and validates if the username
        actually exists in the database

    '''
    
    cursor = get_db().cursor()
    query = '''
            SELECT username FROM User_info WHERE username=%s
            '''
    cursor.execute(query,(decode_token,))
    verify_person = cursor.fetchall()
    if verify_person == tuple():
        return None
    else:
        return True


def update_user_info(firstname,lastname,othernames,username,tel_no,email,user_avatar,password,user_id):
    cursor = get_db().cursor()
    query = '''
        UPDATE user_info SET firstname=%s,lastname=%s,othernames=%s,username=%s,
        telephone_number=%s,email=%s,user_avatar=%s,user_password=%s WHERE user_id=%s
    '''
    try:   
        cursor.execute(query,(firstname,lastname,othernames,username,tel_no,email,user_avatar,password,int(user_id),))
        get_db().commit()
        return jsonify({
            "mesage":"user info updated"
        })
    except:
        return jsonify({
            "message":"invalid user id, you cant update"
        })
    
def verify_if_is_admin(id):
    cursor = get_db().cursor()
    query='''
        SELECT isAdmin FROM user_info WHERE user_id=%s
    '''
    cursor.execute(query,(int(id),))
    result = cursor.fetchall()
    if result== tuple():
        return jsonify({
            "message":"invalid id"
        })
    else:
        if result[0]==1:
            return True
        else:
            return False

def get_all_users():
    cursor = get_db().cursor()
    query = '''
        SELECT user_id,firstname,lastname,othernames,username,email,telephone_number,
                user_avatar FROM user_info
    '''
    cursor.execute(query)
    user_all_info = {}
    info = cursor.fetchall()
    i=1
    for user_info in info:
        user_all_info.update({"User"+str(i):{
            "user_id":user_info[0],
            "firstname":user_info[1],
            "lastname":user_info[2],
            "othernames":user_info[3],
            "username":user_info[4],
            "email":user_info[5],
            "telephone_number":user_info[6],
            "user_avatar":user_info[7]
        }})
        i=i+1
    return jsonify(user_all_info)


def delete_user(id):
    cursor= get_db().cursor()
    query = '''
        DELETE FROM user_info WHERE user_id=%s
    '''
    try:
        cursor.execute(query,(int(id),))
        get_db().commit()
        return jsonify({
            "message":"User deleted successfully"
        })
    except:
        return jsonify({
            "message":"Invalid user id and therefore cant delete user"
        })



def verify_id_in_user_info(id):
    cursor = get_db().cursor()
    query = '''
        SELECT username FROM user_info WHERE user_id=%s
    '''
    cursor.execute(query,(int(id),))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False
    

def verify_id_in_drivers(id):
    cursor = get_db().cursor()
    query = query = '''
        SELECT driver_id FROM drivers WHERE user_id=%s
    '''
    cursor.execute(query,(int(id),))
    result = cursor.fetchall()
    if result:
        return False
    else:
        return True





def register_driver(date_of_birth,license,sex,residential_address,id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO drivers (date_of_birth,license_no,sex,residential_address,
        user_id) VALUES (%s,%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(date_of_birth,license,sex,residential_address,int(id),))
        get_db().commit()
        return jsonify({
            "message":"Registered driver sucessfully"
        })

    except:
        return jsonify({
            "message":"License number already exist"
        })

def get_driver_info(id):
    cursor = get_db().cursor()
    query = '''
        SELECT user_info.firstname,user_info.lastname,user_info.othernames,user_info.username,
        user_info.email,user_info.telephone_number,user_info.user_avatar,
        drivers.date_of_birth,drivers.license_no,drivers.sex,drivers.residential_address
        FROM user_info
        JOIN drivers ON user_info.user_id=drivers.user_id WHERE user_info.user_id=%s
    '''
    cursor.execute(query,(int(id),))
    result = cursor.fetchall()
    return jsonify({
        "firstname":result[0][0],
        "lastname":result[0][1],
        "othername":result[0][2],
        "username":result[0][3],
        "email":result[0][4],
        "telephone_number":result[0][5],
        "user_avatar":result[0][6],
        "date_of_birth":result[0][7],
        "license":result[0][8],
        "sex":result[0][9],
        "residential_address":result[0][10],
        "user_id":id
    })




def update_driver_info(date_of_birth,license,sex,residential_address,id):
    cursor = get_db().cursor()
    query = '''
        UPDATE drivers SET date_of_birth=%s,license_no=%s,sex=%s,residential_address=%s
        WHERE user_id=%s
    '''
    cursor.execute(query,(date_of_birth,license,sex,residential_address,int(id),))
    get_db().commit()
    return jsonify({
        "message":"Update successful"
    })



def get_all_drivers():
    cursor = get_db().cursor()
    query = '''
        SELECT user_info.firstname,user_info.lastname,user_info.othernames,user_info.username,
        user_info.email,user_info.telephone_number,user_info.user_avatar,
        drivers.date_of_birth,drivers.license_no,drivers.sex,drivers.residential_address,
        drivers.user_id
        FROM 
            user_info
        INNER JOIN 
            drivers ON user_info.user_id=drivers.user_id
    '''
    
    cursor.execute(query)
    drivers_tuple = cursor.fetchall()
    i=1
    drivers={}
    for driver in drivers_tuple:
        drivers.update({
            "driver"+str(i):{
                "firstname":driver[0],
                "lastname":driver[1],
                "othername":driver[2],
                "username":driver[3],
                "email":driver[4],
                "telephone_number":driver[5],
                "user_avatar":driver[6],
                "date_of_birth":driver[7],
                "license":driver[8],
                "sex":driver[9],
                "residential_address":driver[10],
                "user_id":driver[11]
            }
        })
        i=i+1
    return jsonify(drivers)



def delete_driver(id):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM drivers WHERE user_id=%s
    '''
    try:
        cursor.execute(query,(int(id),))
        get_db().commit()
        return jsonify({
            "message":"User deleted successfully"
        })
    except:
        return jsonify({
            "message":"User id not a driver therefore cant be deleted"
        })


def register_vehicle(car_no,car_photo_url,vehicle_type,capacity,company_name,user_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO vehicles 
        (car_no,car_photo_url,vehicle_type,capacity,company_name,user_id)
        VALUES (%s,%s,%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(car_no,car_photo_url,vehicle_type,int(capacity),company_name,int(user_id),))
        get_db().commit()
        return True   

    except:
        return False



def get_all_vehicles():
    cursor = get_db().cursor()
    query = '''
        SELECT user_info.firstname,user_info.lastname,user_info.othernames,user_info.username,
        user_info.email,user_info.telephone_number,user_info.user_avatar,vehicles.car_no,
        vehicles.car_photo_url,vehicles.capacity,vehicles.vehicle_type,vehicles.company_name
        FROM user_info
        JOIN vehicles ON user_info.user_id=vehicles.user_id
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    vehicleUsers = {}
    i=0
    for vehicle in result:
        vehicleUsers.update({
            "user"+str(i):{
                "firstname":vehicle[0],
                "lastname":vehicle[1],
                "othername":vehicle[2],
                "username":vehicle[3],
                "email":vehicle[4],
                "telephone_number":vehicle[5],
                "user_avatar":vehicle[6],
                "car_no":vehicle[7],
                "car_photo_url":vehicle[8],
                "capacity":vehicle[9],
                "car_type":vehicle[10],
                "company_name":vehicle[11]
            }
        })
        i=i+1
    
    return jsonify(vehicleUsers)