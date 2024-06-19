from database import *
from query_settings import *


class Contract:
    def __init__(self):
        pass

    def has_a_contract(self, clientid):
        query = "select contract_id from contract where client_id= {} and void = 0".format(clientid)
        output = handle_select(query)

        if output: return True
        return False 
    
    def contract_view(self, client_id):
        query =" select problem, service_type, start_date, end_date, square_meter, unit, price from contract where client_id = {} and void = 0".format(client_id)
        return handle_select(query)
    
    
    def add_contract(self, ref_id, problem, service_type, start_date, end_date, square_meter, unit, price):
        query = (
            "insert into CONTRACT (client_id, problem, service_type, start_date, end_date, square_meter, unit, price, void)"
            "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, problem, service_type, start_date, end_date, square_meter, unit, price, 0)
        handle_transaction(query, data)
    
    def edit_contract_info(self, cont_id, ref_id, categ, new_input):
        temp = "update CONTRACT set {} = ".format(categ) 
        query = temp + "%s where contract_id = %s and client_id = %s"
        data = (new_input, cont_id, ref_id)
        handle_transaction(query, data)

    def get_data(self, ref_id, categ):
        temp = "select {} from CONTRACT ".format(categ)
        query = temp + "where client_id = {}".format(ref_id)
        return handle_select(query)

    def search(self, input):
        query = f"""
            select * from CONTRACT 
            where (
            contract_id LIKE '%{input}%'
            OR client_id LIKE '%{input}%'
            OR problem LIKE '%{input}%' 
            OR service_type LIKE '%{input}%' 
            OR start_date LIKE '%{input}%' 
            OR end_date LIKE '%{input}%'
            OR square_meter LIKE '%{input}%'
            OR unit LIKE '%{input}%'
            OR price LIKE '%{input}%'
            ) 
        """
        return handle_select(query)    

#c = Contract()
#c.add_contract(1, "Roaches", "Misting Method", "2023-01-01", "2024-01-01", 100.00, 3, 100000)
#print(c.search(""))
#print(c.has_a_contract(1))