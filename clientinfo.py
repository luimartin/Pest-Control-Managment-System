from database import *
from query_settings import *

from contract import Contract
from schedule import Schedule

class ClientInfo:
    def __init__(self):
        self.Contract = Contract()
        self.Schedule = Schedule()        
    
    def add_client_info(self, name, email, phone_num, address):
        query = (
            "insert into CLIENT(name, email, phone_num, address, status, void)"
            "values (%s, %s, %s, %s, %s, %s)"
        )
        data = (name, email, phone_num, address, 'New', 0)
        handle_transaction(query, data)

    def contract_view(self, client_id):
        query = "select name, phone_num, address, email from client where client_id  = {}".format(client_id)
        return handle_select(query)

        
    def edit_personal_info(self, ref_id, categ, new_input):
        temp = "update CLIENT set {} = ".format(categ) 
        query = temp + "%s where client_id = %s"
        data = (new_input, ref_id)
        handle_transaction(query, data)

    
    def select_all_clients(self):
        query = "select client_id, name, phone_num, address from CLIENT where void = 0"
        return handle_select(query)

    
    def select_all_clients_void(self):
        query = "select client_id, name, phone_num, address, email from CLIENT where void = 1"
        return handle_select(query)


    def get_data(self, ref_id, categ):
        temp = "select {} from CLIENT ".format(categ)
        query = temp + "where client_id = {}".format(ref_id)
        return handle_select(query)
        
        
    """def search(self, input):
        query = "select * from CLIENT where name = {}".format("\'"+input+"\'")
        return handle_select(query)   
    """

    def search(self, input, void):
        query = """
            select client_id, name, phone_num, status from CLIENT 
            where (
            client_id LIKE '%{}%'
            OR name LIKE '%{}%'
            OR email LIKE '%{}%' 
            OR phone_num LIKE '%{}%' 
            OR address LIKE '%{}%' 
            OR status LIKE '%{}%'
            ) 
            and void = {}
        """.format(input, input, input, input, input, input, void)
        return handle_select(query)     


#c = ClientInfo()
#c.get_data(1, ("name, phone_num, address, email"))