from database import *
from query_settings import *


class User:
    def __init__(self):
        pass

    def add_user(self, uname, pword):
        query = (
            "insert into USER(username, password)"
            "values(%s, %s, %s)"
        )
        data = (uname, pword, 0)
        handle_transaction(query, data)
    
    def edit_user(self, user_id,  categ, new_input):
        temp = "update USER set {} = ".format(categ)
        query = temp + "%s where user_id =  %s"
        data = (new_input, user_id)
        handle_transaction(query, data)
    
    def get_data(self, ref_id, categ):
        temp = "select {} from USER ".format(categ)
        query = temp + "where user_id = {}".format(ref_id)
        return handle_select(query)[0][0]
