from datetime import datetime, date, timedelta

from database import *
from query_settings import *
from datetime import date
from technician import Technician

import random

class Schedule:
    def __init__(self):
        self.Technician = Technician()
        self.today = date.today()

    def show_tech(self):
        query = """
        select  technician_id ,concat(TECHNICIAN.first_name,
        " ", TECHNICIAN.last_name) from TECHNICIAN
	    where void = 0
        """ 
        return handle_select(query)
    
    def view_sched(self):
        query = """
 select schedule_id ,c.name, schedule_type, start_date, end_date, time_in, 
	time_out, s.status, concat("[", TECHNICIAN.technician_id, "]", " ", 
    TECHNICIAN.first_name, " ", TECHNICIAN.last_name) from schedule as s
    inner join client as c on s.client_id = c.client_id
       left join TECHNICIAN on TECHNICIAN.technician_id = s.technician_id
                where s.void = 0 order by
            case when s.status = 'Progress' then 1 else 2 end,
            case when s.status = 'Done' then 3 end,
            start_date, time_in, time_out; 
        """
        return handle_select(query)
    
    def specific_view_sched(self,id):
        query = """
    select schedule_id ,client.name, schedule_type, start_date, end_date, time_in, 
	time_out, schedule.status, concat("[", TECHNICIAN.technician_id, "]", " ", 
    TECHNICIAN.first_name, " ", TECHNICIAN.last_name) from schedule 
    inner join client on schedule.client_id = client.client_id
       left join TECHNICIAN on TECHNICIAN.technician_id = Schedule.technician_id
        where SCHEDULE.void = 0 and schedule.client_id ={};
        """.format(id)
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
        query1 = """ 
                select schedule_id, start_date, time_in, time_out from SCHEDULE 
                where start_date like '{}%'
                union
                select schedule_id, single_date, "09:00:00", "17:00:00" from SCHEDULIZER
                where single_date like '{}%'
                order by start_date, time_in, time_out ASC
            """.format(self.today, self.today)    
        
        for id in handle_select(query1):
            query = "update SCHEDULE set status = 'Progress' where schedule_id = %s"
            query1 = (
                "update TECHNICIAN set state = 'Active' "
                "where technician_id = (select technician_id from SCHEDULE where schedule_id = %s)"
            )
            data = (id[0],)
            handle_transaction(query, data)
            handle_transaction(query1, data)  
        
    def earliest_deadline_first_show(self):
        query = """
        select *
        from SCHEDULE
        order by
            case when status = 'Progress' then 1 else 2 end,
            case when status = 'Done' then 3 end,
            start_date, time_in, time_out;
        """
        return handle_select(query)

    
    def update_state_when_done(self, sched_id, client_id):
        query = (
            "update TECHNICIAN, SCHEDULE "
            "set SCHEDULE.status = 'Done', TECHNICIAN.state = 'Idle', SCHEDULE.technician_id = NULL "
            "where SCHEDULE.technician_id = TECHNICIAN.technician_id "
            "and SCHEDULE.client_id = %s and SCHEDULE.schedule_id = %s and "
            "TECHNICIAN.technician_id = (select technician_id from SCHEDULE where client_id = %s and schedule_id = %s)"
        )
        data = (client_id, sched_id, client_id, sched_id) 
        handle_transaction(query, data)
        

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


    def assign_technician(self, sched_id, tech_id):
        # Check if the technician exists and is available
        isTechnicianExist = self.Technician.isTechnicianExist(tech_id)
        isTechnicianAvailable = self.Technician.isTechnicianAvailable(tech_id)

        if isTechnicianExist and isTechnicianAvailable:
            # Get the time_in, time_out, and start_date for the new schedule
            query_schedule_time = """
                SELECT time_in, time_out, start_date, technician_id
                FROM SCHEDULE
                WHERE schedule_id = {}
            """.format(sched_id)
            schedule_time = handle_select(query_schedule_time)

            if not schedule_time:
                return "Schedule not found."

            new_time_in, new_time_out, new_start_date, assigned_tech_id = schedule_time[0]
            print(new_time_in, new_time_out, new_start_date)

            # Check if the technician is already assigned to this schedule
            if assigned_tech_id == tech_id:
                return "Technician is already assigned to this schedule. [Already Assigned]"

            # Check for scheduling conflicts on the same date
            query_conflicts = """
                SELECT time_in, time_out 
                FROM SCHEDULE 
                WHERE technician_id = {} 
                AND start_date = '{}' 
                AND ((time_in < '{}' AND time_out > '{}') OR (time_in < '{}' AND time_out > '{}') OR (time_in >= '{}' AND time_out <= '{}'))
            """.format(tech_id, new_start_date, new_time_out, new_time_in, new_time_in, new_time_out, new_time_in, new_time_out)
            existing_schedules = handle_select(query_conflicts)
            print(existing_schedules)

            if existing_schedules:
                return "Technician has a scheduling conflict on the same day."

            # If no conflicts, proceed with assignment
            query = """               
                UPDATE SCHEDULE 
                SET technician_id = %s
                WHERE schedule_id = %s
            """
            data = (tech_id, sched_id)
            handle_transaction(query, data)     

            query1 = """
                UPDATE TECHNICIAN 
                SET state = 'Assigned' 
                WHERE technician_id = %s
            """
            data = (tech_id,)
            handle_transaction(query1, data)

            return "Technician assigned successfully."
        else:
            return "Technician not available or does not exist."



    def show_accounted_technician(self):
        query = """
                select  concat("[", TECHNICIAN.technician_id, "]", " ", TECHNICIAN.first_name, " ", TECHNICIAN.last_name) as 'Accounted Technician' 
                from SCHEDULE 
                left join TECHNICIAN on TECHNICIAN.technician_id = Schedule.technician_id
                where SCHEDULE.void = 0
            """
        return handle_select(query)
    

    def timetable(self, schedule_event=None):
        query = """
            select SCHEDULE.start_date, CLIENT.name, SCHEDULE.time_in, SCHEDULE.time_out
            from SCHEDULE 
            inner join CLIENT on SCHEDULE.client_id = CLIENT.client_id 
            where SCHEDULE.start_date <= LAST_DAY("{}") and SCHEDULE.start_date > LAST_DAY(DATE_SUB("{}", INTERVAL 1 MONTH)) 
            union 
            select SCHEDULIZER.single_date, CLIENT.name, "09:00:00", "17:00:00" 
            from SCHEDULIZER 
            inner join SCHEDULE on SCHEDULIZER.schedule_id = SCHEDULE.schedule_id
            inner join CLIENT on SCHEDULE.client_id = CLIENT.client_id 
            where SCHEDULIZER.single_date <= LAST_DAY("{}") and SCHEDULIZER.single_date > LAST_DAY(DATE_SUB("{}", INTERVAL 1 MONTH)) 
            order by start_date ASC  
        """.format(self.today, self.today, self.today, self.today)
        temp_list = handle_select(query)

        # Add root dict
        for sched in temp_list:
            date = sched[0].strftime("%Y-%m-%d")
            if date not in schedule_event:
                schedule_event[date] = {}

        # Add nested dict from the root dict
        for event in temp_list:
            date = event[0].strftime("%Y-%m-%d")
            client_name = event[1]
            event_time = f'{event[2]} to {event[3]}'
            
            # Initialize the list if the client name does not exist in the date
            if client_name not in schedule_event[date]:
                schedule_event[date][client_name] = []
            
            # Append the event time to the client's list for that date
            schedule_event[date][client_name].append(event_time)

        return schedule_event

    def round_robin(self):
        rr_queue = []

        query_techs = """
            SELECT technician_id, CONCAT(first_name, ' ', last_name) AS 'Available Technician', state 
            FROM TECHNICIAN 
            WHERE state = 'Idle'
        """
        idle_technicians = handle_select(query_techs)
        if not idle_technicians:
            return "No Technicians available."

        for tech in idle_technicians:
            rr_queue.append(tech[0])  # Assuming the first element is technician_id

        # Shuffle the queue to randomize the starting point
        random.shuffle(rr_queue)

        schedules_tomorrow = self.show_sched_for_tom()
        if not schedules_tomorrow:
            return "No Schedules for tomorrow."

        rr_index = 0
        num_techs = len(rr_queue)
        for sched in schedules_tomorrow:
            schedule_id = sched[0]  # Schedule ID
            sched_time_in = sched[2]
            sched_time_out = sched[3]
            
            # Keep track of how many technicians we've checked
            technicians_checked = 0
            assigned = False

            while technicians_checked < num_techs:
                technician_id = rr_queue[rr_index]

                # Check for scheduling conflicts
                query_conflicts = """
                    SELECT time_in, time_out 
                    FROM SCHEDULE 
                    WHERE technician_id = {} 
                    AND ((time_in < '{}' AND time_out > '{}') OR 
                        (time_in < '{}' AND time_out > '{}') OR 
                        (time_in >= '{}' AND time_out <= '{}'))
                """.format(technician_id, sched_time_out, sched_time_in, sched_time_in, sched_time_out, sched_time_in, sched_time_out)
                existing_schedules = handle_select(query_conflicts)

                if not existing_schedules:
                    query_type = """
                        SELECT schedule_type
                        FROM SCHEDULE
                        WHERE schedule_id = {}
                        order by start_date, time_in, time_out ASC
                    """.format(schedule_id)
                    schedule_type = handle_select(query_type)[0][0]

                    # Check if the technician can be assigned based on the schedule type
                    if schedule_type == "Posting":
                        # Assign the technician to the schedule
                        self.assign_technician(schedule_id, technician_id)
                        # Remove the technician from the round robin queue
                        rr_queue.pop(rr_index)
                        num_techs -= 1
                        assigned = True
                    else:  # Default schedule type
                        # Check if the technician has been assigned less than twice
                        query_count = """
                            SELECT COUNT(*)
                            FROM SCHEDULE
                            WHERE technician_id = {} AND schedule_type = 'Default'
                        """.format(technician_id)
                        tech_assign_count = handle_select(query_count)[0][0]

                        if tech_assign_count < 2:
                            # Assign the technician to the schedule
                            self.assign_technician(schedule_id, technician_id)
                            assigned = True

                    if assigned:
                        break  # Exit the while loop to move on to the next schedule

                # Move to the next technician in the queue
                rr_index = (rr_index + 1) % num_techs
                technicians_checked += 1

            if not assigned:
                return "Could not assign all schedules due to conflicts."

        return "Technicians assigned successfully."

            
    def show_sched_for_tom(self):
        query = f"""
            select schedule_id, start_date, time_in, time_out 
            from SCHEDULE 
            where start_date = "2024-06-18" + interval 1 day and status = 'Idle' 
            union 
            select SCHEDULIZER.schedule_id, SCHEDULIZER.single_date, SCHEDULE.time_in, SCHEDULE.time_out 
            from SCHEDULIZER 
            inner join SCHEDULE on SCHEDULE.schedule_id = SCHEDULIZER.schedule_id 
            where SCHEDULIZER.single_date = "2024-06-18" + interval 1 day and SCHEDULE.status = 'Idle' 
            order by start_date, time_in, time_out ASC
        """
        return handle_select(query)    


    def edit_schedule_info(self, sched_id, categ, new_input):
        temp = "update SCHEDULE set {} = ".format(categ) 
        query = temp + "%s where schedule_id = %s"
        data = (new_input, sched_id)
        handle_transaction(query, data)


    def get_data(self, sched_id, categ):
        temp = "select {} from SCHEDULE ".format(categ)
        query = temp + "where schedule_id = {} and void = 0".format(sched_id)
        return handle_select(query)
    

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
    def placeholder_sched(self, sched_id):
        query = """
        select c.name, schedule_type, start_date, end_date, 
        time_in, time_out from schedule as s inner join 
        client as c on s.client_id = c.client_id where schedule_id = {};
        """.format(sched_id)
        return handle_select(query)

#s = Schedule()
#s.earliest_deadline_first()
#print(s.earliest_deadline_first_show())
#print(s.get_data(28, "client_id, schedule_type, start_date, end_date, time_in, time_out"))
#print(s.placeholder_sched(28))
#s.earliest_deadline_first
#s.add_schedule(1, "Default", "2024-06-11", "2024-06-22", "20:30:00", "21:00:00")
#print(s.assign_technician(14, 1))
#s.earliest_deadline_first()
#s.update_state_when_done(29, 1)
#temp = {}
#print(s.timetable(temp))
#print(s.round_robin())