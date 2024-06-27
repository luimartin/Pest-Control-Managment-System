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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from io import BytesIO
import io

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
            subtitle1 = Paragraph("N. Domingo St., San Juan City, Metro Manila", subtitle_style)
            subtitle2 = Paragraph("Sales Analysis Report Summary", section_title_center_style)
            elements.extend([title, subtitle1, Spacer(1, 20), subtitle2, Spacer(1, 20)])

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

            # Build the PDF document
            doc.build(elements)

            return f"PDF generated successfully: {file_name}"

        except Exception as e:
            return f"PDF generation failed: {str(e)}"

    
s = Sales()
#s.add_sale(10, 250000, "2022-04-19")
#s.sale_trend()
#s.generate_report()
