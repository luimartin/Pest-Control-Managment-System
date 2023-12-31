from Database import *

def handle_transaction(query, data):
    try:
        mycursor.execute(query, data)
        mydb.commit()
        print("Sucessful Execution")
    except Error as error:
        mydb.rollback()
        print("Error type: {}".format(error))

def handle_select(query):
    output = None

    try:
        mycursor.execute(query)
        output = mycursor.fetchone()
    except Error as error:
        print("Error type: {}".format(error))

    return output
