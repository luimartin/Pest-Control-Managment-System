from Contract import Contract
from Schedule import Schedule

class ClientInfo:
    def __init__(self, name, contact_num, loc, email):
        self.id = None
        
        self.__name = name
        self.__contact_num = contact_num
        self.__loc = loc
        self.__email = email
        
        self.client = []
        self.client.append(self)
        
        self.schedule = None
        self.contract_detail = None
        self.assign_tech = []

        self.status = None
        self.isVoid = False 
    
    def add_contract_detail(self, prob, treatment, start_contract_period, end_contract_period, scope, num_unit, valuation):
        self.contract_detail = Contract(prob, treatment, start_contract_period, end_contract_period, scope, num_unit, valuation)

    def add_schedule(self, sched_type, start_date, end_date, time_in, time_out):
        self.schedule = Schedule(sched_type, start_date, end_date, time_in, time_out)
    
    def edit_personal_info(self, type, value):
        match type: 
            case "name":
                self.__name = value
            case "contact number":
                self.__contact_num = value
            case "location":
                self.__loc = value
            case "time out":
                self.__email = value

    def __str__(self):
        return self.__name, self.__contact_num, self.__loc, self.__email

    @property
    def name(self):
        return self.__name
    
    @property
    def contact_num(self):
        return self.__contact_num
    
    @property
    def loc(self):
        return self.__loc
    
    @property
    def email(self):
        return self.__email
    