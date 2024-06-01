from database import *
from query_settings import *

import bcrypt

class User:
    def __init__(self, username=None):
        self.username = username
        self.isActive = True
        
    def add_user(self, uname, pword):
        hashed_password = bcrypt.hashpw(pword.encode('utf-8'), bcrypt.gensalt())

        query = (
            "insert into USER(username, password, void)"
            "values(%s, %s, %s)"
        )
        data = (uname, hashed_password, 0)
        handle_transaction(query, data)

    def validate_user(self, input_id, input_pwd):
        # This is the place where user's id and password will be validated
        query = "select password from USER where user_id = {}".format(input_id)
        user_pwd = handle_select(query)[0][0]

        if user_pwd is not None: return bcrypt.checkpw(input_pwd.encode('utf-8'), user_pwd.encode('utf-8'))
        else: return False

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
    
u = User()
#u.add_user('neille', '123456')
#print(u.validate_user(24000, '030709'))
