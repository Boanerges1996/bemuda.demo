from db_service import get_db, close_db
from passlib.hash import sha256_crypt
import gc
from flask import jsonify,flash
import jwt


#--------------------USERS API QUERY FUNTIONS--------------------------------
def sign_up(firstname,lastname,othernames,username,tel_no,email,password,user_avatar):
    try:
        cur = get_db().cursor()
        query = '''
        INSERT INTO User_info 
        (firstname,lastname,othernames,username,telephone_number,email,user_password,user_avatar) 
            values(%s,%s,%s,%s,%s,%s, %s,%s)
            '''
        args = (firstname,lastname,othernames,username,tel_no,email,password,user_avatar)
        cur.execute(query,args)
        get_db().commit()
        gc.collect()#Gabbage collection
    except:
        return jsonify({
            "database":"connection problems"
        })

def sign_in(username,password):
    '''
        This handles user Login.
        If username is in an exception is returned
        If valid the password is fetched from the database and the supplied password is hashed
        with the given password. 
        If it returns through then user is login and given a token.
        Else an invalid password is throne to the user
    '''
    try:
        cur = get_db().cursor()
        query = '''
        SELECT user_password FROM User_info WHERE username=%s
        '''
        cur.execute(query,(username,))
        rv = str(cur.fetchall()[0])
        gc.collect()
    except:
        return None
        
    if rv:
        rv = rv[2:79]
        if sha256_crypt.verify(password,rv):
            query_all_data = '''
            SELECT user_id,firstname,lastname,othernames,username,telephone_number
            ,email FROM User_info WHERE (username=%s AND user_password=%s)
            '''
            args = (username,rv)
            cur.execute(query_all_data,args)
            search = cur.fetchall()
            gc.collect()
            return jsonify({"user_id":search[0][0],"firstname":search[0][1],"lastname":search[0][2]
            , "othername":search[0][3],"username":search[0][4],"telephone_number":search[0][5]
            ,"email":search[0][6]})
        else:
            gc.collect()
            return None
        
   
    



def verify_token(decode_token):
    '''
        This gets a decoded token from the user and validates if the username
        actually exists in the database

    '''
    try:
        cursor = get_db().cursor()
        query = '''
                SELECT username FROM User_info WHERE username=%s
                '''
        cursor.execute(query,decode_token)
        verify_person = cursor.fetchall()[0]
    except:
        return None
    return verify_person



def user_profile_info(username):
    cursor = get_db().cursor()
    query = '''
            SELECT firstname,lastname,othernames,username,telephone_number
            ,email,user_avatar FROM User_info WHERE username=%s 
            '''
    try:
        cursor.execute(query,(username,))
        my_profile_info = cursor.fetchall()[0]
    except:
        return jsonify({
            "message":"invalid username"
        })

    return {
        'firstname':my_profile_info[0],
        'lastname':my_profile_info[1],
        'othernames':my_profile_info[2],
        'username':my_profile_info[3],
        'telephone_number':my_profile_info[4],
        'email':my_profile_info[5],
        'user_avatar':my_profile_info[6]
    }


def verify_username_in_db(username):
    '''
        This helps in validating whether a users username is found in the database
    '''
    cursor = get_db().cursor()
    query = '''
            SELECT * FROM User_info WHERE username=%s
    '''
    cursor.execute(query,(username,))
    search_results = cursor.fetchall()
    if search_results == tuple():
        return None
    else:
        return True



def update_user_info(firstname,lastname,othernames,username,tel_no,email,password,user_avatar,actual_username):
    '''
        This function helps updates a users information provided from the front-end,
        First of all, the username is verified before updating. After updating, we
        fetch the updated information and return it
    '''
    try:
        cursor = get_db().cursor()
        query = '''
            UPDATE User_info SET firstname=%s,lastname=%s,othernames=%s,username=%s,
            telephone_number=%s,email=%s,user_password=%s,user_avatar=%s WHERE username=%s
        '''
        cursor.execute(query,(firstname,lastname,othernames,username,tel_no,email,password,user_avatar,actual_username))
        get_db().commit()
    except:
        return jsonify({
            "message":"You can't update user info"
        })
    cur = get_db().cursor()
    query_two = '''
            SELECT firstname,lastname,othernames,username,telephone_number
            ,email,user_avatar FROM User_info WHERE username=%s 
            '''
    cur.execute(query_two,(actual_username,))
    results = cur.fetchall()[0]
    user_updated_info = jsonify({
        "firstname":results[0],
        "lastname":results[1],
        "othernames":results[2],
        "username":results[3],
        "telephone_number":results[4],
        "email":results[5],
        "user_avatar":results[6]
    })
    return user_updated_info



