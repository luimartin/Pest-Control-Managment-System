from ClientInfo import ClientInfo
from AssignItem import AssignItem

class Technician:
    def __init__(self, l_name, f_name, contact_num, loc):
        self.id = None
        
        self.__l_name = l_name
        self.__f_name = f_name
        self.__contact_num = contact_num
        self.__loc = loc
        
        self.technician = []
        self.technician.append(self)

        self.item = []
        self.client = []
        
        self.status = False
        self.count = 0

    def assign_item(self, item_name, item_type, item_quant, start_assign, Inventory):
        if Inventory.get_item(item_name, item_quant):
            self.item.append(AssignItem(item_name, item_type, item_quant, start_assign))

    def assign_client(self, ClienInfo):
        self.client.append(ClienInfo)
    
    def is_sched_available(self):
        # https://www.geeksforgeeks.org/creating-a-list-of-range-of-dates-in-python/
        # https://www.programiz.com/python-programming/datetime
        pass

    def handled_client(self):
        return self.client[0].__l_name, self.client[0].schedule.__str__()

    def accounted_item(self):
        return self.technician[0].__l_name, self.technician[0].item[0].__str__()
    
    def __str__(self):
        return self.__l_name, self.__f_name, self.__contact_num, self.__loc

    @property
    def l_name(self):
        return self.__l_name
    
    @property
    def f_name(self):
        return self.__f_name
    
    @property
    def contact_num(self):
        return self.__contact_num
    
    @property
    def loc(self):
        return self.__loc