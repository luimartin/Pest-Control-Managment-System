from Database import *
from QuerySettings import *

class Inventory:
    def __init__(self):
        pass

    def add_item(self, name, item_type, quant, expir, desc):
        query = (
            "insert into INVENTORY (item_name, item_type, quantity, expiration, description, void)"
            "values (%s, %s, %s, %s, %s, %s)"
        )
        data = (name, item_type, quant, expir, desc, 0)
        handle_transaction(query, data)

    def deduct_item(self, inv_id, amount):
        output = None 
        if self.isItemExist(inv_id):
            query = "update INVENTORY set quantity = quantity - %s WHERE item_id = %s"
            data = (amount, inv_id)
            handle_transaction(query, data)
            output = True

        return output
    
    def stock_item(self, inv_id, amount):
        if self.isItemExist(inv_id):
            query = "update INVENTORY set quantity = quantity + %s WHERE item_id = %s"
            data = (amount, inv_id)
            handle_transaction(query, data)
        
        return None

    def edit_inv_info(self, inv_id, categ, new_input):
        temp = "update INVENTORY set {} = ".format(categ) 
        query = temp + "%s where item_id = %s"
        data = (new_input, inv_id)
        handle_transaction(query, data)

    def choose_category(self, item_type):
        query = "select item_name, quantity, date_format(expiration, '%m/%d/%y'), \
        description from INVENTORY where item_type = {}".format("\'"+item_type+"\'")
        return handle_select(query)

    def isItemExist(self, inv_id):
        query = "select void from INVENTORY where item_id =  {}".format(inv_id)
        output = handle_select(query)[0][0] # Retriev from List and Tuple

        if not output: return True
        return False 
