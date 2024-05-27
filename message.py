from database import *
from query_settings import *

import re

class Message:
    def __init__(self):
        self.tokens = {
            "cn" : "select name from CLIENT where client_id = ",
            "csd" : "select start_date from SCHEDULE where schedule_id = ",
            "ced" : "select end_date from SCHEDULE where schedule_id = ",
            "cti" : "select time_in from SCHEDULE where schedule_id = ",
            "cto" : "select time_out from SCHEDULE where schedule_id = ",
            "tn" : "select first_name from TECHNICIAN where technician_id = "
        }

    def convert_msg(self, ref_id,  msg_content):
        converted_token = []
        
        pattern = r'@(\w+)'
        captured_tokens = re.findall(pattern, msg_content)
        
        for token in captured_tokens:
            temp = self.tokens[token]
            query = temp + "%s"
            data = (ref_id)
            value = handle_transaction(query, data)
            converted_token.append(value)
        
        result = re.sub(pattern, lambda match: converted_token[int(match.group(1)) - 1])
        ###### THIS WHERE THE ARDUINO BEGINS ######
    
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
