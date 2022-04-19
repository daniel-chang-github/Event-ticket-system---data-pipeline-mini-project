import load_data as load
import connection
import pandas as pd
import statistics

print("Here are the most popular tickets in the past month: ")
for result in ((statistics.query_popular_tickets(connection.get_db_connection()))):
    print(result)