def verify_user_admin_status(username):

        cursor = get_db().cursor()
        query = '''
            SELECT admin_status FROM User_info WHERE username=%s
        '''
        cursor.execute(query,(username,))
        admin_status = cursor.fetchall()[0]

        if admin_status[0]:
            return True
        else:
            return False

def get_user_id(username):
    cursor = get_db().cursor()
    query = '''
        SELECT user_id FROM User_info WHERE username=%s
    '''
    cursor.execute(query,(username,))
    user_id = cursor.fetchall()[0]
    if user_id[0]:
        return user_id[0]
    else:
        return jsonify({
            "message":"User doesnt exist"
        })

def delete_user_from_db(username):
    cursor = get_db().cursor()
    delete_user_query = '''
        DELETE FROM User_info WHERE username=%s
    '''
    cursor.execute(delete_user_query,(username,))
    get_db().commit()
    return jsonify({
        "message":"User deleted by admin"
    })

#-----------------END USERS API QUERY----------------------------------------#




#--------------------DRIVER API------------------------------------------------#


def register_driver(date_of_birth,residential_address,license_no,sex,user_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO driver_info (date_of_birth,residential_address,license_no,
        sex,user_id)VALUES(%s,%s,%s,%s,%s)
    '''
    cursor.execute(query,(date_of_birth,residential_address,license_no,sex,int(user_id),))
    get_db().commit()
    return jsonify({
        "message":"Driver registered successfully"
    })



def verify_userID_in_driver_db(userid):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM driver_info WHERE user_id=%s
    '''
    cursor.execute(query,(userid,))
    fetchDriver_info = cursor.fetchall()
    if fetchDriver_info==tuple():
        return False
    else:
        return True



def isDriver(username):

    user_id = get_user_id(username)
    user_id_in_db = verify_userID_in_driver_db(user_id)
    return user_id_in_db



def get_driver_info(username):
    cursor = get_db().cursor()
    query = '''
        SELECT User_info.firstname,User_info.lastname,User_info.othernames,
        User_info.user_avatar,User_info.email,User_info.telephone_number,
        User_info.username, driver_info.date_of_birth,driver_info.residential_address,
        driver_info.license_no,driver_info.sex
        FROM 
        User_info
        JOIN driver_info ON User_info.user_id=driver_info.user_id WHERE
        username=%s
    '''
    cursor.execute(query,(username,))
    query_results = cursor.fetchall()[0]
    
    query_results = jsonify({
        "firstname":query_results[0],
        "lastname":query_results[1],
        "othernames":query_results[2],
        "user_avatar":query_results[3],
        "email":query_results[4],
        "telephone number":query_results[5],
        "username":query_results[6],
        "date of birth":query_results[7],
        "residential address":query_results[8],
        "license number":query_results[9],
        "sex":query_results[10]
    })
    return query_results



def update_driver_info(dateOfBirth,Residential,license,sex,user_id):
    cursor = get_db().cursor()
    query = '''
        UPDATE driver_info SET date_of_birth=%s,residential_address=%s,
        license_no=%s,sex=%s WHERE user_id = %s
    '''
    cursor.execute(query,(dateOfBirth,Residential,license,sex,user_id,))
    get_db().commit()
    gc.collect()
    return jsonify({
        "message":"Driver information updated sucessfully"
    })




def check_if_driver_registered(user_id):
    '''
        It checks if driver info is already registered, so that no USER can 
        register twice in the database to achieve a 1 to 1 relationship
    '''
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM driver_info WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    if_registered = cursor.fetchall()
    if if_registered==tuple():
        return False
    else:
        return True




def delete_driver(user_id):
    cursor= get_db().cursor()
    query = '''
        DELETE FROM driver_info WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    get_db().commit()
    return jsonify({
        "message":"Driver deleted from database"
    })

# ----------------------------END DRIVER API--------------------------------




# --------------------------VEHICLE API--------------------------------------
# --------------------------BUS----------------------------------------------
def check_id_bus_owner_db(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM Bus_owners WHERE user_id =%s
    '''
    cursor.execute(query,(int(user_id),))
    if_registered = cursor.fetchall()
    if if_registered==tuple():
        return True
    else:
        return False

def register_bus_owner(company_name,location,owner_avatar,user_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO Bus_owners (company_name,location,owner_avatar,user_id)
        VALUES(%s,%s,%s,%s)
    '''
    cursor.execute(query,(company_name,location,owner_avatar,int(user_id),))
    get_db().commit()
    return jsonify({
        "message":"Bus owner registered successfully"
    })

def check_companyName_in_busOwner_db(company_name):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM Bus_owners WHERE company_name=%s
    '''
    cursor.execute(query,(company_name,))
    if_registered = cursor.fetchall()
    if if_registered==tuple():
        return False
    
    else:
        return True
    

def get_busOwner_info(user_id):
    cursor= get_db().cursor()
    query = '''
        SELECT company_name,location,owner_avatar FROM Bus_owners WHERE
        user_id = %s
    '''
    cursor.execute(query,(int(user_id),))
    bus_owner_info = cursor.fetchall()[0]
    bus_owner_information = {
        "company_name":bus_owner_info[0],
        "location":bus_owner_info[1],
        "owner_avatar":bus_owner_info[2]
    }
    return bus_owner_information


def update_busOwner_info(company_name,location,owner_avatar,user_id):
    cursor = get_db().cursor()
    query = '''
        UPDATE Bus_owners SET company_name=%s,location=%s,owner_avatar=%s WHERE user_id=%s
    '''
    cursor.execute(query,(company_name,location,owner_avatar,int(user_id),))
    get_db().commit()
    return jsonify({
        "message":"You bus owner info is updated"
    })



def check_userid_in_busOwners_db(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM Bus_owners WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()
    if result==tuple():
        return False
    else:
        return True


def get_busOwner_id(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT owner_id FROM Bus_owners WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    owner_id = cursor.fetchall()[0]
    return owner_id[0]


def delete_busOwner(user_id):
    cursor = get_db().cursor()
    query='''
        DELETE FROM Bus_owners WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    get_db().commit()
    return jsonify({
        "message":"Bus owner account deleted successfully"
    })

def register_bus(bus_photo,car_no,capacity,owner_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO Buses (bus_photo,car_no,capacity,owner_id) 
        VALUES (%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(bus_photo,car_no,capacity,int(owner_id),))

    except:
        return jsonify({
            "message":"Bus number already exist"
        })
    get_db().commit()
    return jsonify({
        "message":"Bus registered successfully"
    })


def check_owner_id_in_buses_db(owner_id):
    cursor = get_db().cursor()
    query = '''
        SELECT owner_id FROM Buses WHERE owner_id=%s
    '''
    cursor.execute(query,(int(owner_id),))
    result = cursor.fetchall()
    if result==tuple():
        return False
    else:
        return True



def trial_looping():
    cursor = get_db().cursor()
    query = '''
        SELECT username,firstname,lastname,email,telephone_number,
        user_avatar FROM User_info
    '''
    cursor.execute(query)
    rv = cursor.fetchall()
    users ={}
    i=1
    for user in rv:
        users.update({"user"+str(i):user})
        i=i+1
    
    
    return jsonify({
        "message":users
    })


def get_allBuses_of_busOwner(owner_id):
    cursor = get_db().cursor()
    query = '''
        SELECT bus_photo,car_no,capacity FROM Buses WHERE
        owner_id = %s
    '''
    cursor.execute(query,(int(owner_id),))
    allUserBuses = {}
    allBuses = cursor.fetchall()
    i = 0
    for businfo in allBuses:
        allUserBuses.update({
            "Bus "+str(i):{
                "bus_image_url":businfo[0],
                "car number":businfo[1],
                "capacity":businfo[2]
            }
        })
        i= i+1
    return allUserBuses


def update_bus(bus_url,capacity,car_no):
    cursor = get_db().cursor()
    query = '''
        UPDATE Buses SET bus_photo=%s,capacity=%s WHERE car_no=%s
    '''
    cursor.execute(query,(bus_url,int(capacity),car_no))
    get_db().commit()
    return jsonify({
        "message":"Bus info updated"
    })


def delete_bus(car_no):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM Buses WHERE car_no=%s
    '''
    cursor.execute(query,(car_no,))
    get_db().commit()

    return jsonify({
        "message":"Bus deleted successfully"
    })

# ----------------------------------------END BUSES API---------------------------------------------


# -----------------------------------------TROSKIS API START---------------------------------------
def verify_troski_owner_in_db(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM Troski_owner WHERE user_id = %s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()
    if result==tuple():
        return True
    else:
        return False


def register_trokis_owner(owner_photo,location,user_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO Troski_owner (owner_photo,location,user_id) VALUES (%s,%s,%s)
    '''
    cursor.execute(query,(owner_photo,location,int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Troski owner register"
    })


def get_troski_owner_info(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT owner_photo,location FROM Troski_owner WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()[0]
    return {
        "owner_photo":result[0],
        "location":result[1]
    }


def update_trokis_owner_info(owner_photo,location,user_id):
    cursor = get_db().cursor()
    query = '''
        UPDATE Troski_owner SET owner_photo=%s,location=%s WHERE user_id=%s
    '''
    cursor.execute(query,(owner_photo,location,int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Trokis owner info updated"
    })


def delete_troski_owner(user_id):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM Troski_owner WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Troski owner info deleted"
    })


def get_troski_owner_id(user_id):
    cursor= get_db().cursor()
    query = '''
        SELECT owner_id FROM Troski_owner WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()[0]
    return result[0]


def register_troski(photo,car_no,capacity,owner_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO Troskis (photo,car_no,capacity,owner_id) VALUES (%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(photo,car_no,int(capacity),int(owner_id),))
        get_db().commit()
    except:
        return jsonify({
            "message":"Vehicle with that number already registered"
        })

    return jsonify({
        "message":"Trokis registered"
    })


def get_all_troskis(owner_id):
    cursor = get_db().cursor()
    query = '''
        SELECT photo,car_no,capacity FROM Troskis WHERE
        owner_id = %s
    '''
    cursor.execute(query,(int(owner_id),))
    allUserTroskis = {}
    allTroskis = cursor.fetchall()
    i = 0
    for businfo in allTroskis:
        allUserTroskis.update({
            "Troski "+str(i):{
                "Troskis_image_url":businfo[0],
                "car number":businfo[1],
                "capacity":businfo[2]
            }
        })
        i= i+1
    # Will deal with whether car number is wrongly given
    return allUserTroskis



def update_troski(photo_url,capacity,car_no):
    cursor = get_db().cursor()
    query = '''
        UPDATE Troskis SET photo=%s,capacity=%s WHERE car_no=%s 
    '''
    try:
        cursor.execute(query,(photo_url,int(capacity),car_no,))
        get_db().commit()
    except:
        return jsonify({
            "message":"Invalid car number"
        })

    return jsonify({
        "message":"Bus info updated"
    })


def delete_troski(car_no):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM Troskis WHERE car_no=%s
    '''
    try:
        cursor.execute(query,(car_no,))
        get_db().commit()
    except:
        return jsonify({
            "message":"This car number doesnt exist"
        })

    return jsonify({
        "message":"Bus deleted successfully"
    })
# ----------------------------------------END TROSKIS---------------------------------------


# ----------------------------------------PRIVATE CAR---------------------------------------
def verify_userID_in_privateCArOwner(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM private_car_users WHERE user_id = %s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()
    if result==tuple():
        return True
    else:
        return False


def register_privateCarOwner(location,user_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO private_car_users (location,user_id) VALUES (%s,%s)
    '''
    cursor.execute(query,(location,int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Private car owner registered"
    })



def get_privateCarOwnerInfo(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT location FROM private_car_users WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()[0]
    return {
        "location":result[0]
    }

def update_privateCarOwner_info(location,user_id):
    cursor = get_db().cursor()
    query = '''
        UPDATE private_car_users SET location=%s WHERE user_id=%s
    '''
    cursor.execute(query,(location,int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Private car owner info updated"
    })

def delete_privateCarOwner_info(user_id):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM private_car_users WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Pricate car owner deleted"
    })




def get_privateCar_ownerId(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT owner_id FROM private_car_users WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()[0]
    return result[0]


def register_privateCar(car_type,car_photo,car_no,owner_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO private_cars (car_type,car_photo,car_number,owner_id) VALUES (%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(car_type,car_photo,car_no,int(owner_id),))
        get_db().commit()
    except:
        return jsonify({
            "message":"Vehicle with that number already registered"
        })

    return jsonify({
        "message":"Private car registered successfully"
    })


def get_privateCar(owner_id):
    cursor = get_db().cursor()
    query = '''
        SELECT car_type,car_photo,car_number FROM private_cars WHERE
        owner_id = %s
    '''
    cursor.execute(query,(int(owner_id),))
    allUserprivateCars = {}
    allCars = cursor.fetchall()
    i = 0
    for businfo in allCars:
        allUserprivateCars.update({
            "Car "+str(i):{
                "Car_type":businfo[0],
                "car_photo":businfo[1],
                "car_number":businfo[2]
            }
        })
        i= i+1
    # Will deal with whether car number is wrongly given
    return allUserprivateCars


def update_car(car_type,car_photo,car_no):
    cursor = get_db().cursor()
    query = '''
        UPDATE private_cars SET car_type=%s,car_photo=%s WHERE car_number=%s
    '''
    
    cursor.execute(query,(car_type,car_photo,car_no,))
    result = cursor.fetchall()
    if result==tuple():
        return jsonify({
            "message":"Car number doesnt exist"
        })
    get_db().commit()

    

    return jsonify({
        "message":"Private car owner info updated"
    })

def delete_car(car_no):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM private_cars WHERE car_number=%s
    '''
    try:
        cursor.execute(query,(car_no,))
        get_db().commit()
    except:
        return jsonify({
            "message":"Car number doesnt exist and therefore cant delete"
        })

    return jsonify({
        "message":"Private car deleted"
    })

    # ------------------------------------END PRIVATE CARS--------------------------


    # --------------------------OTHER VEHICLES--------------------------------------
def verify_otherVehicleOwner_in_db(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT * FROM other_vehicle_users WHERE user_id = %s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()
    if result==tuple():
        return True
    else:
        return None



def register_other_owners(photo,location,user_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO other_vehicle_users (photo,location,user_id) VALUES (%s,%s,%s)
    '''
    cursor.execute(query,(photo,location,int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Vehicle registered successfully"
    })
    


def get_otherVehicleOwnersInfo(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT photo,location FROM other_vehicle_users WHERE user_id = %s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()[0]
    return {
        "photo_url":result[0],
        "location":result[1]
    }


def update_OtherVehicleOwnersInfo(photo_url,location,user_id):
    cursor = get_db().cursor()
    query = '''
        UPDATE other_vehicle_users SET photo=%s,location=%s WHERE user_id=%s
    '''
    
    cursor.execute(query,(photo_url,location,int(user_id),))
    get_db().commit()
    return jsonify({
        "message":"Other vehicle info updated"
    })


def delete_OtherVehicleOwnersInfo(user_id):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM other_vehicle_users WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    get_db().commit()

    return jsonify({
        "message":"Other vehicle owner info deleted"
    })



def get_otherVehicleOwnerId(user_id):
    cursor = get_db().cursor()
    query = '''
        SELECT owner_id FROM other_vehicle_users WHERE user_id=%s
    '''
    cursor.execute(query,(int(user_id),))
    result = cursor.fetchall()[0]
    return result[0]


def register_OtherVehicles(photo,car_no,car_type,owner_id):
    cursor = get_db().cursor()
    query = '''
        INSERT INTO other_vehicles (photo,car_no,car_type,owner_id) VALUES (%s,%s,%s,%s)
    '''
    try:
        cursor.execute(query,(photo,car_no,car_type,int(owner_id),))
        get_db().commit()
        return jsonify({
            "message":"Car registered successfully"
        })

    except:
        return jsonify({
            "message":"car number already exists"
        })  
    


def verify_ownerid_in_OtherVehicles(owner_id):
    cursor=get_db().cursor()
    query = '''
        SELECT * FROM other_vehicles WHERE owner_id=%s
    '''
    cursor.execute(query,(int(owner_id),))
    result = cursor.fetchall()[0]

    if result == tuple():
        return False

    else:
        return True




def get_otherVehicles(owner_id):
    cursor = get_db().cursor()
    query = '''
        SELECT photo,car_no,car_type FROM other_vehicles WHERE owner_id =%s
    '''
    cursor.execute(query,(int(owner_id),))
    result = cursor.fetchall()
    allData = {}
    i=0

    for values in result:
        allData.update({
            "Car"+str(i):{
                "photo_url":values[0],
                "car_number":values[1],
                "car_type":values[2]
            }
        })
        i=i+1
    return allData,201

def update_otherVehiclesInfo(photo,car_type,car_no,):
    cursor = get_db().cursor()
    query = '''
        UPDATE other_vehicles SET photo=%s,car_type=%s WHERE car_no=%s
    '''
    try:
        cursor.execute(query,(photo,car_type,car_no,))
        get_db().commit()
        return jsonify({
            "message":"Information updated"
        })
    except:
        return jsonify({
            "message":"Car number doesnt exist"
        }),201


def delete_otherVehicles(car_no):
    cursor = get_db().cursor()
    query = '''
        DELETE FROM other_vehicles WHERE car_no=%s
    '''  
    cursor.execute(query,(car_no,))  
    get_db().commit()
    return jsonify({
        "message":"Car deleted successfully"
    })

