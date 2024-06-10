from database import *
from query_settings import *

import re

class Message:
    def __init__(self):
        temp_client = "select CLIENT.name from CLIENT where client_id = "
        temp_tech = "select first_name from TECHNICIAN where technician_id = "

        self.tokens = {
            "cn" : (temp_client + "(SELECT client_id FROM SCHEDULE where schedule_id = {})"),
            "csd" : "select start_date from SCHEDULE where schedule_id = {}",
            "ced" : "select end_date from SCHEDULE where schedule_id = {}",
            "cti" : "select time_in from SCHEDULE where schedule_id = {}",
            "cto" : "select time_out from SCHEDULE where schedule_id = {}",
            "tn" : (temp_tech + "(SELECT technician_id FROM SCHEDULE where schedule_id = {})")
        }
        self.converted_token = []

    def convert_msg(self, ref_id,  msg_content):
        placeholders = ["cn", "csd", "ced", "cti", "cto", "tn"]

        pattern = r'@(\w+)'
        captured_tokens = re.findall(pattern, msg_content)
        
        for token in captured_tokens:
            query = self.tokens[token].format(ref_id)
            value = handle_select(query)[0][0]

            if type(value) is not str: # if the value is DATE
                value = value.strftime('%Y-%m-%d')

            self.converted_token.append(value)
        
        # Supporting Function
        def get_value(placeholder):
            try:
                index = placeholders.index(placeholder)
                return self.converted_token[index]
            except ValueError:
                return placeholder

        result = re.sub(pattern, lambda match: get_value(match.group(1)), msg_content)
        ###### THIS WHERE THE ARDUINO BEGINS ######
        return result
    

    def add_message(self, msg_categ, msg_format):
        query = "insert into MESSAGE (message_category, message) values (%s, %s)"
        data = (msg_categ, msg_format)
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

"""m = Message()
msg = "Hello @cn you have a service tomorrow @csd"
print(m.convert_msg(2,msg))
"""
