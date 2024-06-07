from database import *
from query_settings import *

from datetime import date

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

    def avg_sale(self):
        query = (
            ""
        )

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

#s = Sales()
#s.add_sale(1, 10000)