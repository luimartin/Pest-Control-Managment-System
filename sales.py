from database import *
from query_settings import *

from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas as pd

class Sales:
    def __init__(self):
        pass
    
    def view_all_sales(self):
        query = "select c.name, figure, sale_date, s.sale_id from sales as s left join client as c on c.client_id = s.client_id where s.void = 0;"
        return handle_select(query)
    
    def view_specific_sales(self, sale_id):
        query = """
        select c.name, figure, sale_date from sales as s
        inner join client as c on c.client_id = s.client_id
        where s.void = 0 and sale_id = {};;
        """.format(sale_id)
        return handle_select(query)
    
    def add_sale(self, client_id, figure, date):

            query = (
                "insert into SALES (client_id, figure, sale_date, void)"
                "values (%s, %s, %s, %s)"
            )
            data = (client_id, figure, date, 0)
            handle_transaction(query, data)

    def monthly_total_sale(self):
        query = """
            select year(sale_date), date_format(sale_date, '%M'), sum(figure) 
            from SALES where void = 0
            group by year(sale_date) ,date_format(sale_date, '%M') 
            order by date_format(sale_date, '%M') desc;
        """
        return handle_select(query)
    
    def monthly_avg_total_sale(self):
        query = """
                    select year(sale_date), date_format(sale_date, '%M'), cast(avg(figure) as decimal(10,2)) from SALES  where void = 0
            group by year(sale_date), DATE_FORMAT(sale_date, '%M');
        """
        return handle_select(query)

    def sale_trend(self):
        data = self.monthly_total_sale()

        # Convert the month names to month numbers
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        dates = []
        for row in data:
            year = row[0]
            month_name = row[1]
            month_num = month_names.index(month_name) + 1
            date_str = f"{year}-{month_num:02d}"
            dates.append(date_str)
        total = [row[2] for row in data]
        plt.rcParams['toolbar'] = 'None'
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

        last_date = datetime.strptime(dates[-1], '%Y-%m')
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
            where CLIENT.client_id = {} and void = 0
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
        
    def generate_report(self):
        df = pd.DataFrame(self.view_all_sales())
        
        if df is not None:
            # Exporting to Excel
            df.columns = ["Name", "Figure", "SaleDate", "SaleID"]
            #print(df)
            df.to_excel('sales_report.xlsx', index=False )
            return "Spreadsheet generated successfully"
        else:
            return "No data to export"

#s = Sales()
#s.sale_trend()
#s.generate_report()
