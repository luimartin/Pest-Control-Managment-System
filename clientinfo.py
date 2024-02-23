from Database import *
from QuerySettings import *

import Contract as Contract
import Schedule

class ClientInfo:
    def __init__(self):
        self.Contract = Contract()
        self.Schedule = Schedule()        
    
    def add_client_info(self, name, email, phone_num, address):
        query = (
            "insert into CLIENT(name, email, phone_num, address, status, void)"
            "values (%s, %s, %s, %s, %s, %s,)"
        )
        data = (name, email, phone_num, address, 'New', 0)
        handle_transaction(query, data)

    def edit_personal_info(self, ref_id, categ, new_input):
        temp = "update CLIENT set {} = ".format(categ) 
        query = temp + "%s where client_id = %s"
        data = (new_input, ref_id)
        handle_transaction(query, data)

    def get_data(self, ref_id, categ):
        temp = "select {} from CLIENT ".format(categ)
        query = temp + "where client_id = {}".format(ref_id)
        return handle_select(query)
        
    def search(self, input):
        query = "select * from CLIENT where name = {}".format("\'"+input+"\'")
        return handle_select(query)   

c = ClientInfo()
c.add_client_info('Bowie Company', 'bowie@example.com', '12345678912', 'San Juan')
print(c.search('Bowie Company'))