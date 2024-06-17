from database import *
from query_settings import *

class Inventory:
    def __init__(self):
        pass
    
    def select_specific_item(self, inv_id):
        query = "select item_name, quantity, expiration, description, item_type, supplier from Inventory where void = 0 and item_id = {}".format(inv_id)
        return handle_select(query)
    
    def select_inventory(self):
        query = "select item_id,item_name, item_type, quantity, expiration, description, supplier, last_delivery_date from Inventory where void = 0"
        return handle_select(query)
    
    def select_inventory_void(self):
        query = "select item_id,item_name, item_type, quantity, expiration, description from Inventory where void = 1"
        return handle_select(query)

    def select_all_delivery(self):
        query = """
        select delivery_id,
        i.item_name,
        d.quantity,
        d.delivery_date,
        d.expiration,
        d.supplier from delivery 
        as d inner join inventory as i 
        on d.item_id = i.item_id;
        """
        return handle_select(query)

    def for_delivery(self, name, item_type, supplier, deliverydate):
        select = """
        SELECT item_id 
        FROM inventory 
        WHERE item_name = '{}' 
        AND item_type = '{}' 
        AND supplier = '{}' 
        AND last_delivery_date = '{}' 
        AND void = 0;
        """.format(name, item_type, supplier, deliverydate)
        return handle_select(select)

    def add_item(self, name, item_type, quant, desc, expir, supplier, deliverydate):
        query = (
            "insert into INVENTORY (item_name, item_type, quantity, expiration, description, void, supplier, last_delivery_date)"
            "values (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (name, item_type, quant, expir, desc, 0, supplier, deliverydate)
        handle_transaction(query, data)

        id =self.for_delivery(name, item_type, supplier, deliverydate)
        query1 = (
            "insert into delivery (item_id, quantity, expiration, supplier, delivery_date)"
            "values (%s, %s, %s, %s, %s)"
        )
        data1 = (id[0][0], quant, expir, supplier, deliverydate)
        handle_transaction(query1, data1)


    def deduct_item(self, inv_id, amount):
        output = None
        if self.isItemExist(inv_id) and self.isItemAvailable(inv_id, amount):
            query = "update INVENTORY set quantity = quantity - %s WHERE item_id = %s"
            data = (amount, inv_id)
            handle_transaction(query, data)
            output = True

        return output
    
    def stock_item(self, inv_id, quantity, expiration, supplier, deliverydate):
        query = """
        update INVENTORY 
        set quantity = quantity + %s, expiration =  %s,
        supplier = %s, last_delivery_date = %s
        WHERE item_id = %s
        """
        data = (quantity, expiration, supplier, deliverydate , inv_id)
        handle_transaction(query, data)
        
        query1 = """
        INSERT INTO delivery (item_id, 
        quantity, delivery_date, expiration, supplier)
        VALUES(%s,%s,%s,%s,%s)
        """
        data1 = (inv_id, quantity, deliverydate, expiration, supplier)
        handle_transaction(query1, data1)
    
    def isItemExist(self, inv_id):
        query = "select void from INVENTORY where item_id =  {}".format(inv_id)
        output = handle_select(query)[0][0] # Retrieve either 1 or 0 (0 means the item exists in DB, not void)  

        if not output: return True
        return False 
    
    def isItemAvailable(self, inv_id, amount):
        query = "select void from INVENTORY where item_id = {} and quantity >= {}".format(inv_id, amount)
        output = handle_select(query)[0][0] # Retrieve either 1 or 0 (0 means the item exists in DB, not void)
        
        if not output: return True
        return False

    def edit_inv_info(self, inv_id, categ, new_input):
        temp = "update INVENTORY set {} = ".format(categ) 
        query = temp + "%s where item_id = %s"
        data = (new_input, inv_id)
        handle_transaction(query, data)

    def choose_category(self, item_type):
        """query = "select item_name, quantity, date_format(expiration, '%m/%d/%y'), \
        description from INVENTORY where item_type = {}".format("\'"+item_type+"\'")"""
        query = "select item_id,item_name, item_type, quantity, expiration, description from INVENTORY where void = 0 and item_type = {}".format("\'"+item_type+"\'")
        return handle_select(query)
    
    def search(self, input):
        query = f"""
            select * from INVENTORY 
            where (
            item_id LIKE '%{input}%'
            OR item_name LIKE '%{input}%'
            OR item_type LIKE '%{input}%' 
            OR quantity LIKE '%{input}%' 
            OR expiration LIKE '%{input}%' 
            OR description LIKE '%{input}%'
            ) and void = 0
        """
        return handle_select(query) 
  
#i = Inventory()
#print(i.for_delivery("Duster", "Material", "Aling Nena", '2024-06-16 18:52:03')[0][0])
#i.add_item("Mouse Trap", "Material", 10, "Trap the mouse")
#i.edit_inv_info(3, "Expiration", "2025-01-01")
#print(i.choose_category("Chemical"))
