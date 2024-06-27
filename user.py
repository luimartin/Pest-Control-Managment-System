from database import *
from query_settings import *
import hashlib
import os, random
from datetime import datetime


class User:
    security_question = [
            "What is the name of your pet?",
            "What is your favorite food of all time?",
            "What was the first game you played?",
            "What is the toy/stuffed animal you like the most as a kind?",
            "What was your dream job?",
            "What was the first thing you learned to cook?",
            "What is your most listened song ever?",
            "Who is your favorite actor/actress?",
            "Who is your favorite cartoon/anime character?",
            "How did you met your crush?"
    ]

    def __init__(self, username=None):
        self.username = username
        self.isActive = True

    
    # Add the admin account with SHA256 password encrypting and decryption
    def add_user(self, uname, pword, q1, a1, q2, a2):
        sha256 = hashlib.sha256()
        
        salt = os.urandom(16)
        sha256.update(salt + pword.encode('utf-8'))
        hashed_password = sha256.hexdigest()
       
        # Store the salt and hashed password in the database
        query = (
            "insert into USER(username, password, salt, question1, answer1, question2, answer2, void) "
            "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (uname, hashed_password, salt.hex(), q1, a1, q2, a2, 0)
        handle_transaction(query, data)

    # Validate user based from input id and password
    def validate_user(self, input_id, input_pwd):
        # Retrieve the user's salt and hashed password from the database
        query = "select salt, password from USER where user_id = '{}'".format(input_id)
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
            print("Successfully Changed")
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
            return True
        
        return False

    # Validation of account based from the input userid and username for changing of password
    def cp_validate_user(self, user_id, username):
        query = "select user_id, username from USER where user_id = '{}'".format(user_id)
        
        uid = handle_select(query)[0][0]
        uname = handle_select(query)[0][1]


        if uid == user_id and uname == username:
            return True
        
        return False
# q1, a1, q2, a2
    def cp_questions(self, user_id, a1, a2):
        query = "select answer1, answer2 from user where user_id = '{}'".format(user_id)
        ans = handle_select(query)

        if ans[0][0] == a1 and ans[0][1] == a2:
            return True
        return False
    
    # User backlogs or auditing
    def add_backlogs(self, active_user, activity):
        # This is the place where the activity within the system will be accounted
        query = (
            "insert into ACTIVITY(act_user_id, activity, dateact)"
            "values(%s, %s, %s)"
        )
        data = (active_user, activity, datetime.today())
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
        query = temp + "where user_id = '{}'".format(ref_id)
        return handle_select(query)
    
    def show_userlog(self):
        query = """
            select * from activity;
    """ 
        return handle_select(query)
    
    def show_id(self):
        query = """
        select user_id, username from user;
    """ 
        return handle_select(query)

#u = User()
#print(u.get_data(11, 'question1, answer1, question2, answer2'))
#print(u.show_id())
#print(u.get_data(4, ("question1, question2")))
#print(u.cp_questions(4,"Human", "Sugar Baby"))
#u.add_user("joy", "030709", "What is the name of your pet?", "fallfee", "What is your favorite food of all time?", "sinigang")
#u.add_user("cris", "030709", "What was the first game you played?", "jackstone", "What is the toy/stuffed animal you like the most as a kid?", "giraffe")
#u.add_user("doctora", "030709", "What was your dream job?", "doctor", "What was the first thing you learned to cook?", "hotdog")
#u.add_user("gil", "030709", "What is your most listened song ever?", "supershy", "What is the toy/stuffed animal you like the most as a kid?", "dog")
