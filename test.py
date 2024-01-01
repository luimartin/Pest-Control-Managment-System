from Database import *
from QuerySettings import *

class Technician:
    def __init__(self):
        pass
    
    def add_technician(self, f_name, l_name, phone_num, address):
        query = (
            "insert into TECHNICIAN (first_name, last_name, phone_num, address, void)"
            "values (%s, %s, %s, %s, %s)"
        )
        data = (f_name, l_name, phone_num, address, 0)
        handle_transaction(query, data)

    def edit_technician_info(self, tech_id, categ, new_input):
        temp = "update TECHNICIAN set {} = ".format(categ) 
        query = temp + "%s where technician_id = %s"
        data = (new_input, tech_id)
        handle_transaction(query, data)
