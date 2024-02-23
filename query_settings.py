from database import *

# Use to handle insert, update, and delete queries
def handle_transaction(query, data):
    try:
        mycursor.execute(query, data)
        mydb.commit()
        print("Sucessful Execution")
    except Error as error:
        mydb.rollback()
        print("Error type: {}".format(error))

# Use to handle SELECT queries
def handle_select(query):
    output = 0
    try:
        mycursor.execute(query)
        output = mycursor.fetchall()
    except Error as error:
        print("Error type: {}".format(error))

    return output
