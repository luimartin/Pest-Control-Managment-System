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

    def add_user(self, uname, pword, q1, a1, q2, a2):
        # Hash and store the username
        sha256 = hashlib.sha256()
        uname_salt = os.urandom(16)
        sha256.update(uname_salt + uname.encode('utf-8'))
        hashed_uname = sha256.hexdigest()

        # Hash and store the password
        sha256 = hashlib.sha256()  # Reset the hasher
        pword_salt = os.urandom(16)
        sha256.update(pword_salt + pword.encode('utf-8'))
        hashed_password = sha256.hexdigest()

        # Hash and store the first security question answer
        sha256 = hashlib.sha256()  # Reset the hasher
        a1_salt = os.urandom(16)
        sha256.update(a1_salt + a1.encode('utf-8'))
        hashed_a1 = sha256.hexdigest()

        # Hash and store the second security question answer
        sha256 = hashlib.sha256()  # Reset the hasher
        a2_salt = os.urandom(16)
        sha256.update(a2_salt + a2.encode('utf-8'))
        hashed_a2 = sha256.hexdigest()

        # Store the salts and hashed values in the database
        query = (
            "INSERT INTO USER(username, password, salt, question1, answer1, question2, answer2, void, uname_salt, a1_salt, a2_salt) "
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (hashed_uname, hashed_password, pword_salt.hex(), q1, hashed_a1, q2, hashed_a2, 0, uname_salt.hex(), a1_salt.hex(), a2_salt.hex())
        handle_transaction(query, data)

    def validate_user(self, input_id, username, input_pwd):
        query = "SELECT uname_salt, salt, password FROM USER WHERE BINARY user_id = '{}'".format(input_id)
        result = handle_select(query)
        
        if not result:
            return False

        stored_uname_salt, stored_pword_salt, stored_hashed_password = result[0]

        sha256 = hashlib.sha256()

        # Hash the input username with the stored username salt
        sha256.update(bytes.fromhex(stored_uname_salt) + username.encode('utf-8'))
        input_hashed_uname = sha256.hexdigest()

        # Retrieve the stored hashed username for validation
        query = "SELECT username FROM USER WHERE BINARY user_id = '{}'".format(input_id)
        stored_hashed_uname = handle_select(query)[0][0]

        if input_hashed_uname != stored_hashed_uname:
            return False

        # Hash the input password with the stored password salt
        sha256.update(bytes.fromhex(stored_pword_salt) + input_pwd.encode('utf-8'))
        input_hashed_password = sha256.hexdigest()

        return stored_hashed_password == input_hashed_password

    def new_pass(self, user_id, new_pass, confirm_pass):
        if new_pass == confirm_pass:
            print("Successfully Changed")
            sha256 = hashlib.sha256()
        
            salt = os.urandom(16)
            sha256.update(salt + new_pass.encode('utf-8'))
            hashed_password = sha256.hexdigest()
        
            query = (
                "UPDATE USER SET password = %s, salt = %s"
                " WHERE user_id = %s"
            )
            data = (hashed_password, salt.hex(), user_id)
            handle_transaction(query, data)
            return True
        
        return False

    def cp_questions(self, user_id, input_answer1, input_answer2):
        # Retrieve the stored answers and salts
        query = "SELECT answer1, a1_salt, answer2, a2_salt FROM USER WHERE user_id = {}".format(user_id)
        result = handle_select(query)
        
        if not result:
            return False

        stored_hashed_a1, a1_salt, stored_hashed_a2, a2_salt = result[0]

        sha256 = hashlib.sha256()

        # Hash the first input answer with the stored salt
        sha256.update(bytes.fromhex(a1_salt) + input_answer1.encode('utf-8'))
        input_hashed_a1 = sha256.hexdigest() 

        print(input_hashed_a1)
        print(stored_hashed_a1)

        sha256 = hashlib.sha256()
        # Hash the second input answer with the stored salt
        sha256.update(bytes.fromhex(a2_salt) + input_answer2.encode('utf-8'))
        input_hashed_a2 = sha256.hexdigest()

        print(input_hashed_a2)
        print(stored_hashed_a2)

        # Compare the hashed input answers with the stored hashed answers
        return stored_hashed_a1 == input_hashed_a1 and stored_hashed_a2 == input_hashed_a2

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

u = User()
print(u.cp_questions(1, "fallfee", "sinigang"))
#print(u.validate_user(1, "joy", "030709"))
#print(u.get_data(11, 'question1, answer1, question2, answer2'))
#print(u.show_id())
#print(u.get_data(4, ("question1, question2")))
#print(u.cp_questions(4,"Human", "Sugar Baby"))
#u.add_user("joy", "030709", "What is the name of your pet?", "fallfee", "What is your favorite food of all time?", "sinigang")
#u.add_user("cris", "030709", "What was the first game you played?", "jackstone", "What is the toy/stuffed animal you like the most as a kid?", "giraffe")
#u.add_user("doctora", "030709", "What was your dream job?", "doctor", "What was the first thing you learned to cook?", "hotdog")
#u.add_user("gil", "030709", "What is your most listened song ever?", "supershy", "What is the toy/stuffed animal you like the most as a kid?", "dog")
