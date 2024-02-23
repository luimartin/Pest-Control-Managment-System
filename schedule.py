from datetime import datetime, date, timedelta

from database import *
from query_settings import *

from technician import Technician

class Schedule:
    def __init__(self):
        self.Technician = Technician()
        
    def add_schedule(self, ref_id, sched_type, start_date, end_date, time_in = None, time_out = None):        
        query = (
            "insert into SCHEDULE (client_id, schedule_type, start_date, end_date, time_in, time_out)"
            "values (%s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, sched_type, start_date, end_date, time_in, time_out)
        handle_transaction(query, data)    

        if sched_type == 'Posting':
            temp_query = "select last_insert_id()"
            sched_id = handle_select(temp_query)[0][0]

            self.posting_schedulizer(sched_id, start_date, end_date)

    def posting_schedulizer(self, sched_id, start_date, end_date):
        ref_sched = start_date

        while(True):
            if ref_sched is not None:
                

                query = (
                    "insert into SCHEDULIZER (schedule_id, single_date)"
                    "values (%s, %s)"                
                )
                data = (sched_id, ref_sched)
                handle_transaction(query, data)
                
            if ref_sched == end_date: break
            ref_sched = self.modifyDate(ref_sched)        
       
    def modifyDate(self, ref_sched):
        output = None

        temp_query = "select dayname({})".format(ref_sched)
        day_tester = handle_select(temp_query)[0][0]

        if day_tester != 'Sunday':
            date = datetime.strptime(ref_sched,  '%Y-%m-%d')
            modified_date = date + timedelta(days = 1)
            output = datetime.strftime(modified_date, '%Y-%m-%d')
        
        return output
    
    def posting_modifier(self):
        pass

    def assign_technician(self, sched_id, client_id, tech_id):
        isTechnicianExist = self.Technician.isTechnicianExist(tech_id)
        isTechnicianAvailable = self.Technician.isTechnicianAvailable(tech_id)
        
        if isTechnicianExist and isTechnicianAvailable:
            query = (
                "update SCHEDULE "
                "set technician_id = %s "
                "where schedule_id = %s and client_id = %s"
            )
            data = (tech_id, sched_id, client_id)
            handle_transaction(query, data)      

    def show_accounted_technician(self, sched_id, client_id, tech_id):
        query = """
                select SCHEDULE.schedule_id, SCHEDULE.client_id, CLIENT.name, 
                concat("[", TECHNICIAN.technician_id, "]", " ", TECHNICIAN.first_name, " ", TECHNICIAN.last_name) as 'Accounted Technician' 
                from SCHEDULE 
                inner join CLIENT on CLIENT.client_id = {} 
                inner join TECHNICIAN on TECHNICIAN.technician_id = {} 
                where SCHEDULE.schedule_id = {}
            """.format(client_id, tech_id, sched_id)
        return handle_select(query)

    def edit_schedule_info(self, sched_id, ref_id, categ, new_input):
        temp = "update SCHEDULE set {} = ".format(categ) 
        query = temp + "%s where schedule_id = %s and client_id = %s"
        data = (new_input, sched_id, ref_id)
        handle_transaction(query, data)

    def get_data(self, sched_id, ref_id, categ):
        temp = "select {} fzom SCHEDULE ".format(categ)
        query = temp + "where schedule_id = {} and client_id = {}".format(sched_id, ref_id)
        handle_select(query)

s = Schedule()
s.add_schedule(1, 'Posting', '2023-01-01', '2023-01-05', '08:00:00', '10:00:00')
