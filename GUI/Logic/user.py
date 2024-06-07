from Logic.database import *
from Logic.query_settings import *
import hashlib
import os

class User:
    def __init__(self, username=None):
        self.username = username
        self.isActive = True
        
    def add_user(self, uname, pword):
        # Create a new SHA-256 hash object
        sha256 = hashlib.sha256()
        
        # Hash the password with a salt
        salt = os.urandom(16)
        sha256.update(salt + pword.encode('utf-8'))
        hashed_password = sha256.hexdigest()
       
        
        # Store the salt and hashed password in the database
        query = (
            "insert into USER(username, salt, password, void) "
            "values(%s, %s, %s, %s)"
        )
        data = (uname, salt.hex(), hashed_password, 0)
        handle_transaction(query, data)

    def validate_user(self, input_id, input_pwd):
        # Retrieve the user's salt and hashed password from the database
        query = "select salt, password from USER where user_id = {}".format(input_id)
        result = handle_select(query)
        if not result:
            return False

        stored_salt, stored_hashed_password = result[0]

        # Create a new SHA-256 hash object
        sha256 = hashlib.sha256()

        # Hash the input password with the stored salt
        sha256.update(bytes.fromhex(stored_salt) + input_pwd.encode('utf-8'))
        input_hashed_password = sha256.hexdigest()

        # Compare the stored hashed password with the input hashed password
        return stored_hashed_password == input_hashed_password

    def add_activity(self, active_user, activity):
        # This is the place where the activity within the system will be accounted
        query = (
            "insert into ACTIVITY(act_user, activity)"
            "values(%s, %s)"
        )
        data = (active_user, activity)
        handle_transaction(query, data)
    
    def edit_user(self, user_id, categ, new_input):
        temp = "update USER set {} = ".format(categ)
        query = temp + "%s where user_id =  %s"
        data = (new_input, user_id)
        handle_transaction(query, data)
    
    def get_data(self, ref_id, categ):
        temp = "select {} from USER ".format(categ)
        query = temp + "where user_id = {}".format(ref_id)
        return handle_select(query)[0][0]
    
#u = User()
#u.add_user('Bowie', 'Shendi')
#print(u.validate_user(1, '123456'))
