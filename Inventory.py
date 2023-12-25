class Inventory:
    def __init__(self, name, item_type, quant, exp_date, desc):
        self.id = None
        
        self.__name = name
        self.__item_type = item_type
        self.__quant = quant
        self.__exp_date = exp_date
        self.__desc = desc

        self.inventory = []
        self.inventory.append(self)

        self.isVoid = False
        self.curr_index = 0

    def get_item(self, name, amount):   
        if self.item_exist(name): 
            if self.inventory[self.curr_index].__quant >= amount:
                self.inventory[self.curr_index].__quant -= amount
                print(f'Item obtained: {name} with amount of {amount}')
                return True
        
        print(f'Item failed to obtain')
        return False
 
    def restock_item(self, name, amount):
        if self.item_exist(name):
            self.__quant += amount
            print(f'Item added: to {name} with amount of {amount}')
            return True

        print(f'Item failed to add')
        return False

    def item_exist(self, name):
        for i in range(len(self.inventory)):
            if name == self.inventory[i].name:
                self.curr_index = i
                return True
        
        return False

    def edit_item_info(self, type, value):
        match type:
            case "name":
                self.__name = value
            case "item type":
                self.__item_type = value
            case "quant":
                self.__quant = value
            case "exp_date":
                self.__exp_date = value
            case "description":
                self.__desc = value

    def __str__(self):
        return self.__name, self.__item_type, self.__quant, self.__exp_date, self.__desc

    @property
    def name(self):
        return self.__name
    
    @property
    def item_type(self):
        return self.__item_type
    
    @property
    def quant(self):
        return self.__quant

    @property
    def exp_date(self):
        return self.__exp_date

    @property
    def desc(self):
        return self.__desc    
        
        
    