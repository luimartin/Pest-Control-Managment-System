from database import *
from query_settings import *

class Message:
    def __init__(self):
        pass
    
    def add_message(self, msg_categ, msg_format):
        query = "insert into MESSAGE (message_category, message, void) values (%s, %s, %s)"
        data = (msg_categ, msg_format, 0)
        handle_transaction(query, data)
    
    def edit_message(self, msg_id, new_categ, new_input):
        temp = "update MESSAGE set message_category = %s, message = %s "
        query = temp + "where message_id = %s"
        data = (new_categ, new_input, msg_id)
        handle_transaction(query, data)
    
    def get_data(self, msg_id, categ):
        temp = "select {} from MESSAGE ".format(categ)
        query = temp + "where message_id = {}".format(msg_id)
        return handle_select(query)

m = Message()
