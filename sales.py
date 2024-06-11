from database import *
from query_settings import *

from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

class Sales:
    def __init__(self):
        pass
    
    def add_sale(self, client_id, figure):
        sale_date = date.today()

        query = "select client_id from CLIENT where client_id = {}".format(client_id)
        valid_id = handle_select(query)[0][0]

        if valid_id is not None:
            query = (
                "insert into SALES (client_id, figure, sale_date)"
                "values (%s, %s, %s)"
            )
            data = (valid_id, figure, sale_date)
            handle_transaction(query, data)

    def monthly_total_sale(self):
        query = (
            "select date_format(sale_date, '%Y-%m'), sum(figure) "
            "from SALES "
            "group by date_format(sale_date, '%Y-%m') "
            "order by date_format(sale_date, '%Y-%m')"
        )
        return handle_select(query)
    
    def monthly_avg_total_sale(self):
        query = (
            "select year(sale_date), date_format(sale_date, '%M'), avg(figure) from SALES "
            "group by year(sale_date), month(sale_date) "
            "order by year(sale_date), month(sale_date)"
        )
        return handle_select(query)

    def sale_trend(self):
        data = self.monthly_total_sale()
    
        dates = [row[0] for row in data]
        total = [row[1] for row in data]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, total, marker='o', linestyle='-')
        plt.xlabel('Date')
        plt.ylabel('Total Sale')
        plt.title('Monthly Total Sale')
        plt.xticks(rotation=45)
        plt.grid(True)
        
        window_size = 3 
        moving_avg = []
        for i in range(len(total) - window_size + 1):
            avg = sum(total[i:i+window_size]) / window_size
            moving_avg.append(avg)
        
        last_date = datetime.strptime(dates[-1], '%Y-%m')  # Convert last date string to datetime
        next_dates = [last_date + relativedelta(months=i) for i in range(1, 4)]
        
        last_value = total[-1]
        prediction = [last_value] * 3
        
        plt.plot(dates[:-window_size+1], moving_avg, color='red', linestyle='--', label='Moving Average')
        plt.plot([date.strftime('%Y-%m') for date in next_dates], prediction, color='green', linestyle='--', label='Predicted Total Sale')
        plt.legend()
        
        plt.tight_layout()
        plt.show()

    def paid_client(self, client_id):
        query = """
            select CLIENT.name from CLIENT
            inner join SALES on SALES.client_id = {}
            where CLIENT.client_id = {}
        """.format(client_id)
        return handle_select(query)[0][0]
    
    def edit_sale_info(self, sale_id, categ, new_input):
        temp = "update SALES set {} = ".format(categ)
        query = temp + "%s where sale_id = %s"
        data = (new_input, sale_id)
        handle_transaction(query, data)

    def get_data(self, sale_id, categ, new_input):
        temp = "select {} from SALES ".format(categ)
        query = temp + "where sale_id = {}".format(sale_id)
        return handle_select(query)[0][0]

    def search(self, input):
        query = f"""
            select * from SALES 
            where ( sale_id LIKE '%{input}%'
            OR client_id LIKE '%{input}%'
            OR figure LIKE '%{input}%' 
            OR sale_date LIKE '%{input}%' 
            )
        """
        return handle_select(query) 

'''s = Sales()
s.add_sale(1, 30000)
print(s.sale_trend())'''
#s = Sales()
#print(s.search("10000"))