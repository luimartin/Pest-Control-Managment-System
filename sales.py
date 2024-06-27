from database import *
from query_settings import *

from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus.doctemplate import PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from io import BytesIO
import io
import numpy as np
from sklearn.linear_model import LinearRegression

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
    
    def compute_daily_sales(self):
        query = """
        select year(sale_date), date_format(sale_date, '%M, %d'), sum(figure) as total_sales
        from sales
        group by sale_date;
        """
        return handle_select(query)
    
    def report_month_analysis_query(self):
        query = """ select year(sale_date), date_format(sale_date, '%M'), sum(figure), Round(avg(figure), 2)
            from SALES where void = 0
            group by year(sale_date), date_format(sale_date, '%M') 
            order by year(sale_date) desc;"""
        return handle_select(query)
    
    def report_year_analysis_query(self):
        query = """select year(sale_date), sum(figure), Round(avg(figure), 2)
            from SALES where void = 0
            group by year(sale_date);"""
        return handle_select(query)
        
    def generate_trend_graph(self, data, title, x_label, y_label, filename):
        years = [row[0] for row in data]
        values = [row[1] for row in data]

        plt.figure(figsize=(5, 4))
        plt.plot(years, values, marker='o', linestyle='-', color='b', label=y_label)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(years)
        plt.legend()

        # Save plot to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()
        buffer.seek(0)
        return buffer.getvalue()  # Return the bytes object containing the image

    def generate_3_month_forecast(self, df_month_analysis):
        # Prepare the data for linear regression
        X = np.array([i for i in range(len(df_month_analysis))]).reshape(-1, 1)
        y = df_month_analysis['Service Revenue'].values

        # Fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Get the slope and intercept of the trend line
        slope = model.coef_[0]
        intercept = model.intercept_

        # Generate the forecasted values for the next 3 months
        forecast = []
        for i in range(1, 4):
            forecast_value = slope * (len(df_month_analysis) + i) + intercept
            forecast.append(forecast_value)

        return forecast

    def generate_report(self):
        try:
            df = pd.DataFrame(self.compute_daily_sales())
            df_month_analysis = pd.DataFrame(self.report_month_analysis_query())
            df_year_analysis = pd.DataFrame(self.report_year_analysis_query())

            # Define the file name for the PDF file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f'sales_analysis_report_{timestamp}.pdf'

            # Create a PDF document
            doc = SimpleDocTemplate(file_name, pagesize=letter)
            elements = []

            # Set up text styles
            styles = getSampleStyleSheet()
            title_style = styles['Title']
            subtitle_style = ParagraphStyle('Subtitle', fontSize=12, leading=14, alignment=1)
            section_title_center_style = ParagraphStyle('SectionTitleCenter', fontSize=14, leading=16, spaceAfter=12, alignment=1)
            section_title_left_style = ParagraphStyle('SectionTitleLeft', fontSize=14, leading=16, spaceAfter=10, alignment=0)
            normal_style = styles['Normal']

            # Add title and subtitles
            title = Paragraph("HomeFix Pest and Termite Control Services", title_style)
            subtitle1 = Paragraph("190-C N. Domingo St., San Juan City, Metro Manila", subtitle_style)
            subtitle11 = Paragraph("Tel No: (02) 664-9120", subtitle_style)
            subtitle12 = Paragraph("Cel No: 09175724420", subtitle_style)
            subtitle2 = Paragraph("Sales Analysis Report Summary", section_title_center_style)
            elements.extend([title, subtitle1, subtitle11, subtitle12, Spacer(1, 25), subtitle2, Spacer(1, 20)])

            # Function to create tables with fixed column widths
            def create_table(data, col_widths):
                table = Table(data, colWidths=col_widths)
                table.setStyle(table_style)
                return table

            # Define table styles
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ])

            # Set column widths
            col_widths_sales = [150, 100, 150]  # Widths for Sales Report table
            col_widths_month = [100, 100, 150, 150]  # Widths for Month Analysis table
            col_widths_year = [150, 150, 150]  # Widths for Year Analysis table

            # === Daily Analysis ===
            elements.append(Paragraph("Daily Analysis:", section_title_left_style))
            if not df.empty:
                df.columns = ["Year", "Date", "Daily Service"]
                data = [df.columns.tolist()] + df.values.tolist()
                table = create_table(data, col_widths_sales)
                elements.append(table)
            else:
                elements.append(Paragraph("No data for Daily Analysis to export", normal_style))
            elements.append(Spacer(1, 20))

            # === Month Analysis ===
            elements.append(Paragraph("Month Analysis:", section_title_left_style))
            if not df_month_analysis.empty:
                df_month_analysis.columns = ["Year", "Month", "Service Revenue", "Average Service Revenue"]
                data = [df_month_analysis.columns.tolist()] + df_month_analysis.values.tolist()
                table = create_table(data, col_widths_month)
                elements.append(table)

            else:
                elements.append(Paragraph("No data for Month Analysis to export", normal_style))
            elements.append(Spacer(1, 20))

            # === Year Analysis ===
            elements.append(Paragraph("Year Analysis:", section_title_left_style))
            if not df_year_analysis.empty:
                df_year_analysis.columns = ["Year", "Service Revenue", "Average Service Revenue"]
                data = [df_year_analysis.columns.tolist()] + df_year_analysis.values.tolist()
                table = create_table(data, col_widths_year)
                elements.append(table)
                elements.append(Spacer(1, 20))
                # Generate trend graph for Year Analysis
                year_graph_data = df_year_analysis[["Year", "Service Revenue"]].values.tolist()
                year_graph_buffer = self.generate_trend_graph(year_graph_data, 'Annual Service Revenue Trend', 'Year', 'Service Revenue', 'year_trend.png')
                year_graph_image = Image(io.BytesIO(year_graph_buffer))  # Ensure to wrap in io.BytesIO
                elements.append(year_graph_image)

            else:
                elements.append(Paragraph("No data for Year Analysis to export", normal_style))

            if not df_month_analysis.empty:
                # Generate the 3-month forecast
                forecast = self.generate_3_month_forecast(df_month_analysis)

                # Add the forecast to the report
                elements.append(Paragraph("3-Month Forecast:", section_title_left_style))
                forecast_table_data = [["Month", "Forecasted Service Revenue"]]
                for i, value in enumerate(forecast):
                    current_month = df_month_analysis.index[-1] + i + 1
                    forecast_table_data.append([f"After {i+1} months", f"{value:.2f}"])
                forecast_table = create_table(forecast_table_data, [150, 150])
                elements.append(forecast_table)
                elements.append(Spacer(1, 20))


            elements.append(PageBreak())
            # Define the bottom frame for date and other footer elements
            def add_footer(canvas, doc):
                canvas.saveState()
                canvas.setFont('Helvetica', 9)
                width, height = doc.pagesize

                # Draw the "Generated by" text above the "Report generated on" text
                footer_text2 = "Generated by: _____________"
                footer_text = datetime.now().strftime("Report generated on %Y-%m-%d at %H:%M:%S")

                # Positioning the texts appropriately
                canvas.drawRightString(width - inch, 0.6 * inch, footer_text2)
                canvas.drawRightString(width - inch, 0.4 * inch, footer_text)

                canvas.restoreState()

            # Add PageTemplate with custom onPage for the last page
            doc.addPageTemplates([
                PageTemplate(id='LastPageTemplate', frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='last')],
                            onPage=add_footer)
            ])

            # Build the PDF document
            doc.build(elements, onLaterPages=add_footer)

            return f"PDF generated successfully: {file_name}"

        except Exception as e:
            return f"PDF generation failed: {str(e)}"

    
s = Sales()
#s.add_sale(10, 250000, "2022-04-19")
#s.sale_trend()
#s.generate_report()