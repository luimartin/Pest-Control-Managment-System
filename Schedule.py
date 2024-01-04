from Database import *
from QuerySettings import *

from ClientInfo import ClientInfo
from Technician import Technician

class Schedule:
    def __init__(self):
        self.ClientInfo = ClientInfo()
        self.Techincian = Technician()
        
    def add_schedule(self, ref_id, sched_type, start_date, end_date, time_in, time_out):
        query = (
            "insert into SCHEDULE (client_id, schedule_type, start_date, end_date, time_in, time_out)"
            "values (%s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, sched_type, start_date, end_date, time_in, time_out)
        handle_transaction(query, data)

    def assign_technician(self, sched_id, client_id, tech_id):
        query = (
            "update SCHEDULE"
            "set technician_id = %s"
            "where schedule_id = %s and client_id = %s"
        )
        data = (tech_id, sched_id, client_id)
        handle_transaction(query, data)      

    def edit_schedule_info(self, sched_id, ref_id, categ, new_input):
        temp = "update SCHEDULE set {} = ".format(categ) 
        query = temp + "%s where schedule_id = %s and client_id = %s"
        data = (new_input, sched_id, ref_id)
        handle_transaction(query, data)

    def get_data(self, sched_id, ref_id, categ):
        temp = "select {} from SCHEDULE ".format(categ)
        query = temp + "where schedule_id = {} and client_id = {}".format(sched_id, ref_id)
        handle_select(query)
