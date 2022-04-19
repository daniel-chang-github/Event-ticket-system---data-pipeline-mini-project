import connection as connect

conn = connect.get_db_connection()

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS SALES")

#Creating table as per requirement
sql ='''CREATE TABLE SALES(
   ticket_id INT,
   trans_date DATE,
   event_id INT,
   event_name VARCHAR(50),
   event_date DATE,
   event_type VARCHAR(10),
   event_city VARCHAR(20),
   customer_id INT,
   price DECIMAL,
   num_tickets INT
)'''
cursor.execute(sql)

#Closing the connection
conn.close()