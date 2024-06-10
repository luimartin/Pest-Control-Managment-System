from database import *
from query_settings import *

from inventory import Inventory

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
        isItemValid = self.Inventory.deduct_item(item_id, quantity)
        if isItemValid:
            query = (
                "insert into TECHNICIAN_ITEM (technician_id, item_id, quantity, date_acquired)"
                "values (%s, %s, %s, %s)"
            )
            data = (tech_id, item_id, quantity, date_acquired)
            handle_transaction(query, data)
        
        return None

    def show_accounted_item(self, tech_id):
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
                "set TECHNICIAN_ITEM.quantity = TECHNICIAN_ITEM.quantity - %s, "
                "INVENTORY.quantity = INVENTORY.quantity + %s "
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
    
    def isTechnicianExist(self, tech_id):
        query = "select void from TECHNICIAN where technician_id = {}".format(tech_id)
        output = handle_select(query)[0][0] # Retrieve either 1 or 0 (0 means the item exists in DB, not void)  

        if not output: return True
        return False 

    def isTechnicianAvailable(self, tech_id):
        query = (
            "select count(schedule_id) from SCHEDULE "
            "inner join TECHNICIAN on TECHNICIAN.technician_id = {}".format(tech_id)
        )
        output_amount = handle_select(query)[0][0]
        
        # The number of rows determines the number of accounted clients 
        # (Max. 2 only, otherwise not available)
        if output_amount >= 2: return False
        return True

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
    
    def search(self, input):
        query = f"""
            select * from TECHNICIAN 
            where (
            first_name LIKE '%{input}%'
            OR last_name LIKE '%{input}%'
            OR phone_num LIKE '%{input}%' 
            OR address LIKE '%{input}%' 
            ) and void = 0
        """
        return handle_select(query)

t = Technician()
#t.add_technician("Mora", "Jeremy", "09154847877", "Pasig City")
#print(t.search("Mor"))