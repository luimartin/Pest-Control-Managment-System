from database import *
from query_settings import *

from datetime import date

class Sales:
    def __init__(self):
        pass
    
    def add_sale(self, figure):
        sale_date = date.today()

        query = (
            "insert into SALES (figure, sale_date)"
            "values (%s, %s)"
        )
        data = (figure, sale_date)
        handle_transaction(query, data)

    def edit_sale_info(self, sale_id, categ, new_input):
        temp = "update SALES set {} = ".format(categ)
        query = temp + "%s where sale_id = %s"
        data = (new_input, sale_id)
        handle_transaction(query, data)

    def get_data(self, sale_id, categ, new_input):
        temp = "select {} from SALES ".format(categ)
        query = temp + "where sale_id = {}".format(sale_id)
        return handle_select(query)[0][0]
