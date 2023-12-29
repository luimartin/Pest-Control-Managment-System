from Database import *
from QuerySettings import *

class ClientInfo:
    def __init__(self):
        pass
    
    def add_client_info(self, name, email, phone_num, address):
        query = (
            "insert into CLIENT(name, email, phone_num, address, status, void)"
            "values (%s, %s, %s, %s, %s, %s,)"
        )
        data = (name, email, phone_num, address, 'New', 0)
        handle_transaction(query, data)

    def add_contract(self, ref_id, problem, service_type, start_date, end_date, square_meter, unit, price):
        query = (
            "insert into CONTRACT (client_id, problem, service_type, start_date, end_date, square_meter, unit, price)"
            "values (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, problem, service_type, start_date, end_date, square_meter, unit, price)
        handle_transaction(query, data)

    def add_schedule(self, ref_id, sched_type, start_date, end_date, time_in, time_out):
        query = (
            "insert into SCHEDULE (client_id, schedule_type, start_date, end_date, time_in, time_out)"
            "values (%s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, sched_type, start_date, end_date, time_in, time_out)
        handle_transaction(query, data)

    def edit_personal_info(self, ref_id, categ, new_input):
        temp = "update CLIENT set {} = ".format(categ) 
        query = temp + "%s where client_id = %s"
        data = (new_input, ref_id)
        handle_transaction(query, data)

    # Partial Only
    def search(self, input):
        query = "select * from CLIENT where name = {}".format("\'"+input+"\'")
        handle_select(query)   

c = ClientInfo()
c.edit_personal_info(1, "address", "West Crame")
