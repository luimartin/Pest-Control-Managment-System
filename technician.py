from database import *
from query_settings import *

from datetime import date
from inventory import Inventory


class Technician:
    def __init__(self):
        self.Inventory = Inventory()
        self.today = date.today()

    def add_technician(self, f_name, l_name, phone_num, address):
        query = (
            "insert into TECHNICIAN (first_name, last_name, phone_num, address, void, state)"
            "values (%s, %s, %s, %s, %s, %s)"
        )
        data = (f_name, l_name, phone_num, address, 0, "Idle")
        handle_transaction(query, data)

    def assign_item(self, tech_id, item_id, quantity):
        date_acquired = date.today()

        isItemValid = self.Inventory.deduct_item(item_id, quantity)
        if isItemValid:
            query = (
                "insert into TECHNICIAN_ITEM (technician_id, item_id, quantity, date_acquired)"
                "values (%s, %s, %s, %s)"
            )
            data = (tech_id, item_id, quantity, date_acquired)
            handle_transaction(query, data)
            return "Item Assign"
        return "Invalid"
    
    def show_assigned_client(self):
        query = """
            select concat(TECHNICIAN.first_name, ' ',TECHNICIAN.last_name), CLIENT.name, SCHEDULE.start_date, SCHEDULE.end_date, SCHEDULE.time_in, SCHEDULE.time_out, 
            SCHEDULE.schedule_id, CLIENT.client_id from SCHEDULE 
            inner join CLIENT on CLIENT.client_id = SCHEDULE.client_id 
            inner join TECHNICIAN on TECHNICIAN.technician_id = SCHEDULE.technician_id;

        """
        return handle_select(query)

    def show_accounted_item(self, tech_id):
        query = """
        select technician_item_id, concat(TECHNICIAN.first_name, ' ',TECHNICIAN.last_name), 
        INVENTORY.item_name, INVENTORY.item_type, TECHNICIAN_ITEM.quantity, date_acquired 
        , inventory.item_id, TECHNICIAN.technician_id from TECHNICIAN_ITEM 
        inner join INVENTORY 
        on INVENTORY.item_id = TECHNICIAN_ITEM.item_id 
        inner join TECHNICIAN 
        on TECHNICIAN.technician_id = TECHNICIAN_ITEM.technician_id
        where TECHNICIAN_ITEM.technician_id = {};
        """.format(tech_id)
        
        return handle_select(query)

    def return_item(self, tech_item_id, inv_id, return_amount):
        if self.isAssignedItemAvailable(tech_item_id, return_amount):
            query = (
                "update TECHNICIAN_ITEM, INVENTORY "
                "set TECHNICIAN_ITEM.quantity = TECHNICIAN_ITEM.quantity - %s, "
                "INVENTORY.quantity = INVENTORY.quantity + %s "
                "where TECHNICIAN_ITEM.item_id = %s and INVENTORY.item_id = %s and TECHNICIAN_ITEM.technician_item_id = %s"
            )                                                                   
            data = (return_amount, return_amount, inv_id, inv_id, tech_item_id)
            handle_transaction(query, data)

    def isAssignedItemAvailable(self, tech_item_id, return_amount):
        query = (
            "select quantity from TECHNICIAN_ITEM "
            "where technician_item_id = {} ".format(tech_item_id)
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
            "where technician_id = {}".format(tech_id)
        )
        output_amount = handle_select(query)[0][0]
        print(output_amount)
        
        # The number of rows determines the number of accounted clients 
        # (Max. 2 only, otherwise not available)
        if output_amount >= 2: return False
        return True

    def isTechnicianOnPosting(self, tech_id, sched_id):
        query = (
            "select schedule_type from SCHEDULE "
            "where technician_id = {} and schedule_id = {}".format(tech_id, sched_id)
        )
        output = handle_select(query)[0][0]
        
        if output == 'Posting': return True
        return False

    def edit_technician_info(self, tech_id, categ, new_input):
        temp = "update TECHNICIAN set {} = ".format(categ) 
        query = temp + "%s where technician_id = %s "
        data = (new_input, tech_id)

        self.void_assigned_from_sched(tech_id)
        self.void_tech_item(tech_id)

        handle_transaction(query, data)

    def void_assigned_from_sched(self, tech_id):
        query = """
            select schedule_id from SCHEDULE
            where technician_id = {}
        """.format(tech_id)
        t_assigned_id = handle_select(query)
        print(t_assigned_id)
        
        if t_assigned_id:
            for sched in t_assigned_id:
                query_void = """
                    update SCHEDULE set technician_id = Null 
                    where schedule_id = %s 
                """
                data = (sched[0], )
                handle_transaction(query_void, data)
    
    def void_tech_item(self, tech_id):
        query = """
            select technician_item_id, item_id, quantity from TECHNICIAN_ITEM
            where technician_id = {}
        """.format(tech_id)
        t_item_id = handle_select(query)
        print(t_item_id)

        if t_item_id:
            for item in t_item_id:
                self.return_item(item[0], item[1], item[2])
        
    
    def get_data(self, tech_id, categ):
        temp = "select {} from TECHNICIAN ".format(categ)
        query = temp + "where technician_id = {}".format(tech_id)
        return handle_select(query)
        
    def search(self, input):
        query = "select * from TECHNICIAN where first_name = {}".format("\'"+input+"\'")
        return handle_select(query)   
    
    def search(self, input):
        query = f"""
            select technician_id,concat(TECHNICIAN.first_name, " ", 
            TECHNICIAN.last_name)
        , phone_num, address ,state, null, null, null
            from TECHNICIAN 
            where (
            first_name LIKE '%{input}%'
            OR last_name LIKE '%{input}%'
            OR phone_num LIKE '%{input}%' 
            OR address LIKE '%{input}%' 
            ) and void = 0
        """
        return handle_select(query)
    
    def select_all_tech(self):
        query = """
        select technician_id,concat(TECHNICIAN.first_name, " ", TECHNICIAN.last_name)
        , phone_num, address ,state, null, null, null from technician where void = 0;
        """
        return(handle_select(query))
    
    def select_all_tech_void(self):
        query = """
        select technician_id,concat(TECHNICIAN.first_name, " ", TECHNICIAN.last_name)
        , phone_num, address, null ,state, null, null from technician where void = 1;
        """
        return(handle_select(query))

    def select_specific_tech(self, techid):
        query = """
        select first_name, last_name, phone_num, address from technician
        where void = 0 and technician_id = {};
        """.format(techid)
        return handle_select(query)
    

t = Technician()
#t.void_assigned_from_sched(21)
#t.void_tech_item(21)
#print(t.show_assigned_client())
#print(t.show_accounted_item(10))
#print(t.select_specific_tech(10))
#t.add_technician("Robert", "Santos", "09452842467", "Balong Bato, San Juan City")
#t.add_technician("John", "Timado", "09760040362", "West Crame San Juan City")
#t.add_technician("Lawrence", "Buena", "09452842467", "Pacita, Laguna")
#t.add_technician("Ijah", "Buena", "09760040362", "Pacita Laguna")
#t.add_technician("Johnny", "Mora", "09452842467", "Pasig City")
#t.assign_item(3, "last_name", "Cruz")
#print(t.get_data(10, 'concat(TECHNICIAN.first_name, " ", TECHNICIAN.last_name)'))
