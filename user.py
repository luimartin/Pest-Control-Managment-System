from database import *
from query_settings import *
import hashlib
import os

class User:
    def __init__(self, username=None):
        self.username = username
        self.isActive = True
    
    # Add the admin account with SHA256 password encrypting and decryption
    def add_user(self, uname, pword):
        sha256 = hashlib.sha256()
        
        salt = os.urandom(16)
        sha256.update(salt + pword.encode('utf-8'))
        hashed_password = sha256.hexdigest()
       
        # Store the salt and hashed password in the database
        query = (
            "insert into USER(username, password, void, salt) "
            "values(%s, %s, %s, %s)"
        )
        data = (uname, hashed_password, 0, salt.hex())
        handle_transaction(query, data)

    # Validate user based from input id and password
    def validate_user(self, input_id, input_pwd):
        # Retrieve the user's salt and hashed password from the database
        query = "select salt, password from USER where user_id = {}".format(input_id)
        result = handle_select(query)
        if not result:
            return False

        stored_salt, stored_hashed_password = result[0]

        sha256 = hashlib.sha256()

        # Hash the input password with the stored salt
        sha256.update(bytes.fromhex(stored_salt) + input_pwd.encode('utf-8'))
        input_hashed_password = sha256.hexdigest()

        # Compare the stored hashed password with the input hashed password
        return stored_hashed_password == input_hashed_password

    # Changing of password
    def new_pass(self, user_id, new_pass, confirm_pass):
        if new_pass == confirm_pass:
            print("yun")
            sha256 = hashlib.sha256()
        
            salt = os.urandom(16)
            sha256.update(salt + new_pass.encode('utf-8'))
            hashed_password = sha256.hexdigest()
        
            query = (
                "update USER set password = %s, salt = %s"
                " where user_id = %s"
            )
            data = (hashed_password, salt.hex(), user_id)
            handle_transaction(query, data)

    # Validation of account based from the input userid and username for changing of password
    def cp_validate_user(self, user_id, username):
        query = "select user_id, username from USER where user_id = {}".format(user_id)
        uid = handle_select(query)[0][0]
        uname = handle_select(query)[0][1]

        if uid == user_id and uname == username:
            return True
        
        return False

    # User backlogs or auditing
    def add_backlogs(self, active_user, activity):
        # This is the place where the activity within the system will be accounted
        query = (
            "insert into ACTIVITY(act_user, activity)"
            "values(%s, %s)"
        )
        data = (active_user, activity)
        handle_transaction(query, data)
    
    # Editing of admin account information
    def edit_user(self, user_id, categ, new_input):
        temp = "update USER set {} = ".format(categ)
        query = temp + "%s where user_id =  %s"
        data = (new_input, user_id)
        handle_transaction(query, data)
    
    # Searching of admin account 
    def get_data(self, ref_id, categ):
        temp = "select {} from USER ".format(categ)
        query = temp + "where user_id = {}".format(ref_id)
        return handle_select(query)[0][0]

    
u = User()
#u.add_user('bianca', 'gojo')
#print(u.validate_user(24002, 'yuta'))
#print(u.cp_validate_user(24002, 'yuta'))
#u.new_pass(24002, 'yuta', 'yuta')