from database import *
from query_settings import *

from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
            select c.name, figure, sale_date, s.sale_id 
            from sales as s left join client as c on c.client_id = s.client_id  
            where ( sale_id LIKE '%{input}%'
            OR s.client_id LIKE '%{input}%'
            OR figure LIKE '%{input}%' 
            OR sale_date LIKE '%{input}%' 
            OR c.name LIKE '%{input}%' 
            )
        """
        return handle_select(query) 
    
    def report_sale_query(self):
        query = """select c.name, figure, sale_date
        from sales as s left join client as c on c.client_id = s.client_id 
        where s.void = 0;"""
        return handle_select(query)
    
    def report_month_analysis_query(self):
        query = """ select year(sale_date), date_format(sale_date, '%M'), sum(figure), avg(figure)
            from SALES where void = 0
            group by year(sale_date) ,date_format(sale_date, '%M') 
            order by date_format(sale_date, '%M') desc;"""
        return handle_select(query)
    
    def report_year_analysis_query(self):
        query = """select year(sale_date), sum(figure), avg(figure)
            from SALES where void = 0
            group by year(sale_date);"""
        return handle_select(query)
        
    def generate_report(self):
        df = pd.DataFrame(self.report_sale_query())
        df_month_analysis = pd.DataFrame(self.report_month_analysis_query())
        df_year_analysis = pd.DataFrame(self.report_year_analysis_query())

        # Define the file name for the PDF file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f'sales_analysis_report_{timestamp}.pdf'

        # Create a PDF document
        c = canvas.Canvas(file_name, pagesize=letter)

        # Set up text styles
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(300, 750, "Sales Analysis Report")

        # Move to the next line
        c.setFont("Helvetica", 12)

        # === Sales Report ===
        c.drawString(100, 700, "Sales Report:")

        # Assign column names
        df.columns = ["Name", "Figure", "Date Paid"]

        # Export df to the PDF
        if df is not None and not df.empty:
            df_columns = list(df.columns)
            data = [df_columns] + list(df.values.tolist())
            for row_idx, row in enumerate(data, start=1):
                for col_idx, cell in enumerate(row):
                    c.drawString(100 + col_idx * 120, 680 - row_idx * 20, str(cell))

        else:
            c.drawString(100, 680, "No data for Sales Report to export")

        # Move to the next section
        c.drawString(100, 640 - len(df.index) * 20, "-" * 80)  # Separator line

        # === Month Analysis ===
        c.drawString(100, 620 - len(df.index) * 20, "Month Analysis:")

        # Assign column names
        df_month_analysis.columns = ["Year", "Month", "Total Sales", "Average Sales"]

        # Export df_month_analysis to the PDF
        if not df_month_analysis.empty:
            df_month_columns = list(df_month_analysis.columns)
            data = [df_month_columns] + list(df_month_analysis.values.tolist())
            for row_idx, row in enumerate(data, start=1):
                for col_idx, cell in enumerate(row):
                    c.drawString(100 + col_idx * 120, 600 - len(df.index) * 20 - row_idx * 20, str(cell))

        else:
            c.drawString(100, 600 - len(df.index) * 20, "No data for Month Analysis to export")

        # Move to the next section
        c.drawString(100, 560 - (len(df.index) + len(df_month_analysis.index)) * 20, "-" * 80)  # Separator line

        # === Year Analysis ===
        c.drawString(100, 540 - (len(df.index) + len(df_month_analysis.index)) * 20, "Year Analysis:")

        # Assign column names
        df_year_analysis.columns = ["Year", "Total Sales", "Average Sales"]

        # Export df_year_analysis to the PDF
        if not df_year_analysis.empty:
            df_year_columns = list(df_year_analysis.columns)
            data = [df_year_columns] + list(df_year_analysis.values.tolist())
            for row_idx, row in enumerate(data, start=1):
                for col_idx, cell in enumerate(row):
                    c.drawString(100 + col_idx * 120, 520 - (len(df.index) + len(df_month_analysis.index)) * 20 - row_idx * 20, str(cell))

        else:
            c.drawString(100, 520 - (len(df.index) + len(df_month_analysis.index)) * 20, "No data for Year Analysis to export")

        # Save the PDF document
        c.save()

        return f"PDF generated successfully: {file_name}"

    
#s = Sales()
#s.sale_trend()
#s.generate_report()
