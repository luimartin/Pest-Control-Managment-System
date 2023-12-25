class Contract:
    def __init__(self, prob, treatment, start_contract_period, end_contract_period, scope, num_unit, valuation):
        self.__prob = prob
        self.__treatment = treatment
        self.__start_contract_period = start_contract_period
        self.__end_contract_period = end_contract_period
        self.__scope = scope
        self.__num_unit = num_unit
        self.__valuation = valuation
    
    def edit_contract_detail(self, type, value):
        match type: 
            case "problem":
                self.__prob = value
            case "treatment":
                self.__treatment = value
            case "start contract period":
                self.__start_contract_period = value
            case "end contract period":
                self.__end_contract_period = value
            case "scope":
                self.__scope = value
            case "num unit":
                self.__num_unit = value
            case "valuation":
                self.__valuation = value 

    def __str__(self):
        return (self.__prob, self.__treatment, self.__start_contract_period, 
                self.__end_contract_period, self.__scope, self.__num_unit, self.__valuation)

    @property
    def prob(self):
        return self.__prob
    
    @property
    def treatment(self):
        return self.__treatment
    
    @property
    def start_contract_period(self):
        return self.__start_contract_period
    
    @property
    def end_contract_period(self):
        return self.__end_contract_period

    @property
    def scope(self):
        return self.__scope
    
    @property
    def num_unit(self):
        return self.__num_unit
    
    @property
    def valuation(self):
        return self.__valuation
    