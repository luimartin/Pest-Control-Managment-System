import mysql.connector
from mysql.connector import Error

# Connect database
mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'bowie',
	passwd = '030709',
	database = 'mansys'
)
mycursor = mydb.cursor()

"""
    MySQL Queries
	
	For creating tables
    1. DONE (VALIDATED)
    create table CLIENT(
        client_id int not null auto_increment,
		name varchar(50) not null,
		email varchar(50) not null,
		phone_num varchar(16) not null,
		address varchar(50) not null,
		status varchar(10) not null,
		void tinyint(1),
		PRIMARY KEY (client_id)
    );

	2. DONE (VALIDATED)
	create table CONTRACT(
        contract_id int not null auto_increment,
		client_id int, 
		problem varchar(70) not null,
        service_type varchar(50) not null,
		start_date date not null,
		end_date date not null, 
	    square_meter decimal(5,2) not null,
		unit int not null,
		price decimal(10,2) not null,
		PRIMARY KEY (contract_id), 
		CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES CLIENT(client_id)
    );
	
	3. DONE (VALIDATED) 
	create table SCHEDULE(
        schedule_id int not null auto_increment,
		client_id int,
		technician_id int,
		schedule_type varchar(20) not null,
		start_date date not null,
		end_date date not null,
		time_in datetime not null,
		time_out datetime not null,
        PRIMARY KEY (schedule_id),
        CONSTRAINT fk_client_sched FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
		CONSTRAINT fk_technician FOREIGN KEY (technician_id) REFERENCES TECHNICIAN(technician_id)
	);

    3.1 DONE (VALIDATED)
    create table SCHEDULIZER(
		schedulizer_id int not null auto_increment,
        schedule_id int,
        single_date date not null,
        PRIMARY KEY (schedulizer_id),
        CONSTRAINT fk_schedizer FOREIGN KEY (schedule_id) REFERENCES SCHEDULE(schedule_id)
	);
	
    4. DONE (VALIDATED)
	create table TECHNICIAN(        
        technician_id int not null auto_increment,
		first_name varchar(50) not null,
		last_name varchar(50) not null,
        phone_num varchar(16) not null,
		address varchar(50) not null,
		void tinyint(1),
        PRIMARY KEY (technician_id)
	);
	
	5. DONE (VALIDATED)
	create table TECHNICIAN_ITEM(
		technician_item_id int not null auto_increment,
        technician_id int, 
		item_id int,
		quantity int not null,
		date_acquired date not null,
        PRIMARY KEY (technician_item_id),
		CONSTRAINT fk_technician_assign FOREIGN KEY (technician_id) REFERENCES TECHNICIAN(technician_id),
        CONSTRAINT fk_inventory FOREIGN KEY (item_id) REFERENCES INVENTORY(item_id)
    );
	
	6. DONE (VALIDATED)
	create table INVENTORY(
        item_id int not null auto_increment, 
		item_name varchar(50) not null, 
		item_type varchar(50) not null,
		quantity int not null,  
		expiration date,
		description varchar(255), 
        void tinyint(1) not null,
		PRIMARY KEY (item_id)
    );
	
	7. PARTIAL
	create table CATEGORY(
        category_id int not null auto_increment,
		category_name varchar(50) not null, 
		PRIMARY KEY (category_id)
    );
	
	8.  
	create table SALES(
        sale_id int not null auto_increment,
		figure decimal(10, 2) not null,
        sale_date date not null,
		PRIMARY KEY (sale_id)
	);
	
	9. DONE (Validated) 
    create table MESSAGE(
        message_id int not null auto_increment,
        client_id int, 
        technician_id int,
        message_category varchar(50),
        message varchar(255),
        PRIMARY KEY (message_id),
        CONSTRAINT fk_client_msg FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
        CONSTRAINT fk_technician_msg FOREIGN KEY (technician_id) REFERENCES TECHNICIAN(technician_id)
    );
    
	10. DONE (VALIDATED)
	create table USER(
        user_id int not null auto_increment,
		username varchar(20) not null UNIQUE KEY,
		password char(32) not null,  
		PRIMARY KEY (user_id)
    );
	
"""