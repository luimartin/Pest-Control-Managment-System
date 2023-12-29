from Database import *
from QuerySettings import *

class Client:
    def __init__(self):
        pass
    
    def add_client_info(self, name, email, phone_num, address):
        query = "insert into CLIENT values (%s, %s, %s, %s, %s, %s, %s)"
        data = (name, email, phone_num, address, 'New', 0)
        handle_transaction(query, data)

    def add_contract(self, ref_id, problem, service_type, start_date, end_date, square_meter, unit, price):
        query = "insert into CONTRACT values (%s, %s %s, %s, %s, %s, %s, %s, %s)"
        data = (problem, service_type, start_date, end_date, square_meter, unit, price)
        handle_transaction(query, data)

    def search(self):
        query = "select * from CLIENT"
        handle_select(query)
        
c = Client()
c.add_contract(1, "General Infestation", "Pest and Termite", "2022-12-31", "2023-01-02", 187.0, 7, 15000)
