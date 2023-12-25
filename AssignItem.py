class AssignItem:
    def __init__(self, item_name, item_type, item_quant, start_assign):
        self.__item_name = item_name
        self.__item_type = item_type
        self.__item_quant = item_quant
        self.__start_assign  = start_assign
        
    def __str__(self):
        return self.__item_name, self.__item_type, self.__item_quant, self.__start_assign
    
    @property
    def item_name(self):
        return self.__item_name
    
    @property
    def item_type(self):
        return self.__item_type
    
    @property
    def item_quant(self):
        return self.__item_quant
    
    @property
    def start_assign(self):
        return self.__start_assign
    