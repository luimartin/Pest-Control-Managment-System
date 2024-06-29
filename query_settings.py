from database import *



def handle_select(query):
    connection = connect_db()
    cursor = connection.cursor()
    output = []
    try:
        cursor.execute(query)
        output = cursor.fetchall()
        print("Retrieval Success")
    except Error as error:
        print("Error type: {}".format(error))
    finally:
        cursor.close()
        connection.close()

    return output

def handle_exec(query):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Committed Execution")
    except Error as error:
        connection.rollback()
        print("Error type: {}".format(error))
    finally:
        cursor.close()
        connection.close()

        # Use to handle insert, update, and delete queries
def handle_transaction(query, data):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Successful Execution")
    except Error as error:
        connection.rollback()
        print("Error type: {}".format(error))
    finally:
        cursor.close()
        connection.close()