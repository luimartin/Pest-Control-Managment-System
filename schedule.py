from datetime import datetime, date, timedelta

from database import *
from query_settings import *

from technician import Technician

class Schedule:
    def __init__(self):
        self.Technician = Technician()
     
    def view_sched(self):
        query = "select client.name, schedule_type, start_date, end_date, time_in, time_out, schedule.status from schedule inner join client on schedule.client_id = client.client_id where schedule.void = 0"
        return handle_select(query)
    def add_schedule(self, ref_id, sched_type, start_date, end_date, time_in = None, time_out = None):        
        query = (
            "insert into SCHEDULE (client_id, schedule_type, start_date, end_date, time_in, time_out, void, status)"
            "values (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (ref_id, sched_type, start_date, end_date, time_in, time_out, 0, "Idle")
        handle_transaction(query, data)    

        if sched_type == 'Posting':
            temp_query = "select last_insert_id()"
            sched_id = handle_select(temp_query)[0][0]

            self.posting_schedulizer(sched_id, start_date, end_date)

    def earliest_deadline_first(self):
        today = date.today()
        
        query1 = """ 
                select schedule_id, start_date, time_in, time_out from schedule 
                where start_date like '{}%'
                and schedule_type = 'Default'
                union
                select schedule_id, single_date, "09:00:00", "17:00:00" from schedulizer
                where single_date like '{}%'
                order by time_in, time_out ASC
            """.format(today, today)    

        query2 = (
            "update schedule set status = 'Progress' "
            "where schedule_id in {}"
        )

        return handle_select(query1)
    
    def update_state_when_done(self, client_id, sched_id):
        query = (
            "update schedule set status = 'Done' "
            "where client_id = %s and schedule_id = %s"
        )
        data = (client_id, sched_id)

    def posting_schedulizer(self, sched_id, start_date, end_date):
        ref_sched = start_date
        day_tester = None

        while(True):
            temp_query = "select dayname({})".format("\'"+ref_sched+"\'")
            day_tester = handle_select(temp_query)[0][0]

            if day_tester != 'Sunday':
                query = (
                    "insert into SCHEDULIZER (schedule_id, single_date)"
                    "values (%s, %s)"                
                )
                data = (sched_id, ref_sched)
                handle_transaction(query, data)

            if ref_sched == end_date: break
            ref_sched = self.modifyDate(ref_sched)        
       

    def modifyDate(self, ref_sched):
        date = datetime.strptime(ref_sched,  '%Y-%m-%d')
        modified_date = date + timedelta(days = 1)
        
        return datetime.strftime(modified_date, '%Y-%m-%d')
    

    def posting_modifier(self, ref_id, sched_id, new_start_date, new_end_date):
        prev_start_date = datetime.strftime(self.get_data(sched_id, ref_id, 'start_date'), '%Y-%m-%d') 
        prev_end_date = datetime.strftime(self.get_data(sched_id, ref_id, 'end_date'), '%Y-%m-%d')  

        self.edit_schedule_info(sched_id, ref_id, 'start_date', new_start_date)
        self.edit_schedule_info(sched_id, ref_id, 'end_date', new_end_date)   

        self.deleteRangedDates(prev_start_date, new_start_date, new_start_date)        

        if new_end_date < prev_end_date:
            self.deleteRangedDates(new_end_date, prev_end_date, new_end_date)
        
        if  new_end_date > prev_end_date:
            ref_start_date = self.modifyDate(prev_end_date)
            self.posting_schedulizer(sched_id, ref_start_date, new_end_date)


    def deleteRangedDates(self, date_1, date_2, date_boundary):
        query = (
            "delete from SCHEDULIZER "
            "where single_date between %s and %s "
            "and single_date not in (%s)"
        )
        data = (date_1, date_2, date_boundary)  
        handle_transaction(query, data)


    def assign_technician(self, sched_id, client_id, tech_id):
        isTechnicianExist = self.Technician.isTechnicianExist(tech_id)
        isTechnicianAvailable = self.Technician.isTechnicianAvailable(tech_id)
        print(isTechnicianExist)
        print(isTechnicianAvailable)

        if isTechnicianExist and isTechnicianAvailable:
            query = (
                "update SCHEDULE "
                "set technician_id = %s"
                "where schedule_id = %s and client_id = %s"
            )
            data = (tech_id, sched_id, client_id)
            handle_transaction(query, data)     

            query = (
                "update TECHNICIAN "
                "set state = 'Active' "
                "where technician_id = %s"
            )
            data = (tech_id)
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
        return handle_select(query)[0][0]
    

    def edit_schedule_info(self, sched_id, ref_id, categ, new_input):
        temp = "update SCHEDULE set {} = ".format(categ) 
        query = temp + "%s where schedule_id = %s and client_id = %s"
        data = (new_input, sched_id, ref_id)
        handle_transaction(query, data)


    def get_data(self, sched_id, ref_id, categ):
        temp = "select {} from SCHEDULE ".format(categ)
        query = temp + "where schedule_id = {} and client_id = {}".format(sched_id, ref_id)
        return handle_select(query)[0][0]
    

    def search(self, input):
        query = f"""
            select * from SCHEDULE 
            where (
            schedule_id LIKE '%{input}%'
            OR client_id LIKE '%{input}%'
            OR technician_id LIKE '%{input}%' 
            OR schedule_type LIKE '%{input}%' 
            OR start_date LIKE '%{input}%' 
            OR time_in LIKE '%{input}%'
            OR time_out LIKE '%{input}%'
            ) and void = 0
        """
        return handle_select(query) 

#s = Schedule()
#s.add_schedule(1, 'Default', '2024-06-11', '2024-06-11', '08:00:00', '13:00:00')
#s.assign_technician(12, 1, 1)
#s.posting_modifier(1, 28, "2024-02-24", "2024-02-27")
#print(s.search("Posting"))
#print(s.earliest_deadline_first())