import mysql.connector


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='user',
                                            password='pass',
                                            host='localhost',
                                            port='3306',
                                            database='sales')
    except Exception as error:
        print("Error while connecting to database for job tracker",error)
    return connection

conn = get_db_connection()

cursor = conn.cursor()