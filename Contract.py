from Database import *
from QuerySettings import *

from ClientInfo import ClientInfo

class Contract:
    def __init__(self):
        self.ClientInfo = ClientInfo()
        pass

    def add_contract(self, ref_id, problem, service_type, start_date, end_date, square_meter, unit, price):
        query = (
            "insert into CONTRACT (client_id, problem, service_type, start_date, end_date, square_meter, unit, price)"
            "values (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, problem, service_type, start_date, end_date, square_meter, unit, price)
        handle_transaction(query, data)
    
    def edit_contract_info(self, cont_id, ref_id, categ, new_input):
        temp = "update CONTRACT set {} = ".format(categ) 
        query = temp + "%s where contract_id = %s and client_id = %s"
        data = (new_input, cont_id, ref_id)
        handle_transaction(query, data)

    def get_data(self, cont_id, ref_id, categ):
        temp = "select {} from CONTRACT ".format(categ)
        query = temp + "where contract_id = {} and client_id = {}".format(cont_id, ref_id)
        handle_select(query)
