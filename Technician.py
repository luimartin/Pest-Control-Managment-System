from Database import *
from QuerySettings import *

from Inventory import Inventory

class Technician:
    def __init__(self):
        self.Inventory = Inventory()
    
    def add_technician(self, f_name, l_name, phone_num, address):
        query = (
            "insert into TECHNICIAN (first_name, last_name, phone_num, address, void)"
            "values (%s, %s, %s, %s, %s)"
        )
        data = (f_name, l_name, phone_num, address, 0)
        handle_transaction(query, data)
    
    def assign_item(self, tech_id, item_id, quantity, date_acquired):
        is_item_valid = self.Inventory.deduct_item(item_id, quantity)
        if is_item_valid:
            query = (
                "insert into TECHNICIAN_ITEM (technician_id, item_id, quantity, date_acquired)"
                "values (%s, %s, %s, %s)"
            )
            data = (tech_id, item_id, quantity, date_acquired)
            handle_transaction(query, data)
        
        return None

    def accounted_item(self, tech_id):
        query = (
            "select TECHNICIAN.technician_id, TECHNICIAN.first_name, TECHNICIAN.last_name, "
            "INVENTORY.item_name, INVENTORY.item_type, TECHNICIAN_ITEM.quantity, date_acquired "
            "from TECHNICIAN_ITEM "
            "inner join INVENTORY "
            "on INVENTORY.item_id = TECHNICIAN_ITEM.item_id "
            "inner join TECHNICIAN "
            "on TECHNICIAN.technician_id = {}".format(tech_id)
        )
        return handle_select(query)

    def return_item(self, tech_id, inv_id, return_amount):
        if self.isAssignedItemAvailable(tech_id, inv_id, return_amount):
            query = (
                "update TECHNICIAN_ITEM, INVENTORY "
                "set TECHNICIAN_ITEM.quantity = TECHNICIAN_ITEM.quantity - %s"
                ", INVENTORY.quantity = INVENTORY.quantity + %s "
                "where TECHNICIAN_ITEM.item_id = %s and TECHNICIAN_ITEM.item_id = %s"
            )
            data = (return_amount, return_amount, inv_id, tech_id)
            handle_transaction(query, data)

    def isAssignedItemAvailable(self, tech_id, inv_id, return_amount):
        query = (
            "select quantity from TECHNICIAN_ITEM "
            "where technician_id = {} and item_id = {}".format(tech_id, inv_id)
        )
        output = handle_select(query)[0][0]

        if output >= return_amount: return True
        return False
    
    def isTechnicianAvailable(self, tech_id):
        pass

    def edit_technician_info(self, tech_id, categ, new_input):
        temp = "update TECHNICIAN set {} = ".format(categ) 
        query = temp + "%s where technician_id = %s"
        data = (new_input, tech_id)
        handle_transaction(query, data)

    def get_data(self, tech_id, categ):
        temp = "select {} from TECHNICIAN ".format(categ)
        query = temp + "where technician_id = {}".format(tech_id)
        return handle_select(query)
        
    def search(self, input):
        query = "select * from TECHNICIAN where first_name = {}".format("\'"+input+"\'")
        return handle_select(query)   

t = Technician()
