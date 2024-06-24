from database import *
from query_settings import *

import datetime

import re

class Message:
    def __init__(self):
        temp_client = "select CLIENT.name from CLIENT where client_id = "
        temp_tech = "select first_name from TECHNICIAN where technician_id = "

        # Fix token error from Technician
        self.tokens = {
            "cn" : (temp_client + "(SELECT client_id FROM SCHEDULE where schedule_id = {})"),
            "csd" : "select start_date from SCHEDULE where schedule_id = {}",
            "ced" : "select end_date from SCHEDULE where schedule_id = {}",
            "cti" : "select time_in from SCHEDULE where schedule_id = {}",
            "cto" : "select time_out from SCHEDULE where schedule_id = {}",
            "tn" : (temp_tech + "(select technician_id from SCHEDULE where schedule_id = {})")
        }
        self.converted_token = []

    def convert_msg(self, sched_id,  msg_content):
        # The msg_content should be retreived from database
        pattern = r'@(\w+)'
        captured_tokens = re.findall(pattern, msg_content)
        
        for token in captured_tokens:
            query = self.tokens[token].format(sched_id)
            value = handle_select(query)[0][0]
            
            if type(value) is datetime.date:
                value = value.strftime('%Y-%m-%d')
            
            if type(value) is datetime.timedelta:
                value = str(value)
        
            self.converted_token.append(value)
        
        # Supporting Function
        def get_value(placeholder):
            try:
                index = captured_tokens.index(placeholder)
                return self.converted_token[index]
            except ValueError:
                return placeholder

        result = re.sub(pattern, lambda match: get_value(match.group(1)), msg_content)
        ###### THIS WHERE THE ARDUINO BEGINS ######
        self.converted_token = []
        return result

    def add_message(self, msg_categ, msg_title, msg_format):
        query = "insert into MESSAGE (message_category, message, title) values (%s, %s, %s)"
        data = (msg_categ, msg_format, msg_title)
        handle_transaction(query, data)
    
    def edit_message(self, msg_id, new_categ, new_input, title):
        temp = "update MESSAGE set message_category = %s, message = %s, title = %s "
        query = temp + "where message_id = %s"
        data = (new_categ, new_input, title , msg_id)
        handle_transaction(query, data)
    
    def get_data(self, msg_id, categ):
        temp = "select {} from MESSAGE ".format(categ)
        query = temp + "where message_id = {}".format(msg_id)
        return handle_select(query)
    
    def search(self, input):
        query = f"""
            select * from MESSAGE 
            where (
            message_id LIKE '%{input}%'
            OR client_id LIKE '%{input}%'
            OR technician_id LIKE '%{input}%' 
            OR message_category LIKE '%{input}%' 
            OR message LIKE '%{input}%' 
            ) and void = 0
        """
        return handle_select(query) 

    def show_all(self):
        query = """
        select * from message;
        """
        return handle_select(query)
    
    def show_all_categ(self, categ):
        query = """
        select * from message where message_category = '{}';
        """.format(categ)
        return handle_select(query)
    
    def show_specific(self, id):
        query = """
        select * from message where message_id = {}
        """.format(id)
        return handle_select(query)
m = Message()
#print(m.convert_msg(28, m.get_data(1, 'message')))
#print(m.get_data(7, 'message'))
#print(m.show_specific(7))
print(m.show_all_categ('Client'))
