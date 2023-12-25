class Schedule:
    def __init__(self, sched_type, start_date, end_date, time_in=9, time_out=17):
        self.__sched_type = sched_type
        self.__start_date = start_date       
        self.__end_date = end_date
        self.__time_in = time_in
        self.__time_out = time_out
        
    def __str__(self):
        return self.__sched_type, self.__start_date, self.__end_date, self.__time_in, self.__time_out

    @property
    def sched_type(self):
        return self.__sched_type
    
    @property
    def start_date(self):
        return self.__start_date
    
    @property
    def end_date(self):
        return self.__end_date
    
    @property
    def time_in(self):
        return self.__time_in
    
    @property
    def time_out(self):
        return self.__time_out    
