import pandas as pd
import csv
def load_third_party(connection, csv_file): 
    cursor = connection.cursor()
    
    insert_statement = ("""INSERT INTO SALES (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)""")
    # insert_statement = ("""INSERT INTO sales.SALES(ticket_id) VALUES(%s)""")

    with open(csv_file, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=',')
        csv_data_list = list(reader)
        for row in csv_data_list:
            cursor.execute(insert_statement, row)
            print(row)

    connection.commit()
    cursor.close()
    return