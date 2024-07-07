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
        print(self.today)

    def show_tech(self):
        query = """
        select technician_id ,concat(TECHNICIAN.first_name,
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
                where s.void = 0 and c.void = 0 order by
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
            temp_query = "select max(schedule_id) from SCHEDULE;"
            sched_id = handle_select(temp_query)[0][0]
            print(sched_id)

            self.posting_schedulizer(sched_id, start_date, end_date)

    def earliest_deadline_first(self):
        query1 = """ 
                select schedule_id, start_date, time_in, time_out
                from SCHEDULE 
                where start_date like '{}%' and void = 0
                union
                select SCHEDULIZER.schedule_id, SCHEDULIZER.single_date, "09:00:00", "17:00:00" 
                from SCHEDULIZER 
                inner join SCHEDULE on SCHEDULE.schedule_id = SCHEDULIZER.schedule_id  
                where single_date like '{}%' and SCHEDULE.void = 0 
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
        select schedule_id ,c.name, schedule_type, start_date, end_date, time_in, 
	    time_out, s.status, concat("[", TECHNICIAN.technician_id, "]", " ", 
        TECHNICIAN.first_name, " ", TECHNICIAN.last_name) from schedule as s
        inner join client as c on s.client_id = c.client_id
        left join TECHNICIAN on TECHNICIAN.technician_id = s.technician_id
        where s.void = 0 and s.status = 'Progress'
        """
        return handle_select(query)

    
    def update_state_when_done(self, sched_id):
        query_technician_id = """
        SELECT technician_id 
        FROM SCHEDULE 
        WHERE schedule_id = {}
        """.format(sched_id)
        technician_id = handle_select(query_technician_id)[0][0] 

        if not technician_id:
            return "No technician assigned to this schedule."
        

        # Check if the technician is assigned to any other schedules
        query_check_other_assignments = """
        SELECT COUNT(*) 
        FROM SCHEDULE 
        WHERE technician_id = {} AND status != 'Done' 
        """.format(technician_id)
        count = handle_select(query_check_other_assignments)[0][0]


        query = """
        UPDATE SCHEDULE 
        SET status = case 
            when schedule_type = 'Posting' then 'Idle'
            else 'Done'
        end,
        technician_id = NULL 
        WHERE schedule_id = %s ;
        """
        data = (sched_id, )
        handle_transaction(query, data)

        if count == 1:
            # If no other schedules are assigned to this technician, update their state to 'Idle'
            query_update_technician = """
            UPDATE TECHNICIAN 
            SET state = 'Idle' 
            WHERE technician_id = %s 
            """
            data_check = (technician_id, )
            handle_transaction(query_update_technician, data_check)

        return "Schedule status updated successfully."

        
    def posting_schedulizer(self, sched_id, start_date, end_date):
        ref_sched = start_date
        day_tester = None

        while(True):
            temp_query = "select dayname({})".format("\'"+ref_sched+"\'")
            day_tester = handle_select(temp_query)[0][0]

            if day_tester != 'Sunday':
                query = (
                    "insert into SCHEDULIZER (schedule_id, single_date, single_status)"
                    "values (%s, %s, %s)"                
                )
                data = (sched_id, ref_sched, 'Idle')
                handle_transaction(query, data)

            if ref_sched == end_date: break
            ref_sched = self.modifyDate(ref_sched)        
       

    def modifyDate(self, ref_sched):
        date = datetime.strptime(ref_sched,  '%Y-%m-%d')
        modified_date = date + timedelta(days = 1)
        
        return datetime.strftime(modified_date, '%Y-%m-%d')
    

    def posting_modifier(self, sched_id, new_start_date, new_end_date):
        prev_start_date = datetime.strftime(self.get_data(sched_id, 'start_date'), '%Y-%m-%d') 
        prev_end_date = datetime.strftime(self.get_data(sched_id, 'end_date'), '%Y-%m-%d')  

        self.edit_schedule_info(sched_id, 'start_date', new_start_date)
        self.edit_schedule_info(sched_id, 'end_date', new_end_date)   

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
                AND void = 0
            """.format(sched_id)
            schedule_time = handle_select(query_schedule_time)

            if not schedule_time:
                return "Schedule not found."

            new_time_in, new_time_out, new_start_date, assigned_tech_id = schedule_time[0]

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
                AND void = 0
            """.format(tech_id, new_start_date, new_time_out, new_time_in, new_time_in, new_time_out, new_time_in, new_time_out)
            existing_schedules = handle_select(query_conflicts)
            print("Existing Schedules", existing_schedules)

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

            return "Technician assigned successfully!"
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
            select SCHEDULE.start_date, concat("[", schedule.schedule_id, "]", " ", client.name), SCHEDULE.time_in, SCHEDULE.time_out, SCHEDULE.status 
            from SCHEDULE 
            inner join CLIENT on SCHEDULE.client_id = CLIENT.client_id 
            where SCHEDULE.start_date <= LAST_DAY("{}") and SCHEDULE.start_date > LAST_DAY(DATE_SUB("{}", INTERVAL 1 MONTH)) 
            and SCHEDULE.void = 0
            union 
            select SCHEDULIZER.single_date, concat("[", schedule.schedule_id, "]", " ", client.name), "09:00:00", "17:00:00", CASE WHEN SCHEDULIZER.single_date = "{}" THEN "Progress" ELSE SCHEDULIZER.single_status END
            from SCHEDULIZER 
            inner join SCHEDULE on SCHEDULIZER.schedule_id = SCHEDULE.schedule_id
            inner join CLIENT on SCHEDULE.client_id = CLIENT.client_id 
            where SCHEDULIZER.single_date <= LAST_DAY("{}") and SCHEDULIZER.single_date > LAST_DAY(DATE_SUB("{}", INTERVAL 1 MONTH)) 
            and SCHEDULE.void = 0 
            order by start_date ASC;
        """.format(self.today, self.today, self.today, self.today, self.today)
        print(self.today)
        temp_list = handle_select(query)
        print("1")

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
            status = event[4]

            # Initialize the list if the client name does not exist in the date
            if client_name not in schedule_event[date]:
                schedule_event[date][client_name] = []
            
            # Append the event time to the client's list for that date
            schedule_event[date][client_name].append((event_time, status))

        return schedule_event

    def round_robin(self):
        rr_queue = []

        # Get the list of idle technicians
        query_techs = """
            SELECT technician_id, CONCAT(first_name, ' ', last_name) AS 'Available Technician', state 
            FROM TECHNICIAN 
            WHERE state = 'Idle' and void = 0
        """
        idle_technicians = handle_select(query_techs)
        print("Output", idle_technicians)

        if not idle_technicians:
            return "No Technicians available."

        for tech in idle_technicians:
            rr_queue.append(tech[0])  # Assuming the first element is technician_id
        print("Output", rr_queue)
        # Shuffle the queue to randomize the starting point
        random.shuffle(rr_queue)

        # Get the schedules for tomorrow
        schedules_tomorrow = self.show_sched_for_tom()
        print("SCHED FOR TOM:", schedules_tomorrow)
        
        if not schedules_tomorrow:
            return "No Schedules for tomorrow."

        all_assigned = True
        for sched in schedules_tomorrow:
            if sched[8] is None:
                all_assigned = False
                break

        if all_assigned:
            return "All schedules for tomorrow are already assigned."

        rr_index = 0
        num_techs = len(rr_queue)
        for sched in schedules_tomorrow:
            schedule_id = sched[0]  # Schedule ID
            technician_id_assigned = sched[8]  # Assuming the second element is technician_id
            sched_time_in = sched[2]
            sched_time_out = sched[3]

            if technician_id_assigned is not None:
                continue  # Skip if the schedule is already assigned

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
                    and void = 0
                """.format(technician_id, sched_time_out, sched_time_in, sched_time_in, sched_time_out, sched_time_in, sched_time_out)
                existing_schedules = handle_select(query_conflicts)

                if not existing_schedules:
                    query_type = """
                        SELECT schedule_type
                        FROM SCHEDULE
                        WHERE schedule_id = {} and void = 0
                        ORDER BY start_date, time_in, time_out ASC
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
                    else: 
                        # Check if the technician has been assigned less than twice
                        query_count = """
                            SELECT COUNT(*)
                            FROM SCHEDULE
                            WHERE technician_id = {} AND schedule_type = 'Default' and void = 0
                        """.format(technician_id)
                        tech_assign_count = handle_select(query_count)[0][0]

                        if tech_assign_count < 2:
                            # Assign the technician to the schedule
                            self.assign_technician(schedule_id, technician_id)
                            assigned = True

                    if assigned:
                        # Move to the next technician in the queue
                        rr_index = (rr_index + 1) % num_techs
                        technicians_checked += 1
                        print("done")
                        break  # Exit the while loop to move on to the next schedule

                # Move to the next technician in the queue
                rr_index = (rr_index + 1) % num_techs
                technicians_checked += 1

            if not assigned:
                return "Could not assign all schedules due to conflicts."

        return "Technicians assigned successfully."

            
    def show_sched_for_tom(self):
        query = """
            select schedule_id, name, schedule_type, start_date, end_date, time_in, time_out, SCHEDULE.status, concat("[", TECHNICIAN.technician_id, "]", " ", 
			TECHNICIAN.first_name, " ", TECHNICIAN.last_name)
            from SCHEDULE inner join client on client.client_id = SCHEDULE.client_id
            left join TECHNICIAN on TECHNICIAN.technician_id = SCHEDULE.technician_id
            where start_date = '{}' + interval 1 day and SCHEDULE.status = 'Idle' and SCHEDULE.void = 0
            union 
            select SCHEDULIZER.schedule_id, name ,SCHEDULE.schedule_type, SCHEDULIZER.single_date, SCHEDULE.end_date ,SCHEDULE.time_in, SCHEDULE.time_out, SCHEDULIZER.single_status,  concat("[", TECHNICIAN.technician_id, "]", " ", 
			TECHNICIAN.first_name, " ", TECHNICIAN.last_name) 
            from SCHEDULIZER 
            inner join SCHEDULE on SCHEDULE.schedule_id = SCHEDULIZER.schedule_id 
            inner join client on client.client_id = SCHEDULE.client_id
            left join TECHNICIAN on TECHNICIAN.technician_id = SCHEDULE.technician_id
            where SCHEDULIZER.single_date = '{}' + interval 1 day and SCHEDULIZER.single_status = 'Idle' and SCHEDULE.void = 0
            order by start_date, time_in, time_out ASC;
        """.format(self.today, self.today)
        print(handle_select(query))
        return handle_select(query)    

    # Used to finished the schedule when current day is greater than end_date
    def set_sched_to_finish(self):
        query = """
            select schedule_id, end_date from SCHEDULE
            where void = 0 
            and DATE_SUB(end_date, INTERVAL - 1 DAY) = '2024-07-06'
            and status != 'Progress' and status != 'Unfinished'
        """.format(self.today)
        f_sched = handle_select(query)
        
        if f_sched:
            for sched in f_sched:
                if sched[1] < self.today:
                    query = """
                        update SCHEDULE 
                        set status = 'Finished'
                        where schedule_id = %s and void = 0 
                    """
                    data = (sched[0], )
                    handle_transaction(query, data) 
                    
    # Used to finished the 'progress' schedule when not updated by the admin
    def set_progress_to_unfinish(self):
        query = """
            select SCHEDULE.schedule_id, SCHEDULE.start_date, SCHEDULE.schedule_type 
            from SCHEDULE 
            where SCHEDULE.status = 'Progress'
            and SCHEDULE.void = 0 
            and DATE_SUB(SCHEDULE.start_date, INTERVAL - 1 DAY) = '2024-07-06'
            union
            select SCHEDULIZER.schedule_id, SCHEDULIZER.single_date, SCHEDULE.schedule_type 
            from SCHEDULIZER 
            inner join SCHEDULE on SCHEDULE.schedule_id = SCHEDULIZER.schedule_id 
            where SCHEDULE.status = 'Progress'
            and SCHEDULE.void = 0 
            and DATE_SUB(SCHEDULIZER.single_date, INTERVAL - 1 DAY) = '2024-07-06'
        """.format(self.today, self.today)
        prog_sched_id = handle_select(query)
        print(prog_sched_id)

        if prog_sched_id:
            for sched in prog_sched_id:
                if sched[1] < self.today:
                    query = """
                        update SCHEDULE 
                        set status = case 
                            when schedule_type = 'Posting' and end_date >= %s then 'Idle' 
                            else 'Unfinished' 
                        end
                        where status = 'Progress' and schedule_id = %s and void = 0 
                    """
                    data = ('2024-07-06', sched[0], )
                    handle_transaction(query, data) 

    def edit_schedule_info(self, sched_id, categ, new_input):
        temp = "update SCHEDULE set {} = ".format(categ) 
        query = temp + "%s where schedule_id = %s"
        data = (new_input, sched_id)
        handle_transaction(query, data)

    def get_data(self, sched_id, categ):
        temp = "select {} from SCHEDULE ".format(categ)
        query = temp + "where schedule_id = {} and void = 0".format(sched_id)
        print(handle_select(query))
        return handle_select(query)[0][0]
    

    def search(self, input):
        query = f"""
            select schedule_id ,c.name, schedule_type, start_date, end_date, time_in, 
            time_out, s.status, concat("[", TECHNICIAN.technician_id, "]", " ", 
            TECHNICIAN.first_name, " ", TECHNICIAN.last_name) from schedule as s
            inner join client as c on s.client_id = c.client_id
            left join TECHNICIAN on TECHNICIAN.technician_id = s.technician_id
            where (
            schedule_id LIKE '%{input}%'
            OR s.client_id LIKE '%{input}%'
            OR s.technician_id LIKE '%{input}%' 
            OR schedule_type LIKE '%{input}%' 
            OR start_date LIKE '%{input}%' 
            OR time_in LIKE '%{input}%'
            OR time_out LIKE '%{input}%'
            OR c.name LIKE '%{input}%'
            ) and s.void = 0
        """
        return handle_select(query)
    
    def placeholder_sched(self, sched_id):
        query = """
        select c.name, schedule_type, start_date, end_date, 
        time_in, time_out from schedule as s inner join 
        client as c on s.client_id = c.client_id where schedule_id = {};
        """.format(sched_id)
        return handle_select(query)
    
    def smsview(self):
        query = """
        select schedule_id, name from schedule
        inner join 
        client on schedule.client_id = client.client_id and schedule.void = 0 and client.void = 0;
        """
        return handle_select(query)
    
    def assigntechview(self):
        query = """
        select schedule_id, name from schedule
        inner join 
        client on schedule.client_id = client.client_id
        where schedule.technician_id is Null 
        and schedule.void = 0 and 
        client.void = 0 and (schedule.status = "Idle" or schedule.status = "Progress" )
        """

        return handle_select(query)
    


s = Schedule()
#print(s.assigntechview())
#s.set_progress_to_done()
#print(s.get_data(28, 'technician_id'))
#s.edit_schedule_info(29, 'technician_id' , None)
#print(s.get_data(29, 'start_date'))
#print(s.smsview())
#print(s.show_sched_for_tom())
#s.earliest_deadline_first()
#print(s.earliest_deadline_first_show())
#print(s.get_data(28, "client_id, schedule_type, start_date, end_date, time_in, time_out"))
#print(s.placeholder_sched(28))
#s.earliest_deadline_first
#s.add_schedule(1, "Default", "2024-06-11", "2024-06-22", "20:30:00", "21:00:00")
#print(s.assign_technician(14, 1))
#s.earliest_deadline_first()
#s.update_state_when_done(28, 9)
#temp = {}
#print(s.timetable(temp))
#print(s.round_robin())
#s.set_sched_to_finish()
#s.set_progress_to_unfinish()